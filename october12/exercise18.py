"""
Чётное/нечётное. if x % 2 == 0. x - вводится с консоли
"""

number_str = input("please input integer number (int):")

try:
    number = int(number_str)
except ValueError as e:
    print("Sorry, this is not an integer number!")
    print("Please try again")
    exit(1)

the_rest = number % 2
if the_rest == 0:
    print(f"Число {number} четное")
else:
    print(f"Число {number} нечетное")