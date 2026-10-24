from cs50 import get_int


def main():
    height = get_height()
    for i in range(1, height + 1):
        # Print spaces then hashes; no trailing spaces
        print(" " * (height - i) + "#" * i)


def get_height():
    # Prompt until the user gives an int between 1 and 8 inclusive
    while True:
        n = get_int("Height: ")
        if 1 <= n <= 8:
            return n


if __name__ == "__main__":
    main()
