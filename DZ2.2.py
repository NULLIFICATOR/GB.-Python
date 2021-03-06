# 2.Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# Необходимо его обработать — обособить каждое целое число
# (вещественные не трогаем) кавычками (добавить кавычку до
# и кавычку после элемента списка, являющегося числом) и дополнить
# нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Подумать, какое условие записать, чтобы выявить числа среди элементов
# списка?
# Как модифицировать это условие для чисел со знаком?
#
# Примечание:
# - Задача обычной сложности: создайте новый список и заполните его нужными
# значениями, включая элементы-кавычки,например:
# ['в', '"', '05', '"', 'часов',...] или измените существующий список,
# но не добавляйте новые элементы-кавычки, кавычки сразу внесите
# в элемент-число, например: ['в', '"05"', 'часов',...]


default_message = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
converted_message_list = []
for item in default_message:
    if item.isdigit():
        number = int(item)
        item = f'"{number:02d}"'
    elif (item[0] == "+" or item[0] == "-") and item[1:].isdigit():
        number = int(item)
        item = f'"{item[0]}{number:02d}"'
    converted_message_list.append(item)
# Заменяем существующий список по условию задачи, хотя я бы сразу выводил измененный
default_message = converted_message_list
print(default_message)
message = ' '.join(default_message)
print(message.capitalize() + '.')
