# ООП 14 Пространство имен класса Class Body scope in Python

# глобальные переменные
python_dev = 1
go_dev = 1
react_dev = 1

class DepartmentIT:
    # встроенные переменные
    python_dev = 3
    go_dev = 3
    react_dev = 2

    # у метода info нет доступа к встроенным переменным, только к глобальным и локальным
    def info(self):
        # локальные переменные
        python_dev = 2
        go_dev = 2
        react_dev = 2
        # обратится к локальным переменным, если их не будет - к глобальным
        print("Было: " + python_dev, go_dev, react_dev)

    # Обращаемся к встроенным переменным разными способами
    def info(self): # через self
        print(self.python_dev, self.go_dev, self.react_dev)

    def info2(self): # через ИМЯ КЛАССА
        print(DepartmentIT.python_dev, DepartmentIT.go_dev, DepartmentIT.react_dev)

    @property
    def info3(self): # через self и декоратор @property
        print(self.python_dev, self.go_dev, self.react_dev)

    @classmethod
    def info4(cls):  # через cls и декоратор @classmethod
        print(cls.python_dev, cls.go_dev, cls.react_dev)

    @staticmethod
    def info5():  # через ИМЯ КЛАССА и декоратор @staticmethod
        print(DepartmentIT.python_dev, DepartmentIT.go_dev, DepartmentIT.react_dev)


    def new_dev(self):
        # self.python_dev - добавит и сохранит значение в ЭКЗЕМПЛЯРЕ КЛАССА
        self.python_dev += 1
        # DepartmentIT.python_dev - добавит и сохранит значение в ЭКЗЕМПЛЯРЕ КЛАССА
        DepartmentIT.python_dev += 1
