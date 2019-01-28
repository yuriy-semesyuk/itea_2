from string import ascii_letters


def task1():
    print(input("Введіть строку\n")[-1::-1])


def task2():
    inp = input("Введіть строку\n")
    count = 1
    for i in inp:
        if i.isupper():
            count += 1
    print(count)


def task3():
    inp = input("Введіть строку\n")
    result = True
    for i in inp:
        if i not in ascii_letters:
            result = False
            break
    print(result)


def task4():
    inp = input('Enter S\n')
    final_list = []
    for letter in inp:
        temp_list = final_list
        final_list = []
        if temp_list:
            for existing_word in temp_list:
                final_list.append(existing_word + letter.upper())
                final_list.append(existing_word + letter.lower())
        else:
            final_list.append(letter.upper())
            final_list.append(letter.lower())
    print(final_list)


def task5():
    number = "209210"
    result = ''
    count = 0
    for i in range(1, (len(number))):
        while len(number) > len(result):
            result += str(int(number[:i]) + count)
            count += 1
        if result == number:
            break
        count = 0
        result = ''
    if result:
        print("YES")
    else:
        print("NO")


def task6():
    dic = {"numbers": "0123456789", "lower_case": "abcdefghijklmnopqrstuvwxyz",
           "upper_case": "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "special_characters": "!@#$%^&*()-+"}

    li = ["numbers", "lower_case", "upper_case", "special_characters"]

    password = input("PASSWORD: ")
    for i in password:
        for x in dic:
            if i in dic[x] and x in li:
                li.remove(x)
    if len(password) < 6:
        print("Добавте ще {} символ(и)".format(6 - len(password)))
    if li:
        print("Добавте ще такі символи:")
        for i in li:
            print(" - ", dic[i])


if __name__ == "__main__":
    task5()
