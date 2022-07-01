# ООП 17 Магические методы __add__ (сложение), __mul__(умножение), __sub__(вычетание) и __truediv__(деление)
# По примеру ниже можно использовать любой из методов.

class BankAccount:
    # инициализируем клиента
    def __init__(self, name, balance):
        print("new object init")
        self.name = name
        self.balance = balance

    # a = BankAccount("ivan", 500)
    # при сложении баланса
    # a.balance - выдаст "500", a.balance + 500 - выдаст "1000"
    # при попытке сложения объекта с чем либо "a + 5" - выдаст ошибку

    # создаем возможность добавлять что либо к объекту
    def __add__(self, other):
        print("__add__ called")
        # сложение с сторонним числом "b + 12"
        if isinstance(other, (float, int)):
            # return self.balance + other - добавит заданное значение без сохраннеия
            return BankAccount(self.name, self.balance + other) # сохранит результат в новую переменную или обновит старую
        # b = BankAccount("misha", 78)
        # b + 12 - выдаст "90"

        # сложение с другим аккаунтом
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        # b = BankAccount("misha", 78)
        # c = BankAccount("Vasya", 333)
        # выведет "411"

        # сложение строки
        if isinstance(other, str):
            return self.name + other

        # d = BankAccount("Bob", 555)
        # d + " lol" - выдаст 'Bob lol'

        # ошибка, в случае невыполнения ни одного из вариантов
        raise NotImplemented

    # __radd__ - позволяет складывать объект с числом стоящим спереди "12 + b"
    def __radd__(self, other):
        print("__radd__ called")
        if isinstance(other, (float, int)):
            return self + other



    # задаем отображение объекта внутри системы
    def __repr__(self):
        return f"Клиент {self.name}, с балансом {self.balance}"
    # e = BankAccount("Ivan", 555)
    # При вызове "e" выдаст - "Клиент Ivan, с балансом 555"




