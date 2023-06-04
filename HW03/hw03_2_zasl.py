# Celsium to Farengeit
import sys


# Add class for colour description
class Colors:
    RED = "\033[91m"
    WHITE = "\033[37m"


# Start arguments
c = 0
f = 32
# table header
print(Colors.RED + "C\u00b0 \t|\t F\u00b0" + Colors.WHITE)

# print(c, "\t|\t", f)
# calculate
while c <= 100:
    f = c * 9 / 5 + 32
    print(c, "\t|\t", f)
    c = c + 1
