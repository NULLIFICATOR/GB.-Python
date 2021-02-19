# Реализовать склонение слова «процент» для чисел до 20. Например,
# задаем число 5 — получаем «5 процентов», задаем число 2 — получаем
# «2 процента». Вывести все склонения для проверки.

counter = 1
word_end = ""
while counter <= 20:
    if counter == 1:
        word_end = ""
    elif 1 < counter <= 4:
        word_end = "а"
    else:
        word_end = "ов"
    print(counter, "процент" + word_end)
    counter += 1