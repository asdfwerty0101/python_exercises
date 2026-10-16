mystring = input("input a number:")
try:
    mynumber = int(mystring)
    print(mynumber * 2)
    a = mynumber - 1
except ValueError as e:
    print("You entered not a number!")
    exit(-10)
except (ErrorA, ErrorB):
    ...
except SomeError as e:
    ...
except:
    ...
else:
    print("все прошло без исключительных ошибок")
finally:
    print("я выполняюсь всегда!")

a  = 1
if a > 3:
    ...
elif a > 6:
    ...
elif a > 7:
    ...
else:
    ...

if a > 3:
    ...

try:
    ...
except:
    ...

print(mynumber)