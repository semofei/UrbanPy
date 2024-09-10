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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
print(len(h1))
print(len(h2))
print(str(h1))
print(str(h2))


# noinspection SpellCheckingInspection
"""
Цель: понять как работают базовые магические методы на практике.

Задача "Магические здания":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".

Необходимо дополнить класс House следующими специальными методами:
__len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
__str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
"""