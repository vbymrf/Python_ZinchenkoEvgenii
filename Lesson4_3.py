# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.


print([x for x in range(20, 240, 1) if x % 20 == 0 or x % 21 == 0])

# Почему range() выдает  TypeError: 'type' object is not subscriptable Если это не список и не итератор, то что выдает range?
# rag=range[20,240,1]
# print(type(rag))
# rag=iter(range[20,240,1])
# print(next(rag))
