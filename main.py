# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет
print ('Введите цифру от 1 до 7 обозначающую день недели: ')

integer = False
while not integer:
    day = input()
    if day.isdigit():
        final = int(day)
        integer = True


day= int(day)

if day > 5 and day<=7:
    print ("Выходной")
elif day >=1 and day <=5:
    print ("Будний")
else:
    print ("Введите корректное челое число от 1 до 7")