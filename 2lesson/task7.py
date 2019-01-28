def logg(func):
    def inner(*args, **kwargs):
        with open('logg.txt', 'a') as logg_file:
            logg_file.write(str(args)+"\n")
            logg_file.write(str(kwargs))
            result = func(*args, **kwargs)
            logg_file.write('Arguments are written\n')
            return result

    return inner


@logg
def add(*args):
    return sum(args)


@logg
def multiply(*args):
    result = 1
    for x in args:
        result = result * x
    return result


if __name__ == "__main__":
    add(32, 23, 323)
    multiply(23, 324, 43, 34)
