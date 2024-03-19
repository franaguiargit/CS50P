time = input("What time is it?: ")

hours, minutes = time.split(":")

def convert(hours, minutes):
    timeToFloat = int(hours) + round(int(minutes)/60, 2)
    if 7 <= timeToFloat <= 8:
        print("breakfast time")
    elif  12 <= timeToFloat <= 13:
        print("lunch time")
    elif 18 <= timeToFloat <= 19:
        print("dinner time")
    else:
        print("Enjoy the day")

convert(hours, minutes)

