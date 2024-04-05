# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


print ('Введите координаты точки (X и Y): ')

while True:
    N = 2
    day = [0]*N
    for i in range (N):
        print ("day[",i,"=", sep="", end="")
        day[i] = input()
        try:
            day = [float(i) for i in day]
        except ValueError:
            print("Это не правильный ввод. Это не число вообще! Это строка, попробуйте еще раз.")

def checkCoordinates(xy):
    text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    print(f"Точка находится в {text} четверти плоскости")