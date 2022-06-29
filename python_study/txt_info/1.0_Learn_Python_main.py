! ООП !

# УРОК 8
Возможность менять сразу все переменные в классе, вне зависимости от объектов, к которым они присвоены.

################################################################################################################################################

# УРОК 9 Инкапсуляция
	Защищенные и приватные атрибуты и методы в классе
	_name - защещенный атрибут (доступен вне класса, но сигнализирует разработчику, что не должен использоваться вне класса)
	__name - приватный атрибут (доступен только в классе, что бы его вызвать, нужно использовать функцию внутри класса)

################################################################################################################################################

# УРОК 10 Getter, Setter, Property

	# c помощью приставки "__" мы делаем переменную приватной и доступной только внутри класса
	# Функция Getter позволяет вызвать приватную переменную внутри класса и отобразить ее вне класса
	# Функция Setter позволяет переопределить приватную переменную внутри класса
	# Property (свойство) - позволяет вызвать разные функции класса с помощью одой переменной.
	
	class BancAccount:

    # задаем переменные по умолчанию
    def __init__(self, name, ballance):
        # делаем атрибуты приватными с помощью приставки "__", они не будут доступны вне класса BancAccount.
        self.name = name
        self.__ballance = ballance

    # функция внутри класса BancAccount, которая позволит вызывать нужные переменные вне класса BancAccount.
    def getter(self):
        return self.__ballance

    # функция внутри класса BancAccount, которая позволит редактировать параметры переменных.
    def setter(self, value):
        # проверка является ли value числом
        if not isinstance(value, (int, float)):
            # если нет - вызываем ошибку и описание
            raise ValueError("Значение должно быть числом.")
        # если да - присваиваем значение
        self.__ballance = value

    def del_ballance(self):
        del self.__ballance

    # property позволит вызвать различные функции класса с помощью одной переменной ballance
    ballance = property(fget=getter, fset=setter, fdel=del_ballance)


################################################################################################################################################

# УРОК 11 Декоратор Property

 class BancAccount:

    # Инициализируем переменные по умолчанию
    def __init__(self, name, balance):
        # делаем атрибуты приватными с помощью приставки "__", они не будут доступны вне класса BancAccount.
        self.name = name
        self.__balance = balance

    # декоратор - добавляет переменной заданный сценарий поведения.
    @property #аналог: my_balance = property(my_balance)
    # функция внутри класса BancAccount, которая позволит вызывать нужные переменные вне класса BancAccount.
    def my_balance(self):
        return self.__balance

    # сохраняем результат функции getter в переменную my_property_ballance для дальнейшего использования
    # my_property_ballance = getter

    @my_balance.setter # аналог: my_balance = my_property_ballance.setter(my_balance)
    # функция внутри класса BancAccount, которая позволит редактировать параметры переменных.
    def my_balance(self, value):
        # проверка является ли value числом
        if not isinstance(value, (int, float)):
            # если нет - вызываем ошибку и описание
            raise ValueError("Значение должно быть числом.")
        # если да - присваиваем значение
        self.__balance = value

    # @my_balance.deleter # аналог: my_balance = my_property_ballance.deleter(my_balance)
    # def my_balance(self):
    #     del self.__balance
    # КАК ВЫЗВАТЬ DELETER НИХРЕНА НЕ ПОНЯЛ, ЧЕКНУТЬ ОТВЕТ ПОД УРОКОМ ПОЗЖЕ!


################################################################################################################################################


# УРОК 12 Вычисляемые свойства (Calculated properties python)
class Square:

    def __init__(self, s):
        self.__side = s
        self.__area = None
        self.__perimetr = None

    # создаем getter
    @property
    def side(self):
        return self.__side

    # создаем setter + сброс для переменной self.__area = None
    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None
        self.__perimetr = None

    # проверяем проводился ли уже расчет self.__area,
    # если self.__area is None - проводим расчет,
    # если нет - выводим результат прошлого расчета для экономии времени.
    @property
    def area(self):
        if self.__area is None:
            self.__area = self.side ** 2
        return self.__area

    # аналогичный расчет для периметра квадрата
    @property
    def perimetr(self):
        if self.__perimetr is None:
            self.__perimetr = self.__side * 4
        return self.__perimetr


################################################################################################################################################

# ООП 12.1 Практика по методам и свойствам (property)

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
    @staticmethod # делает функцию доступной от самого класса, без параметра self
    def is_include_numder(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    # проверка на наличие пароля в базе скомпрометированных паролей "pass_base.txt"
    @staticmethod # делает функцию доступной от самого класса, без параметра self
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

################################################################################################################################################

# ООП 13 Класса-методы ( сlassmethod ) и статические методы (staticmethod)
class Example:

    # функция доступна только от самого класса
    # Example.hello()
    def hello():
        print("hello")

    # функция доступна только от экземпляра класса
    # self.instance_hello()
    def instance_hello(self):
        print(f"instance_hello {self}")

    #  @staticmethod делает функцию доступной как от самого класса, так и от экземпляра
    #  "Example.static_hello() или self.static_hello()
    @staticmethod
    def static_hello():
        print("static_hello")

    # @classmethod посылает в функцию первым значением имя класса
    # метод нужен когда я хочу сделать обработку над целым классом, а не только екзепляром self
    @classmethod
    def class_hello(cls):
        print(f"class_hello {cls}")


################################################################################################################################################

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

################################################################################################################################################








 ! ДОП МАТЕРИАЛ !



################################################################################################################################################

# УРОК Область видимости. 
	Локальная, глобальная и встроенная области видимости Python

	# глобальная
		a = 1
		def s():
			# встроенная
			a = 2 
				def z():
				# локальная
					a = 3
					# выдаст встроенную переменную а = 2
					nonlocal a
					# выдаст глобальную переменную a = 1
					global a

################################################################################################################################################

# УРОК Передача аргументов Python. Сопоставление аргументов по имени и позиции

1.	* перед переменной - означает, что весь излишек заданных параметров будет присвоен в нее
	a, b, *c = [1, 2, 3, 4]
	a = 1
	b = 2
	c = [3, 4]

2.	*s - распаковывает переменную s как 2 числа
	s = [4,10]
	print(list(range(*s)))

3. 	*a - распакует переменную а по элементам кортежа
	def f(a,b,c,d):
    	print(a,b,c,d)

	a = (1, 2, 3, 4)
	f(*a)

4. *args - неограниченное кол-во неименованных параметров, все значения переданные функции упакуются в виде контежа
	def f(*args):
    	print(args)

	f(1,2,3,4,5)

	# вывод: (1,2,3,4,5)

5. **kwargs - неограниченное кол-во именованных параметров, все значения переданные функции упакуются в виде словаря

	def f(**kwargs):
    	print(kwargs)

	f(a=1,b=2,c=3,d=4,f=5)

	# вывод: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'f': 5}

6. Комбинация *args и **kwargs
	def f(*args,**kwargs):
    	print(args, kwargs)

	f(9,8,7, a=1,b=2,c=3,d=4,f=5)

	# вывод: (9, 8, 7) {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'f': 5}

################################################################################################################################################

# УРОК Замыкание - возвращаем функцию без вызова (без скобок в конце).

	# замыкание без функции вызова разных параметров при вызове переменной
	def main_funk(name):
    	def inner_funk():
        	print("Hello World!", name)
    	return inner_funk

	a = main_funk("name")
	a()


	# замыкание с функцией вызова разных параметров при вызове переменной
	def main_funk():
    	def inner_funk(name):
        	print("Hello World!", name)
    	return inner_funk

	a = main_funk()
	a("name")

	# Результат: Hello World! name

 	# функция 1 нужна для присвоения переменной функции 2 и имени, с которым функция 2 будет использоваться

################################################################################################################################################

# УРОК Декоратор 
	Декоратор добавляет новой переменной заданный сценарий поведения.
	from functools import wraps
	# wraps нужен для сохранения имени __name__  и документации __doc__ при декорировании

	def header(a):
		@wraps(a) # декорируем имя и док.
    	def inner(*args, **kwargs):
        	print("<h1>")
        	a(*args, **kwargs)
        	print("</h1>")

        	# делает тоже самое, что и warps. подменяет параметр __name__ и __doc__
        	# inner.__name__ = a.__name__
        	# inner.__doc__ = a.__doc__
    	return inner

	def table(a):
		@wraps(a) # декорируем имя и док.
	    def inner(*args, **kwargs):
	        print("<table>")
	        a(*args, **kwargs)
	        print("</table>")

	        # делает тоже самое, что и warps. подменяет параметр __name__ и __doc__
        	# inner.__name__ = a.__name__
        	# inner.__doc__ = a.__doc__
	    return inner

	@header # декоратор
	@table # декоратор
	# теперь функция say будет аргументом для функции table и header ( header(table(say)) )
	def say(name, surname, age):
		"bla bla bla" # описание функиции, будет отображено в say.__doc__
    	print("hello world", name, surname, age)
	# say = header(table(say)) - тоже самое
	# теперь say() - вызывает не саму функцию, а сценарий прописанный в переменной say, т.е. header(table(say))

	say("Vasya", "Ivanov", 30)
	# Результат:
	# <h1>
	# <table>
	# hello world Vasya Ivanov 30
	# </table>
	# </h1>

	print(say.__name__)
	# результат: say
	print(say.__doc__)
	# результат: "bla bla bla"

################################################################################################################################################


