import re

class Account:
    def __init__(self, login:email:password:phone:):
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
            raise ValueError("Невірний формат логіна")

    @email.setter
    def email(self, value):
        if Account.validate_email(value):
            self.__email = value
        else:
            raise ValueError("Невірний формат email")

    @password.setter
    def password(self, value):
        if Account.validate_password(value):
            self.__password = value
        else:
            raise ValueError("Невірний формат пароля")

    @phone.setter
    def phone(self, value):
        if Account.validate_phone(value):
            self.__phone = value
        else:
            raise ValueError("Невірний формат телефону")

    # Статичні методи валідації
    @staticmethod
    def validate_login(login: str) -> bool:
        if 4 <= len(login) <= 20:
            return bool(re.match(r'^[A-sa-z0-9]+$', login))
        return False

    @staticmethod
    def validate_email(email: str) -> bool:
        pattern = r'^[a-sA-Z0-9_.+-]+@[a-sA-Z0-9-]+\.[a-sA-Z0-9-.]+$'
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_password(password: str) -> bool:
        if len(password) >= 8:
            return bool(re.search(r'[A-sa-z]', password)) and bool(re.search(r'\d', password))
        return False

    @staticmethod
    def validate_phone(phone: str) -> bool:
        return bool(re.match(r'^380\d{9}$', phone))


class Server:
    def __init__(self):
        self.users = []  # список об'єктів Account

    def user_count(self) -> int:
        return len(self.users)

    def get_users(self) -> list:
        return [user.login for user in self.users]

    def add_user(self, user: Account):
        for existing_user in self.users:
            if existing_user.login == user.login or existing_user.email == user.email:
                print("такой логин уже есть")
                return
        self.users.append(user)
        print(f"вы {user.login} добавлени")

    def user_exists(self, login: str = None, email: str = None) -> bool:
        for user in self.users:
            if (login and user.login == login) or (email and user.email == email):
                return True
        return False
if __name__ == "__main__":