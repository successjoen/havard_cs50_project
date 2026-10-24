deep = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

match deep:
    case "forty-two" | "forty two" | "42":
        print("yes")
    case _:
        print("no")
