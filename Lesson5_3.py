# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.



salary_list = []
sum = 0
person = 0
with open("text3.txt", "r", encoding="utf-8") as salary_file:
    while True:
        salary_text=salary_file.readline()
        if not salary_text:
            break
        surname, salary = salary_text.split()
        sum += int(salary)
        person += 1
        if int(salary) < 20000:
            salary_list.append(surname)
print(f"Средняя зарплата = {sum/person} \n Сотрудники с заплатой, меньше 20000: {salary_list}")
