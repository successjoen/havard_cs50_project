#asking users for meal price and tip percentage
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * (percent/100)
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # separate and delete the dollar sign
    dollars  = d.replace("$", "")
    return float(dollars)


def percent_to_float(p):
    # separate and replace the percentage sign to nothing
    percent = p.replace("%", "")
    return float(percent)


main()
