def main():
    amount_due = 50

    # Loop until the amount due is fully paid or overpaid
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))

        # Only deduct accepted coin denominations
        if coin in [25, 10, 5]:
            amount_due -= coin

    # Calculate change owed (absolute value converts negative remaining balance to positive change)
    print(f"Change Owed: {abs(amount_due)}")


if __name__ == "__main__":
    main()
