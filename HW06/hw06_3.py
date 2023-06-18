"""
Написати функцію, яка приймає ціле число і повертає його двійкове представлення. Не слід використовувати готові функції, хіба для перевірки правильності алгоритму..
"""


def binary(number):
    if number == 0:
        return "0"
    binary_string = ""
    while number > 0:
        binary_string = str(number % 2) + binary_string
        number = number // 2
    return binary_string


cases = [
    ["0", 0],
    ["1", 1],
    ["101", 5],
    ["110", 6],
    ["1011", 11],
    ["1100101", 101],
    ["100100101001", 2345],
    ["11000000111000100", 98756],
]

for i in cases:
    expected, number = i
    result = binary(number)
    assert expected == result, "Wrong convertation.\nExpected: {}\nActual: {}".format(
        expected, result
    )
