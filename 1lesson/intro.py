from random import randint


def task1():
    list_num = input("Введіть читсло:  ")
    res = 0
    for i in list_num.split():
        res += int(i)
    print(res)


def task2():
    rivers = {'Amazon': 'South America', 'Dnipro': 'Ukraine', 'Ren': 'Gepman', }
    for i in rivers:
        print("The {} runs through {}.".format(i, rivers[i]))


def task3():
    e2g = {'stork': 'storch', 'hawk': 'falke', 'woodpecker': 'specht', 'owl': 'eule'}
    print("{} : {}".format('owl', e2g['owl']))
    e2g["yes"] = "ya"
    e2g["not"] = "nine"
    lid_dict = []
    for i in e2g:
        lid_dict.append([i, e2g[i]])
    print(lid_dict)


inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']}


def task4():
    inventory["pocket"] = ['seashell', 'strange berry', 'lint']
    print(sorted(inventory['backpack']))
    print(inventory['backpack'].remove("dagger"))
    print(inventory["gold"] + 50)


def task5():
    prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
    stocks = {}
    total = 0
    for i in prices:
        stocks[i] = randint(1, 100)
        total += prices[i] + stocks[i]
        print("{} {}$ - {}".format(i, prices[i], stocks[i]))
    print("TOTAL: {}$".format(total))


def average(li):
    return sum(li)/len(li)


def get_letter_grade(number):
    if number > 89:
        return "A"
    elif 89 < number < 69:
        return "B"
    elif 69 < number < 49:
        return "C"
    else:
        return "D"


def task6():
    lloyd = {"name": "Lloyd", "homework": [90.0, 97.0, 75.0, 92.0], "quizzes": [88.0, 40.0, 94.0],
             "tests": [75.0, 90.0]}
    alice = {"name": "Alice", "homework": [100.0, 92.0, 98.0, 100.0], "quizzes": [82.0, 83.0, 91.0],
             "tests": [89.0, 97.0]}
    tyler = {"name": "Tyler", "homework": [0.0, 87.0, 75.0, 22.0], "quizzes": [0.0, 75.0, 78.0],
             "tests": [100.0, 100.0]}

    students = [lloyd, alice, tyler]

    for i in students:
        print("{}\n    homework - {}\n    quizzes - {}\n    tests - {}"
              .format(i["name"], i["homework"], i["quizzes"], i["tests"]))

    for i in students:
        print("{} - {}".format(i["name"], get_letter_grade(average(i["homework"]))))

    res = []

    for i in students:
        res.append(average(i["tests"]))
    print(int(average(res)), get_letter_grade(average(res)))


if __name__ == "__main__":
    task6()
