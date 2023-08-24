import logging

while True:
    try:
        numb = int(input("enter age: "))
    except ValueError as e:
        logging.error(e)
        logging.info("only digits!")
    else:
        break

print(f"Yor age is {numb}")
