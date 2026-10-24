import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Get user's cash
    rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    cash = float(rows[0]["cash"])

    # Get user's stock holdings (sum shares per symbol)
    stocks = db.execute("""
        SELECT symbol, SUM(shares) as shares
        FROM transactions
        WHERE user_id = ?
        GROUP BY symbol
        HAVING shares > 0
    """, session["user_id"])

    # Calculate total value for each stock using lookup
    portfolio = []
    total_stocks_value = 0
    for stock in stocks:
        quote = lookup(stock["symbol"])
        total = quote["price"] * stock["shares"]
        total_stocks_value += total
        portfolio.append({
            "symbol": stock["symbol"],
            "name": quote["name"],
            "shares": stock["shares"],
            "price": quote["price"],
            "total": total
        })

    grand_total = cash + total_stocks_value

    return render_template("index.html", portfolio=portfolio, cash=cash, grand_total=grand_total)



@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        # Get form input
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")

        # Validate symbol
        if not symbol:
            return apology("must provide symbol")

        stock = lookup(symbol)
        if stock is None:
            return apology("invalid symbol")

        # Validate shares (must be positive integer)
        if not shares.isdigit() or int(shares) <= 0:
            return apology("shares must be a positive integer")
        shares = int(shares)

        # Check user's cash
        rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = rows[0]["cash"]
        total_price = stock["price"] * shares

        if total_price > cash:
            return apology("can't afford")

        # Update users cash
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_price, session["user_id"])

        # Record the transaction
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
                   session["user_id"], stock["symbol"], shares, stock["price"])

        # Redirect to home page
        return redirect("/")

    else:
        # GET → show buy form
        return render_template("buy.html")



@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("""
        SELECT symbol, shares, price, timestamp
        FROM transactions
        WHERE user_id = ?
        ORDER BY timestamp DESC
    """, session["user_id"])

    # Ensure all fields exist
    for t in transactions:
        t["symbol"] = t.get("symbol", "")
        t["shares"] = t.get("shares", 0)
        t["price"] = t.get("price", 0.0)
        t["timestamp"] = t.get("timestamp", "")

    return render_template("history.html", transactions=transactions)




@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()

        # Validate input
        if not symbol:
            return apology("must provide symbol")

        # Lookup stock
        stock = lookup(symbol)
        if stock is None:
            return apology("invalid symbol")

        # Render quoted.html with stock info
        return render_template("quoted.html", stock=stock)

    else:
        # GET → show quote form
        return render_template("quote.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        # Get form inputs
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Validate inputs
        if not username:
            return apology("must provide username")
        if not password:
            return apology("must provide password")
        if password != confirmation:
            return apology("passwords do not match")

        # Hash password
        hash_pw = generate_password_hash(password)

        # Insert user into database
        try:
            new_user_id = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash_pw)
        except ValueError:
            return apology("username already exists")

        # Log user in
        session["user_id"] = new_user_id

        # Redirect to home page
        return redirect("/")

    # GET request → show registration form
    else:
        return render_template("register.html")




@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        # Get symbol and shares from form
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Validate symbol
        if not symbol:
            return apology("must select a symbol")

        # Validate shares
        if not shares.isdigit() or int(shares) <= 0:
            return apology("shares must be a positive integer")
        shares = int(shares)

        # Check how many shares the user owns
        rows = db.execute("""
            SELECT SUM(shares) as owned
            FROM transactions
            WHERE user_id = ? AND symbol = ?
        """, session["user_id"], symbol)
        owned = rows[0]["owned"]

        if owned is None or shares > owned:
            return apology("not enough shares")

        # Lookup current price
        stock = lookup(symbol)
        if stock is None:
            return apology("invalid symbol")

        # Add cash to user
        total_price = shares * stock["price"]
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total_price, session["user_id"])

        # Record the sale as negative shares
        db.execute("""
            INSERT INTO transactions (user_id, symbol, shares, price)
            VALUES (?, ?, ?, ?)
        """, session["user_id"], symbol, -shares, stock["price"])

        # Redirect to index
        return redirect("/")

    else:
        # GET → show a form with dropdown of owned stocks
        stocks = db.execute("""
            SELECT symbol, SUM(shares) as shares
            FROM transactions
            WHERE user_id = ?
            GROUP BY symbol
            HAVING shares > 0
        """, session["user_id"])

        return render_template("sell.html", stocks=stocks)
