# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


print ('Введите координаты точки (X и Y): ')


N = 2
coord = [0]*N
for i in range (N):
    print ("координаты оси[",i,"=", sep="", end="")
    coord[i] = input()
    try:
        coord = [float(i) for i in coord]
    except ValueError:
        print("Это не правильный ввод. Это не число вообще! Это строка, попробуйте еще раз.")

def checkCoordinates(coord):
    text = 4
    if coord[0] > 0 and coord[1] > 0:
        text = 1
    elif coord[0] < 0 and coord[1] > 0:
        text = 2
    elif coord[0] < 0 and coord[1] < 0:
        text = 3
    print(f"Точка находится в {text} четверти плоскости")

checkCoordinates(coord)