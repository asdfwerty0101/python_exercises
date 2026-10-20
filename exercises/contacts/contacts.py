MENU_ITEMS = (
    "добавить", "найти", "удалить", "показать все",
    "сохранить и выйти"
)

contacts_dict = dict()
# загружаю файл contacts.txt в dict
contacts_file = open("contacts.txt", "r")
for line in contacts_file.readlines():
    line_list = line.split(":")
    name = line_list[0]
    phone_number = line_list[1].replace("\n", "")
    # contacts_dict.setdefault(name, phone_number)  # оставляем первое
    # вхождение повторяющихся имен
    contacts_dict[name] = phone_number  # оставляем последнее
    # вхождение повторяющихся имен
contacts_file.close()

while True:
    # показываю меню
    print("-"*5, "Операции над телефонным справочником:", "-" * 5)
    for number, item in enumerate(MENU_ITEMS, 1):
        print(f"{number}.", item)
    # считываю строку с input() и преобразую в int
    choice_str = input("Сделайте выбор, введите число: ")
    try:
        choice_num = int(choice_str)
    except ValueError:
        print("Вы ввели не число, попробуйте еще раз")
        continue
    if choice_num == 1:
        # 1 - добавить
        new_name = input("Введите имя нового контакта:")
        new_phone_number = input("Введите номер нового контакта:")
        if new_name in contacts_dict:
            print("Уже есть такой контакт. Сначала удалите старый контакт")
            continue
        contacts_dict[new_name] = new_phone_number
    elif choice_num == 2:
        # 2 - найти
        name_to_search = input("Введите имя контакта, который ищете:")
        if name_to_search not in contacts_dict:
            print("не найден")
            continue
        print(contacts_dict[name_to_search] )
    elif choice_num == 3:
        # 3 - удалить
        pass
    elif choice_num == 4:
        # 4 - показать все
        pass
    elif choice_num == 5:
        # 5 - сохранить и выйти
        contacts_file = open("contacts.txt", "w")
        for name, phone_number in contacts_dict.items():
            contacts_file.write(f"{name}:{phone_number}\n")
        contacts_file.close()
        exit(0)
    else:
        print("Вы ввели число не из меню, попробуйте еще раз")
        continue