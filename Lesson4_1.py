# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys

def count_per(breakdown,rate,prize):
    return float(breakdown)*float(rate)+float(prize)

breakdown,rate,prize =  sys.argv[1:]

print(count_per(breakdown,rate,prize))