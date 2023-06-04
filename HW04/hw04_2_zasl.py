import math

pi = 3.14
# input numers
x = float(input("Введіть x: "))
mju = float(input("Введіть μ: "))
sigma = float(input("Введіть σ: "))

try:
    if sigma == 0:
        print("σ дорівнює нулю, не підходе нам таке")
    else:
        rez = (1 / sigma * math.sqrt(2 * pi)) * math.exp(
            -((x - mju) ** 2) / (2 * sigma**2)
        )
    # print
    print(rez)
except:
    print("дані введено не вірно, нуль в знаменнику")
