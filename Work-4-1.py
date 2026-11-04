#Розраховувати кількість днів між заданою та поточною датами.

# Імпортуємо модуль
from datetime import datetime, timedelta
# створення об'єктів date 

try:
    input_year = int(input("Введіть рік (Приклад: 1951) >>> "))

except ValueError:
    print("Введіть число")
except Exception as e:
    print ()

#input_manth = input("Введіть місяць (Приклад: 11) >>> ")
# input_day = input("Введіть день (Приклад: 16) >>> ")

date = datetime(input_year, 11, 13)

def get_days_from_today(date):
    return datetime.today() - date

print(date)
nomer = int("".join(list(str([get_days_from_today(date)]).split().pop(0))[25:-1]))


# nomer_1 = str(nomer) #кажу змінній що це строка
# print (nomer_1)
# nomer_2 = nomer_1.split() # виділяю елементи
# print (nomer_2)
# nomer_3 = nomer_2.pop(0) # залишаю перший елемент
# print (nomer_3)
# nomer_4 = list(nomer_3) # дроблю на елементи
# print (nomer_4)
# nomer_5 = nomer_4[25:-1] # виділяю зріз там де номер
# print (nomer_5)
# nomer_6 = int("".join(nomer_5)) # поєдную нумерацію
# print (nomer_6)

print(f"Кількість днів між датами {nomer}")