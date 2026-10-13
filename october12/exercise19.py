"""
Положительное/отрицательное/ноль. Три ветки через elif. Анализируемое число x вводится с консоли
"""

number_str = input("please input integer number (int):")

try:
    number = int(number_str)
except ValueError as e:
    print("Sorry, this is not an integer number!")
    print("Please try again")
    exit(1)

if number < 0:
    print(f"Число {number} отрицательное")
elif number == 0:
    print(f"Число {number} равно нулю")
else:
    print(f"Число {number} положительное")

if number == 40:
    print(f"Вы ввели число 40!")
else:
    # TODO сделать позднее в понедельник
    pass


