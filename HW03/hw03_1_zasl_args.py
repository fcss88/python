import sys


# Add class for colour description
class Colors:
    RED = "\033[91m"


# Check arguments
if len(sys.argv) != 3:
    print(
        Colors.RED
        + "Потрібно ввести тільки два аргумента для виконання операції"
        + Colors.RED
    )
else:
    try:
        FirstNumber = float(sys.argv[1])
        SecondNumber = float(sys.argv[2])

        sum = FirstNumber + SecondNumber
        print("Сума двох чисел що ви передали командним рядком: ", sum)
    except ValueError:
        print(Colors.RED + "Некоректно введені дані" + Colors.RED)
