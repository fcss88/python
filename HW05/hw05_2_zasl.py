# input variables
h = float(input("Введи висоту дверей: "))
w = float(input("Введи ширину дверей: "))
a = float(input("Введи розмір коробки a: "))
b = float(input("Введи розмір коробки b: "))
c = float(input("Введи розмір коробки c: "))
# check
if h <= 0 or w <= 0 or a <= 0 or b <= 0 or c <= 0:
    print("Некоректно введено дані")
    exit()

if a < h and b < w:
    print("влізе")
elif b < h and a < w:
    print("влізе")
elif c < h and a < w:
    print("влізе")
elif a < h and c < w:
    print("влізе")
elif b < h and c < w:
    print("влізе")
elif c < h and b < w:
    print("влізе")
else:
    print("Не влізе")
