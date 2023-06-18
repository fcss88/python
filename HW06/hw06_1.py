"""
Напишіть реалізацію функції closest_mod_5, яка приймає один цілочисельний аргумент
та повертає найменше число y, яке:
y >= x
y % 5 == 0
"""


def closest_mod_5(x):
    if x % 5 == 0:
        return x
    else:
        return x + (5 - x % 5)


cases = [
    # expected, input
    [5, 5],
    [15, 13],
    [0, 0],
    [0, -1],
    [-15, -16],
    [10, 7],
    [15, 12],
    [20, 18],
    [30, 28],
]

for i in cases:
    expected, inp = i
    res = closest_mod_5(inp)
    assert expected == res, "Fail. Expected: {}\nActual: {}".format(expected, res)
#    print("Input: {}, Expected: {}, Actual: {}".format(inp, expected, res))
