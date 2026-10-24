
def main():
    time = input("What time is it? ")
    times = convert(time)
    if  times >= 7.0 and times <= 8.0:
        print("breakfast time ")
    elif  times >= 12.0 and times <= 13.0:
        print("lunch time ")
    elif  times >= 18.0 and times <= 19.0:
        print("dinner time ")


def convert(time):
    hour , minutes = time.split(":")
    hour = int(hour)
    minutes = int(minutes)
    minutes = minutes/60
    time = hour + minutes
    time = float(time)
    return time



if __name__ == "__main__":
    main()
