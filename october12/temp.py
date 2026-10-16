number_str = input(" Please input integer number(int):")

try:
    number = int(number_str)
except ValueError as e:
    print("sorry, this is not an nteger number!")
    print("Please try again")
    number = None
    print(1)

print(234)

print(f"you entered number")