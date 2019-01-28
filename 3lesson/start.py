from random import randint
import requests


def task1():
    with open("numbers.txt", 'w') as numbres:
        for i in range(10):
            numbres.write(str(randint(1, 100)) + "\n")


def read():
    with open("numbers.txt", 'r') as numbres:
        read_numbers = numbres.read()
        suma = 0
        num_list = read_numbers.split()
        for i in num_list:
            suma += int(i)
        with open("sum_numbers.txt", "w") as sum_numbers:
            sum_numbers.write(str(suma))


def task2():
    with open("learning_python.txt", "r") as learning_python:
        li = []
        re = learning_python.read()
        li.append(re.split("\n"))
    print(li)


def task3():
    with open("learning_python.txt", "r") as learning_python:
        re = learning_python.read()
        res = re.replace("Python", "C")
    print(res)


def task4():
    with open("book.txt", "r") as book, \
            open("formatted_text.txt", "w") as formatted_text:
        res = book.read()
        formatted_text.write(res.replace("\n", " "))


def task5():
    with open("book2.txt", "r") as book2, \
            open("chapters.txt", "w") as chapters:
        for i in book2.readlines():
            if i.startswith("CHAPTER"):
                chapters.write(i)


def task7():
    with open("info.csv", "") as learning_python:
        re = learning_python.read()
        res = re.replace("Python", "C")
    print(res)


def task8():
    resp = requests.get('https://lb.api.openprocurement.org/api/2.4/tenders?offset=2018-03-19.')
    n = resp.json()
    id_plus = ""
    id_plus_1 = 0
    q = 0
    for i in n['data']:
        resp_2 = requests.get('https://lb.api.openprocurement.org/api/2.3/tenders/{}'.format(i["id"]))
        y = resp_2.json()
        if y["data"]["status"] == "complete":
            if y["data"]["value"]["amount"] > id_plus_1:
                id_plus_1 = y["data"]["value"]["amount"]
                id_plus = y["data"]["id"]
        elif y["data"]["status"] == "unsuccessful":
            q += 1
    print("unsuccessful",  q)
    with open("max_contract.json", "w") as max_contract:
        max_contract.write(str(requests.get('https://lb.api.openprocurement.org'
                                            '/api/2.3/tenders/{}'.format(id_plus)).json()["data"]["contracts"]))


if __name__ == "__main__":
    task8()
