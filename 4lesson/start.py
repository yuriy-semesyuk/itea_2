


class Shop:

    def __init__(self, shop_name, shop_type):
        self.shop_name = shop_name
        self.shop_type = shop_type

    def discribe_shop(self):
        print(f"{self.shop_type}")

    def open_shop(self):
        print(f"{self.shop_name}")


class User:

    login_atemps = 0

    def __init__(self, first_name, last_name, age, email, login_atemps = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_atemps = login_atemps

    def describe_user(self):
        print(f'{self.first_name} {self.last_name}')

    def greeting_user(self):
        print(f'Hello {self.first_name}')

    def increment_login_atemps(self):
        login_atemps += 1

    def reset_login_atemps(self):
        login_atemps = 0


if __name__ == "__main__":
    user_1 = User("Yuriy", "Semesyuk", 25, "s@s.s")
    user_2 = User("Igor", "Kora", 44, "c@c.c")
    user_3 = User("Vasya", "bonch", 62, "t@t.t")
    user_1.describe_user()
    user_1.greeting_user()
    user_2.describe_user()
    user_2.greeting_user()
    user_3.describe_user()
    user_3.greeting_user()