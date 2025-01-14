import threading
from queue import Queue
from time import sleep
from random import randint


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name: str):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        wait = randint(3, 10)
        sleep(wait)
        print(f'Guest {self.name} eat for {wait} sec.')


class Cafe:
    def __init__(self, *tables: Table):
        self.queue = Queue()
        self.tables = tuple(tables)
        self.free_tables = len(self.tables)

    def guest_arrival(self, *guests: Guest):
        for guest in guests:
            # this check will make this process faster if many guests arrived
            if self.free_tables:
                for table in self.tables:
                    if not table.guest:
                        table.guest = guest
                        print(f'{guest.name} got at the table {table.number}')
                        self.free_tables -= 1
                        guest.start()
                        break
            else:
                print(f'{guest.name} got in queue')
                self.queue.put(guest)

    def discuss_guests(self):
        while True:
            if not self.queue.empty() or self.free_tables != len(self.tables):       # base condition
                for table in self.tables:
                    if table.guest and not table.guest.is_alive():
                        print(f'{table.guest.name} finished dinner and gone\n{table.number} is free')
                        table.guest = None
                        self.free_tables += 1
                    elif not self.queue.empty() and not table.guest:
                        table.guest = self.queue.get()
                        print(f'{table.guest.name} from queue sat at the table {table.number}')
                        table.guest.start()
                        self.free_tables -= 1
            else:
                break


# Создание столов
tables1 = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
# Создание гостей
guests1 = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables1)
# Приём гостей
cafe.guest_arrival(*guests1)
# Обслуживание гостей
cafe.discuss_guests()


# noinspection SpellCheckingInspection
"""
Цель: Применить очереди в работе с потоками, используя класс Queue.

Задача "Потоки гостей в кафе":
Необходимо имитировать ситуацию с посещением гостями кафе.
Создайте 3 класса: Table, Guest и Cafe.
Класс Table:
Объекты этого класса должны создаваться следующим способом - Table(1)
Обладать атрибутами number - номер стола и guest - гость, который сидит за этим столом (по умолчанию None)
Класс Guest:
Должен наследоваться от класса Thread (быть потоком).
Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
Обладать атрибутом name - имя гостя.
Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд.
Класс Cafe:
Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).
Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).
Метод guest_arrival(self, *guests):
Должен принимать неограниченное кол-во гостей (объектов класса Guest).
Далее, если есть свободный стол, то сажать гостя за стол (назначать столу guest), запускать поток гостя и выводить на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue и выводить сообщение "<имя гостя> в очереди".
Метод discuss_guests(self):
Этот метод имитирует процесс обслуживания гостей.
Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive), то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола> свободен". Так же текущий стол освобождается (table.guest = None).
Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), то текущему столу присваивается гость взятый из очереди (queue.get()). Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
Далее запустить поток этого гостя (start)
Таким образом мы получаем 3 класса на основе которых имитируется работа кафе:
Table - стол, хранит информацию о находящемся за ним гостем (Guest).
Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей (guest_arrival) и их обслуживания (discuss_guests).
"""