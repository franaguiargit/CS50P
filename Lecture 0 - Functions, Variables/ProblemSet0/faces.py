def convert(input_str):
    converted_input = input_str.replace(":)" , "🙂").replace(":(" , "🙁")
    return converted_input


def main():
    user_input = input("Say something including :) and :( :  ")
    converted_input = print(convert(user_input))
    return converted_input


main()