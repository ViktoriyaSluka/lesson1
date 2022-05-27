"""
Реализовать вывод информации о промежутке времени в зависимости от его
продолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""

def naive_realisation():
    duration = int(input('Inter duration: '))
    DAYS = duration // 86400
    HOURS = (duration - DAYS * 86400) // 3600
    MINUTES = (duration - DAYS * 86400 - HOURS * 3600) // 60
    SECONDS = (duration - DAYS * 86400 - HOURS * 3600 - MINUTES * 60) % 60

    if DAYS == 0 and HOURS == 0 and MINUTES == 0:
        print(f'{SECONDS} сек')
    elif DAYS == 0 and HOURS == 0:
        print(f'{MINUTES} мин {SECONDS} сек')
    elif DAYS == 0:
        print(f'{HOURS} час {MINUTES} мин {SECONDS} сек')
    else:
        print(f'{DAYS} дн {HOURS} час {MINUTES} мин {SECONDS} сек')


if __name__ == '__main__':
    naive_realisation()