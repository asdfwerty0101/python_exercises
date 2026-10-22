import json

#  читает account.txt
# (одна строка balance) и историю history.txt
def load_account(filename):
    try:
        file = open(filename, "r")
        account_dict = json.load(file)
    except FileNotFoundError:
        print("файл с данным о счете не найден")
        exit(-1)
    except json.JSONDecodeError:
        print("файл с неверным форматом json")
        exit(-2)

    return account_dict["balance"]

#  сохраняет
def save_account(account, filename):
    pass

#  — проверяет,
# что amount > 0 (иначе raise ValueError),
#  прибавляет, пишет в историю "+500"
def deposit(account, amount):
    try:
        amount = float(input("Сумма: "))
        deposit(account, amount)
    except ValueError as e:
        print("Ошибка:", e)
    else:
        print("Успешно. Баланс:", account["balance"])
    finally:
        print("--- операция обработана ---")

#  — проверяет, хватает
# ли средств, вычитает, пишет "-300"
def withdraw(account, amount):
    pass

#  — выводит все операции
# через enumerate
def show_history(account):
    pass

# entry point
def main():
    print(1)
    try:
        balance = load_account("account.txt")
        print(3)
        print(balance)

        while False:
            pass
    except Exception as e:
        print(str(e))
        pass
    else:
        pass
    finally:
        pass


if __name__ == "__main__":
    main()