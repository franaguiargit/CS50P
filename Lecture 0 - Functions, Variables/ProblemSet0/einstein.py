def square(number):
    return number * number

user_input = int(input("Insert some weight in KG!: "))  # Convert user input to an integer
speed_of_light = square(3000000005)  # Square of the speed of light

convert_kg_to_joules = user_input * speed_of_light


print(f"Equivalent energy (Joules): {convert_kg_to_joules}")


