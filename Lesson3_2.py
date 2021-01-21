# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def person(name,surname,yearOfAge,city,email,telephone):
    return f"{name} {surname}, проживает в {city}, год рождения {yearOfAge} , email: {email}, телефон {telephone}"

print(person(name="Женя", surname="Зинченко", yearOfAge=1984,city="Sochi",email="vbymrf@bk.ru",telephone="+79883618870"))