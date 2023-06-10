import random
import time

player1 = random.randint(1, 3)
player2 = random.randint(1, 3)

time.sleep(1)

if player1 == 1:
    print("В першого гравця випав Колодязь", end="\t")
elif player1 == 2:
    print("В першого гравця випали Ножиці", end="\t")
else:
    print("В першого гравця випала Бумага", end="\t")
time.sleep(1)

if player2 == 1:
    print("В другого гравця випав Колодязь", end="\t")
elif player2 == 2:
    print("В другого гравця випали Ножиці", end="\t")
else:
    print("В другого гравця випала Бумага", end="\t")

time.sleep(1)

# check
if player1 == 1 and player2 == 2:
    print("Перший гравець виграв")
elif player1 == 1 and player2 == 3:
    print("Другий гравець виграв")
elif player1 == 2 and player2 == 1:
    print("Другий гравець виграв")
elif player1 == 2 and player2 == 3:
    print("Перший гравець виграв")
elif player1 == 3 and player2 == 1:
    print("Перший гравець виграв")
elif player1 == 3 and player2 == 2:
    print("Другий гравець виграв")
else:
    print("Перемогла дружба")
