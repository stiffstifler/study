# набор цифр в виде строки "0123456789"
from string import digits
# подтягиваем файл с базой скомпрометированных паролей и разбиваем ее по строкам
with open('pass_base.txt', 'r') as f:
    bad_pass_base = f.read().splitlines()

class User:
    # инициализируем нового пользователя
    def __init__(self, login, password):
        self.login = login
        # тут вызывается свойство_1
        self.password = password
        # конф. информация доступная по паролю
        self.__secret = "secret message"

    # проверка пароля для доступа к конф. информации
    @property
    def secret(self):
        a = input("Введите Ваш пароль: ")
        if a == self.password:
            return self.__secret
        else:
            raise ValueError("Доступ закрыт!")

    # getter
    @property
    def password(self):
        return self.__password

    # проверка на наличие цифер в пароле
    @staticmethod # не принимает self
    def is_include_numder(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    # проверка на наличие пароля в базе скомпрометированных паролей "pass_base.txt"
    @staticmethod # не принимает self
    def check_bad_pass(password):
        for i in bad_pass_base:
            if i == password:
                return False
        return True

    # setter
    @password.setter
    def password(self, value): # свойство_1
        # проверка пароля на соответствие трбованиям
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой.")
        if len(value) < 4 or len(value) > 12:
            raise TypeError("Пароль должен содержать 3 - 12 символов.")
        if not User.is_include_numder(value):
            raise TypeError("Пароль должен содержать хотя бы одну цифру.")
        if not User.check_bad_pass(value):
            raise TypeError("Данный пароль был скомпрометирован.")
        self.__password = value

