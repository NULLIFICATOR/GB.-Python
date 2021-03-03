# 5. Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков:
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Например:
#
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.

from random import choice


def get_jokes(num, noun, adv, adj):
    """
    This function create list of jokes. Number of jokes depends on "num" string
    :param num: number of jokes
    :param noun: first word
    :param adv: second word
    :param adj: third word
    :return: list of jokes
    """

    list_of_jokes = []

    length = min(num, len(noun), len(adv), len(adj))
    for item in range(length):
        list_of_jokes.append(f"{choice(nouns)} {choice(adv)} {choice(adj)}")
    return list_of_jokes


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(4, nouns, adverbs, adjectives))
