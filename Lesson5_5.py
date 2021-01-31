# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
text_line = None
with open("text5.txt", "w") as open_file:
    while text_line != "":
        text_line = input("Введите строку:   ")
        open_file.write(text_line+"\n")
text_line = "  "
sum = 0
with open("text5.txt", "r") as count_file:
        text_line = count_file.read()
list_sum = text_line.split()
for number in list_sum:
    if number.isdigit():
        sum += float(number)
print(f" Сумма чисел в файле = {sum}")