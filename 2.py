# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


print ('Введите цифру от 1 до 7 обозначающую день недели: ')

integer = False
while not integer:
    day = input()
    if day.isdigit():
        final = int(day)
        integer = True

print(integer)

day= int(day)

if day > 5 and day<=7:
    print ("Выходной")
elif day >=1 and day <=5:
    print ("Будний")
else:
    print ("Введите корректное челое число от 1 до 7")