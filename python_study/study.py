# ООП 19 Магические методы __eq__ и __hash__. Dunder methods в Python
# НЕХЕШИРУЕМЫЕ - изменяемые объекты, ХЕШИРУЕМЫЕ - неизменяемые.
# __hash__ - возвращает хеш от заданного в функции объекта
# p.s. полезно использовать функцию __hash__ для добавления объектов в качестве ключей словаря.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # проверка равенства 2х объектов !ДЕЛАЕТ РЕЗУЛЬТАТ НЕХЕШИРУЕМЫМ!
    def __eq__(self, other):
        return isinstance(other, Point) \
            and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y)) # считаем хэш от кортежа с self.x, self.y


# dict = {}
# a = Point(3,4)
# dict[a] = 100
# станет dict = {<__main__.Point at 0x1075d01f0>: 100}
