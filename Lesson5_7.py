# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

list_firm = []
dict_firm = {}
sum = 0
sum_firm = 0
with open("text7.txt", "r", encoding="utf8") as firm_file:
    while True:
        text_line = firm_file.readline()
        if not text_line:
            break
        text_list = text_line.split()
        profit = int(text_list[2]) - int(text_list[3])
        dict_firm[text_list[0]] = profit
        if profit > 0:
            sum += profit
            sum_firm += 1
list_firm.append(dict_firm)
list_firm.append({"average_profit": sum/sum_firm})

print(list_firm)

with open("text7_1.txt", "w", encoding="utf8") as file_json:
    json.dump(list_firm, file_json)