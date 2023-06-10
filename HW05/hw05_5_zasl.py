import math

# input variables
a = float(input("Введи ціле додатнє число більше одиниці:"))

if a <= 1 or not a.is_integer():
    print("то нам не підходе, йди геть")
    exit()
else:
    print("ok")

i = 2
checker = True

while i <= a:
    if a % i == 0 and i != a:
        checker = False
        break
    i += 1

if checker:
    print("число є простим")
else:
    print("число не просте")
