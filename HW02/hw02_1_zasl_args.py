# -*- coding: utf-8 -*-
import sys


# Add class for colour description
class Colors:
    RED = "\033[91m"


# Check arguments
if len(sys.argv) != 4:
    print(
        Colors.RED
        + "Недостатньо аргументів, необхідно ввести ПІБ трьома словами"
        + Colors.RED
    )
else:
    # Print greetings
    print("Привіт,", sys.argv[1], sys.argv[2], sys.argv[3])

# print("Ім'я файлу: ", sys.argv[0])
