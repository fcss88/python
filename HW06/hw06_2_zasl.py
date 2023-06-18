"""
Вам треба написати функцію мовою Пайтон, яка приймає три параметри: наявну суму грошей, потрібну суму та річний банківський процент по депозиту. Функція повертає кількість років необхідних для зростання депозиту до потрібної суми.
"""


def calculate_period(amount, expected, percent):
    if amount < 0:
        return None

    year = 0
    while amount < expected:
        needed = amount * (percent * 0.01)
        amount += needed
        year += 1
    return year


cases = [[30, (1000, 10000, 8)], [22, (40000, 1000000, 16)], [0, (1000, -20000, 8)]]

for i in cases:
    expected, inputs = i
    result = calculate_period(*inputs)
    assert expected == result, "Wrong convertation.\nExpected: {}\nActual: {}".format(
        expected, result
    )
