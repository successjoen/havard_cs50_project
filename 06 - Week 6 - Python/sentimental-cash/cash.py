from cs50 import get_float

# keep bugging the user until they give us a non-negative number
while True:
    dollars = get_float("Change owed: ")
    if dollars >= 0:
        break

# convert dollars to cents (no decimals messing stuff up)
cents = round(dollars * 100)

coins = 0

# quarters (25¢)
coins += cents // 25
cents %= 25

# dimes (10¢)
coins += cents // 10
cents %= 10

# nickels (5¢)
coins += cents // 5
cents %= 5

# pennies (1¢)
coins += cents

# just print the number of coins, nothing fancy
print(coins)
