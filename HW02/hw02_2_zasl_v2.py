import sys


# Add class for colour description
class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"


# Check arguments
# add analyze arguments and show an error
if len(sys.argv) != 4:
    print(Colors.GREEN + "Недостатньо аргументів для виконання операції" + Colors.GREEN)
else:
    try:
        FirstNumber = float(sys.argv[1])
        op = sys.argv[2]
        SecondNumber = float(sys.argv[3])
    except:
        print("це не число")
        exit()
try:
    if op == "+":
        result = FirstNumber + SecondNumber
    elif op == "-":
        result = FirstNumber - SecondNumber
    elif op == "*" or op == "x" or op == "X":
        result = FirstNumber * SecondNumber
    elif op == ":" or op == "/":
        if SecondNumber != 0:
            result = FirstNumber / SecondNumber
        else:
            raise ZeroDivisionError("На нуль може ділити тільки Залужний")
    else:
        raise ValueError("Це не оператор: " + op)

    print("Результат", result)
except Exception as e:
    print(
        Colors.RED + "Помилка при виконанні арифметичної операції:" + Colors.RED, str(e)
    )
