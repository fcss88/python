def finding_last(nums, steps):
    people = list(range(1, nums + 1))
    current = 0

    while len(people) > 1:
        current = (current + steps - 1) % len(people)
        people.pop(current)

    return people[0]


nums = int(input("Введіть кількість людей: "))
steps = int(input("Введіть крок: "))
last_person = finding_last(nums, steps)

print("остання людина буде під номером", last_person)
