import random


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# choose algoritm
def sort_list(arr, algorithm):
    if algorithm == "quick":
        return quick_sort(arr)
    elif algorithm == "merge":
        return merge_sort(arr)
    elif algorithm == "selection":
        return selection_sort(arr)
    elif algorithm == "insertion":
        return insertion_sort(arr)
    else:
        print("Невідомий алгоритм сортування.")
        return None


# generate array of 20 random numbers
my_list = [
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
print("Наш список", my_list)
print("Алгоритм merge:", end="\t\t")
selected_algorithm = "merge"
sorted_list = sort_list(my_list, selected_algorithm)
print(sorted_list)

print("Алгоритм quick:", end="\t\t")
selected_algorithm = "quick"
sorted_list = sort_list(my_list, selected_algorithm)
print(sorted_list)

print("Алгоритм selection:", end="\t")
selected_algorithm = "selection"
sorted_list = sort_list(my_list, selected_algorithm)
print(sorted_list)

print("Алгоритм insertion:", end="\t")
selected_algorithm = "insertion"
sorted_list = sort_list(my_list, selected_algorithm)
print(sorted_list)
