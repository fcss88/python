import math

# const
e = 2.72
# input numers
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
try:
    if a < 0:
        print("a менше нуля, не підходе нам таке")
    elif b <= 0:
        print("b менше або рівне нулю, не підходе нам таке")
    else:
        rez = (math.sqrt(a * b) / e**a * b) + (a * e ** (2 * a / b))
    # print
    print(rez)
except:
    print("дані введено не вірно")
