import decimal

# input numers

try:
    salary = decimal.Decimal(input("Введіть розмір своєї заробітньої плати: "))
    salary_decimal = decimal.Decimal(salary)
    #    print("Ваша зарплата:", salary_decimal)

    if salary_decimal == decimal.Decimal("0"):
        print("так а нахіба ти сюди поліз, якщо зарплати не маєш")
    elif salary_decimal < decimal.Decimal("0"):
        print("братан, ти ще винен комусь, податки почекатимуть")
    else:
        miltax = salary_decimal * decimal.Decimal("0.015")
        pdfo = salary_decimal * decimal.Decimal("0.18")
        totally = salary_decimal - pdfo - miltax
        print(
            "Платиш податків на доходи фізосіб:\t",
            pdfo.quantize(decimal.Decimal("0.01"), rounding=decimal.ROUND_HALF_UP),
        )
        print(
            "Платиш податок військового збору:\t",
            miltax.quantize(decimal.Decimal("0.01"), rounding=decimal.ROUND_HALF_UP),
        )
        print(
            "Отримаєш всього на руки ось таке:\t",
            totally.quantize(decimal.Decimal("0.01"), rounding=decimal.ROUND_HALF_UP),
        )
except decimal.InvalidOperation:
    print("Введено некоректні дані")
