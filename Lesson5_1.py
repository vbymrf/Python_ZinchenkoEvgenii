# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
text_line = None
with open("text1.txt", "w") as open_file:
    while text_line != "":
        text_line= input("Введите строку:   ")
        open_file.write(text_line+"\n")

