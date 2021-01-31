# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# # Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

metodol = {}
list_met = []
with open("text6.txt", "r", encoding="utf8") as file_met:

    while True:
        line_txt = file_met.readline()
        if not line_txt:
            break
        line_met = line_txt.split()
        sum = 0
        for i in range(1,len(line_met)):
            number = ""
            for simbol in line_met[i]:
               if simbol.isdigit():
                   number += simbol
               else:
                   break
            if number.isdigit():
                sum += int(number)
        metodol[line_met[0]] = sum
print(metodol)