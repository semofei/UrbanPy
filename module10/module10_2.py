import threading
import time


class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(self.name, 'we have been attacked!', sep=', ')
        enemies = 100
        counter = 0
        while True:
            time.sleep(1)
            counter += 1
            enemies -= self.power
            if enemies > 0:
                print(f'{self.name} fighting {counter} days. {enemies} left')
            else:
                print(f'{self.name} won after {counter} days of fighting!')
                break


major = Knight('BATMAN', 30)
corp = Knight('Steve', 7)
major.start()
corp.start()
major.join()
corp.join()
if not (major.is_alive() and corp.is_alive()):
    print('all fights are done')

# noinspection SpellCheckingInspection
"""
Цель: научиться создавать классы наследованные от класса Thread.

Задача "За честь и отвагу!":
Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
Атрибут name - имя рыцаря. (str)
Атрибут power - сила рыцаря. (int)
А также метод run, в котором рыцарь будет сражаться с врагами:
При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
В процессе сражения количество врагов уменьшается на power текущего рыцаря.
По прошествию 1 дня сражения (1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>..., осталось <кол-во воинов> воинов."
После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
Как можно заметить нужно сделать задержку в 1 секунду, инструменты для задержки выберите сами.
Пункты задачи:
Создайте класс Knight с соответствующими описанию свойствами.
Создайте и запустите 2 потока на основе класса Knight.
Выведите на экран строку об окончании битв.
"""