import math

# input numers
salary = float(input("Введіть розмір своєї заробітньої плати: "))

try:
    if salary == 0:
        print("так а нахіба ти сюди поліз, якщо зарплати не маєш")
    elif salary < 0:
        print("братан, ти ще винен комусь, податки почекатимуть")
    else:
        miltax = salary * 0.015
        pdfo = salary * 0.18
        totally = salary - pdfo - miltax
        print("Платиш податків на доходи фізосіб:\t {:.2f}".format(pdfo))
        print("Платиш податок військового збору:\t {:.2f}".format(miltax))
        print("Отримаєш всього на руки ось таке:\t {:.2f}".format(totally))
except:
    print("щось пішло не так...")
