from random import randint


def task1(*args):
    result = max(args)
    print(result)


def task2():
    list_word = ["wrewrer", "ewrqwerwerqwer", "werqerrwerqw", "w", "ewefwefewfweqffwefqwefewfqwfwefwf"]
    res = ""
    for i in list_word:
        if len(i) > len(res):
            res = i
    print(res)


def task3():
    result = 0
    while result < 100:
        result += randint(1, 10)
    print(result)


def fins_super(num):
    res = 0
    for i in str(num):
        res += int(i)
    if res > 10:
        return fins_super(res)
    else:
        return res


def len_of_args(*args):
    return len(args)


def rand_of_el():
    res = len_of_args(2343, 423434, 2343434) - len_of_args(234234, 2342343242, 234234234)
    print(res)


def task6():
    li = [12, 12, 14, 4, 13, 4, 12, 65885, 1, 1]
    res = []
    for i in li:
        if i not in res:
            res.append(i)
    print(res)


def deprecated_add(*args, **kwargs):
    def wrapper(func):
        def inner(*args, **kwargs):
            return add(*args)
        return inner
    return wrapper


def add(*args):
    return sum(args)


@deprecated_add(add)
def add_old(*args):
    res = 0
    for i in args:
        res += i
    return res


def task11():
    di = {"square": lambda x: x ** 2, "cubic": lambda x: x ** 3, "four": lambda x: x ** 4, "five": lambda x: x ** 5}
    for i in di:
        print(di[i](randint(10, 20)))


def task12():
    li = []
    for i in range(5):
        li_2 = []
        li.append(li_2)
        for x in range(5):
            li_2.append(randint(1, 100))
    print(sorted(li, key=lambda x: x[3]))


def retry(func):
    def wrapper():
        for i in range(10):
            try:
                res = func()
                return res
            except:
                continue
        print("NO RESULT")

    return wrapper


@retry
def gen_random():
    num = randint(1, 10)
    if num == 1:
        return num
    raise Exception()


def run():
    print(gen_random())


if __name__ == "__main__":
    run()
