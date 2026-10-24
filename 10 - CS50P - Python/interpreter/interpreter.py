xx, y, zz = input("Expression: ").strip().split()

x = float(xx)
z = float(zz)

def express():
    if y == "+":
        print(x + z)
    elif y == "-":
        print(x - z)
    elif y == "/":
        print(x / z)
    elif y == "*":
        print(x * z)
    else:
        print("add a right exprression")

express()
