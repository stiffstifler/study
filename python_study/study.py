# ООП 20 Магический метод __bool__ Правдивость объектов в Python
# 0 - False, все остальное - True

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # если метода __bool__ нет, будет вызываться метод  __len__
    def __len__(self):
        print("call_len")
        return abs(self.x - self.y)

    # для примера, все точки на оси координат кроме x = 0 и y = 0 - будут возвращать True
    def __bool__(self):
        print("call_bool")
        return self.x != 0 or self.y != 0 # если хоть одна часть будет истиной - вернется True

a = Point(2, 3) #__bool__ вернет True, т.к. ни x ни y ни равны 0
if a: #если "a" = True - вызываем print
    print("hello!")

# обратная ситуация, когда результатом будет False
b = Point(0, 0)
if b:
    print("hello!") # print не вызывается