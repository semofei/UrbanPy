class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

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


# == != < > <= >= + - += -= * /
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
print('equal', h1 == h2)
print('not equal', h1 != h2)
print('lower than', h1 < h2)
print('greater than', h1 > h2)
print('lower equal', h1 <= h2)
print('greater equal', h1 >= h2)
print('sum', h1 + h2)

h1 = h1 - h2
print('substract', h1)

h1 += h2
print('self add', h1)

h1 -= h2
print('self div', h1)

h1 = h1 * h2
print('multiply', h1)

print('Some tests with numbers')
print(h1-10)
print(h2+15)
print(h1/2)
print(h2*2)


# noinspection SpellCheckingInspection
"""
Цель: применить знания о перегрузке арифметических операторов и операторов сравнения.

Задача "Нужно больше этажей":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".

Необходимо дополнить класс House следующими специальными методами:
__eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
__add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
__radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
Остальные методы арифметических операторов, где self - x, other - y:

Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики перед выполняемыми действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
isinstance(other, int) - other указывает на объект типа int.
isinstance(other, House) - other указывает на объект типа House.
"""