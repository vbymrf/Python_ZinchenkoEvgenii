# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.

str=float(input("Time ="))

hour=str//3600
str2=str%3600
second = str2%60
minute = str2//60
print('hour=%d, second = %d,minute = %d' %(hour,second,minute))
