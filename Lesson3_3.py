# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def addMax(one,two,three):
    list=[one,two,three]
    list.sort()
    return list[2]+list[1]

print(f"Сумма наибольших аргументов = {addMax(1,2,3)}")