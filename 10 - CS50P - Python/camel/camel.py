def main():
    word = input("camelCase: ")

    # Loop through each character in the string
    for c in word:
        if c.isupper():
            # Print an underscore followed by the lowercase letter
            print("_" + c.lower(), end="")
        else:
            # Print lowercase letters as-is
            print(c, end="")

    # Print a new line at the end
    print()

if __name__ == "__main__":
    main()
