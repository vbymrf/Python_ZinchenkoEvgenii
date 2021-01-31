# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
lines = 0
words_in_line = {None:None}
with open("text2.txt", "r") as read_file:
    while True:
        text_line = read_file.readline()
        if not text_line:
            break
        lines += 1
        line = text_line.split()
        words_in_line[lines] = len(line)
        print(f"Cтрока {lines} содержит слов {words_in_line[lines]}")
