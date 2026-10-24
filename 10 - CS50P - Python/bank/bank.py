def main():
    greet = input("Greetings: ").lower().strip()
    if startwithello(greet):
        print("$0")
    elif startwithH(greet):
        print("$20")
    else:
        print("$100")

def startwithH(h):
    if h.startswith("h"):
        return True
    else:
        return False

def startwithello(hello):
    if hello.startswith("hello"):
        return True
    else:
        return False
main()
