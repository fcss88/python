def handling_exception():
    try:
        previous = float(input("input previous value: "))
        current = float(input("input current value: "))

        differ = 100 * (current - previous) / previous

    except ValueError as error:
        print(f"{error.__class__.__name__}: {error}")
    except ZeroDivisionError as error:
        print(f"{error.__class__.__name__}: {error}")
        differ = current
    except Exception as error:
        print(f"{error.__class__.__name__}: {error}")
        print("Шось пішло не так..")
    else:
        if differ > 0:
            print(f"Value increased {differ:.2g} %")
        else:
            print(f"Value decreased {differ:.2g} %")
    finally:
        print("...")


def run_exc():
    while True:
        handling_exception()
        state = input("Do you want to go on? If yes enter y, else n: ")
        if state.lower() == "n":
            break


def get_numbers(n):
    i = 1
    while i <= n:
        yield i
        i += 1
    return "Все ..."


def run_gen(n):
    it = get_numbers(10)
    try:
        while True:
            v = next(it)
            print(v)
    except StopIteration as err:
        print(err)


if __name__ == "__main__":
    #    run_exc()
    run_gen(7)
