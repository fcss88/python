# input surname
num = float(input("Введіть число: "))
i = 1
print("num \t| \t num\u00B2 \t| \t num\u00B3")
while i < int(num):
    print(i, "\t|\t", i * i, "\t|\t", i * i * i)
    i += 1
