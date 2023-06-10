import math

# input variables
a = float(input("Введи a: "))
b = float(input("Введи b: "))
c = float(input("Введи c: "))

if a == 0:
    print("Це не квадратне рівняння, йди геть")
    exit()

d = b * b - 4 * a * c
if d < 0:
    print("рівняння розвязків немає")
    exit()
elif d == 0:
    print("Рівняння має єдиний корінь:", end=" ")
    x = -b / (2 * a)
    print(x)
    exit()

else:
    print("Рівняння має два корені", end=" ")
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    print(x1, x2)
