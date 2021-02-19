# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности
# duration в секундах. Формат вывода результата:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# в остальных случаях: <d> дн <h> час <m> мин <s> сек.
#
# Примеры:
# duration = 53
# 53 сек
#
# duration = 153
# 2 мин 33 сек
#
# duration = 4153
# 1 час 9 мин 13 сек
#
# duration = 400153
# 4 дн 15 час 9 мин 13 сек
# Примечание: можете проверить себя здесь: https://www.epochconverter.com/

duration = int(input("Введите длительность события в секундах: "))
days = duration // 86400
hours = duration // 3600
minutes = duration // 60


if duration < 60:
    print("Длительность: ", duration, " сек")
elif 60 <= duration < 3600:
    remains = duration % minutes
    print("Длительность: ", minutes, "мин.", remains, "сек.")
elif 3600 <= duration < 86400:
    remain_minutes = minutes % 60
    remain_seconds = duration % minutes
    print("Длительность: ", hours, "ч.", remain_minutes, "мин.", remain_seconds, "сек.")
elif 86400 <= duration:
    remain_days = days % 24
    remain_hours = (duration-(remain_days*24*3600))//3600
    remain_minutes = minutes % 60
    remain_seconds = duration % minutes
    print("Длительность: ", remain_days, "дн.", remain_hours, "ч.", remain_minutes, "мин.", remain_seconds, "сек.")
