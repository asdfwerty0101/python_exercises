"""
Условие задачи:
Чётное/нечётное. if x % 2 == 0. x - вводится с консоли
"""

# беру с консоли число в виде строки
number_str = input("please input integer number (int):")

try:
    # перевожу строку в число с помощью int()
    number = int(number_str)
except ValueError as e:
    # обнаружено исключение - пользователь ввел не цифры
    print("Sorry, this is not an integer number!")
    print("Please try again")
    # аварийный выход
    exit(1)
    number = None

# ОК. У меня есть число
# нахожу остаток от деления на 2
the_rest = number % 2

if the_rest == 0:
    # число четное
    print(f"Число {number} четное")
else:
    # число нечетное
    print(f"Число {number} нечетное")