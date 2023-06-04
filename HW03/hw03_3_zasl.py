# input numers
weight = float(input("Введіть вагу в кг: "))
height = float(input("Введіть зріст в м: "))
# print Body Mass Index
bmi = weight / (height * height)
print("Індекс маси тіла:", bmi)
# bmi analyse
if bmi < 19:
    print("Дрищ")
elif bmi >= 19 and bmi <= 25:
    print("Норм")
else:
    print("Жирдос")
