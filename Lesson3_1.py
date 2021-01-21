# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
noExcept=True
while(noExcept):
    temp1 = float(input("Введите число 1="))
    temp2 = float(input("Введите число 2="))


    def division(one, two):
        global noExcept  # не рекомендуется, как тогда быть?
        try:
            noExcept=False
            return one / two
        except ZeroDivisionError:
            print("Делить на ноль нельзя. Укажите числа заново.")
            noExcept=True

    print(f'{temp1}/{temp2}={division(temp1,temp2)}')