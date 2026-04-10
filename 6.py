import re

class Account:
    def __init__(self, login: str, email: str, password: str, phone: str):
        self.__login = login
        self.__email = email
        self.__password = password
        self.__phone = phone

    @property
    def login(self):
        return self.__login

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

    @property
    def phone(self):
        return self.__phone

    @login.setter
    def login(self, value):
        if Account.validate_login(value):
            self.__login = value
        else:
            raise ValueError("Неыерний формат логина")

    @email.setter
    def email(self, value):
        if Account.validate_email(value):
            self.__email = value
        else:
            raise ValueError("Неверый формат gmail")

    @password.setter
    def password(self, value):
        if Account.validate_password(value):
            self.__password = value
        else:
            raise ValueError("неверний формат пароля")

    @phone.setter
    def phone(self, value):
        if Account.validate_phone(value):
            self.__phone = value
        else:
            raise ValueError("Неверний формат телефона")
    @staticmethod
    def validate_login(login: str) -> bool:
        if 4 <= len(login) <= 20:
            return bool(re.match(r'^[A-Za-z0-9]+$', login))
        return False

    @staticmethod
    def validate_email(email: str) -> bool:
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_password(password: str) -> bool:
        if len(password) >= 8:
            return bool(re.search(r'[A-Za-z]', password)) and bool(re.search(r'\d', password))
        return False

    @staticmethod
    def validate_phone(phone: str) -> bool:
        return bool(re.match(r'^380\d{9}$', phone))


class Server:
    def __init__(self):
        self.users = []

    def user_count(self) -> int:
        return len(self.users)

    def get_users(self) -> list:
        return [user.login for user in self.users]

    def add_user(self, user: Account):
        for existing_user in self.users:
            if existing_user.login == user.login or existing_user.email == user.email:
                print("такой логин уже ест")
                return
        self.users.append(user)
        print(f"игрок {user.login} добавлен")

    def user_exists(self, login: str = None, email: str = None) -> bool:
        for user in self.users:
            if (login and user.login == login) or (email and user.email == email):
                return True
        return False
    """Task2"""
    class Server:
        def __init__(self):
            self.users = []
        def user_count(self) -> int:
            return len(self.users)
        def get_users(self) -> list:
            return [user.login for user in self.users]
        def add_user(self, user) -> bool:
            if not isinstance(user, Account):
                print("можно добовлять только об*екти класу")
                return False
            for exiting_user in self.users:
                if exiting_user.login == user.login:
                    print(f"такой логин '{user.login}' уже есть")
                    return False
                if exiting_user.email == user.email:
                    print(f"такой '{user.email}' gmail уже есть")
                    return False
            self.users.append(user)
            print(f"вы'{user.login}' добавлени")
            return True
        def user_exists(self, login: str = None, email: str = None) -> bool:
            if login is None and email is None:
                raise ValueError("надо искать емеил или пароль")
            return False

        def get_user_by_login(self, login: str):
            for user in self.users:
                if user.login == login:
                    return user
            return None

        def get_user_by_email(self, email: str):
            for user in self.users:
                if user.email == email:
                    return user
            return None

        def remove_user(self, login: str = None, email: str = None) -> bool:
            if login is None and email is None:
                raise ValueError("надо логин или емеил")

            for i, user in enumerate(self.users):
                if (login is not None and user.login == login) or \
                        (email is not None and user.email == email):
                    removed_user = self.users.pop(i)
                    print(f"он '{removed_user.login}'удален ")
                    return True
            acc1 = Account("user123", "tesd@gmail.com", "password123", "380501234567")
            acc2 = Account("VANA_WSS", "john@gmail.com", "john1234", "3806343345678")
            print("не найден")
            return False