# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

rus_words = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("text4.txt", "r", encoding="utf8") as file_open:
    with open("text4_1.txt", "w", encoding="utf8") as file_translate:
        while True:
            words = file_open.readline().split()
            if not words:
                break
            for i in range(0,len(words)):
                if rus_words.get(words[i]) != None:
                    words[i] = rus_words[words[i]]
            text = " ".join(words)
            file_translate.write(text+'\n')