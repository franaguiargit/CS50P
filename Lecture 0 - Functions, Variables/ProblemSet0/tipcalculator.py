def main():
    dollars = float(input("How much was the meal? "))
    percent = float(input("What percentage would you like to tip? "))
    percent /= 100  # Convert percentage to decimal
    tip = dollars * percent
    print(f"I'll leave ${tip:.2f}, thank you")

main()
