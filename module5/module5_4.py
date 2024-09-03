class House:

    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')
        return

    def go_to(self, new_floor: int):
        if new_floor > self.number_of_floors or new_floor <= 0:
            print("Такого этажа не сужествует")
        else:
            elevator = []
            for i in range(1, new_floor+1):
                elevator.append(i)
            print(*elevator)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        return (isinstance(other, House)
                and self.name == other.name
                and self.number_of_floors == other.number_of_floors)

    def __ne__(self, other):
        return not (self == other)

    def gnum(self):
        if isinstance(self, House):
            return self.number_of_floors
        elif isinstance(self, int):
            return self
        else:
            raise Exception("Incorrect type")

    def __lt__(self, other):
        return self.number_of_floors < House.gnum(other)

    def __gt__(self, other):
        return self.number_of_floors > House.gnum(other)

    def __le__(self, other):
        return self.number_of_floors <= House.gnum(other)

    def __ge__(self, other):
        return self.number_of_floors >= House.gnum(other)

    def __add__(self, other):
        self.number_of_floors += House.gnum(other)
        return self

    def __sub__(self, other):
        self.number_of_floors -= House.gnum(other)
        return self

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.value = self + House.gnum(other)
        return self

    def __mul__(self, other):
        self.number_of_floors = self.number_of_floors * House.gnum(other)
        return self

    def __truediv__(self, other):
        self.number_of_floors = self.number_of_floors // House.gnum(other)
        return self


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)


# noinspection SpellCheckingInspection
"""
Задача "История строительства":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".

В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.

Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
Дополните метод __new__ так, чтобы:
Название объекта добавлялось в список cls.houses_history.
Название строения можно взять из args по индексу.

Также переопределите метод __del__(self) в котором будет выводиться строка:
"<название> снесён, но он останется в истории"

Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history."""