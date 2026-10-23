import json

#  читает account.txt
# (одна строка balance) и историю history
def load_account(filename):
    try:
        file = open(filename, "r")
        account_dict = json.load(file)
    except FileNotFoundError:
        print("файл с данным о счете не найден")
        exit(1)
    except json.JSONDecodeError:
        print("файл с неверным форматом json")
        exit(2)

    return account_dict

#  сохраняет
def save_account(account, filename):
    pass

#  — проверяет,
# что amount > 0 (иначе raise ValueError),
#  прибавляет, пишет в историю "+500"
def deposit(account, amount):
    if amount <= 0:
        raise ValueError("amount is less than 0")
    account["balance"] += round(amount)
    account["history"].append(f"+{round(amount)}")

#  — проверяет, хватает
# ли средств, вычитает, пишет "-300"
def withdraw(account, amount):
    if amount <= 0:
        raise ValueError("amount is less than 0")

    if account["balance"] < amount:
        raise ValueError(f"Not sufficient balance. Balance is less than "
                         f"{amount}")
    account["balance"] -= round(amount)
    account["history"].append(f"-{round(amount)}")

#  — выводит все операции
# через enumerate
def show_history(account):
    print("Operations history:")
    for index, operation in enumerate(account["history"], 1):
        print(f"{index}. {operation}")

def show_menu():
    print("Choose operation:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show history")
    print("4. Quit")


# entry point
def main():
    try:
        account = load_account("account.txt")

        while True:
            show_menu()
            user_choice = input("Your choice (1-4):")
            user_choice = user_choice.strip()
            if user_choice in ["1", "2"]:
                # deposit or withdraw
                try:
                    amount = float(input("Amount: "))
                    if user_choice == "1":
                        deposit(account, amount)
                    else:
                        withdraw(account, amount)
                except ValueError as e:
                    print("Error:", e)
                else:
                    print("Success. Balance:", account["balance"])
                finally:
                    print("--- operation completed ---")
            elif user_choice == "3":
                # show history
                show_history(account)
            elif user_choice == "4":
                # quit
                print("minibank finished!")
                return
            else:
                print("Please try again. Input numbers 1-4")

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