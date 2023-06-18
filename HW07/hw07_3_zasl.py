import random


def average(lst):
    if len(lst) == 0:
        return 0
    return sum(lst) / len(lst)


def median(lst):
    sorted_lst = sorted(lst)
    print("Сортований список:", end=" ")
    n = len(sorted_lst)
    if n % 2 == 0:
        mid1 = sorted_lst[n // 2 - 1]
        mid2 = sorted_lst[n // 2]
        for i in sorted_lst:
            if i == mid1 or i == mid2:
                print("\033[91m" + str(i) + "\033[0m", end=" ")
            else:
                print(i, end=" ")
        print("\n")
        return (mid1 + mid2) / 2
    else:
        mid = sorted_lst[n // 2]
        for i in sorted_lst:
            if i == mid:
                print("\033[91m" + str(i) + "\033[0m", end=" ")
            else:
                print(i, end=" ")
        print("\n")
        return mid


numbers = [
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
]
print("Наш масив чисел, парна кількість: ", numbers)
avg = average(numbers)
med = median(numbers)
print("Середнє значення:", avg)
print("Медіана:", med)

numbers2 = [
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
    random.randint(1, 100),
]
print("Наш масив чисел, непарна кількість: ", numbers2)
avg = average(numbers2)
med = median(numbers2)
print("Середнє значення:", avg)
print("Медіана:", med)
