# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
yearList=["","январь","февраль","март","апрель","май","июнь","июль","август","сентябрь","октябрь","ноябрь","декабрь"]
yearDict={}
for l in range(len(yearList)):
    yearDict[l]=yearList[l]

print(yearDict)
per=int(input("Введите номер месяца ="))
# Лист
print(f"Номер {per} соответсвует месяцу = {yearList[per]}")
# Словарь
print(f"Номер {per} соответсвует месяцу = {yearDict[per]}")