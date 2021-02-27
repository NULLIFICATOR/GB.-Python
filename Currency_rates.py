# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код
# валюты (USD, EUR, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать
# вместо float тип Decimal? Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.
#
def currency_rates(cur_name):

    import requests

    r = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    message = r.text
    finder = message.find('USD')
    _a = finder + 50
    _b = finder + 80
    value_finder = message.find(',', _a, _b)
    _c = value_finder - 3
    _d = value_finder + 5
    v = message[_c:_d:1]
    j = v.split()
    s = []
    for item in v:
        if item.isdigit():
            number = int(item)
            item = f'"{number}"'
    s.append(item)
    print(s)
