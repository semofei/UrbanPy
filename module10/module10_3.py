import threading
import random
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(0, 100):
            amount = random.randint(50, 500)
            self.balance += amount
            if self.lock.locked() and self.balance > 500:
                self.lock.release()
            print('Top up: %s. Balance: %s.' % (amount, self.balance))
            sleep(0.001)

    def take(self):
        for k in range(0, 100):
            query = random.randint(50, 500)
            print('Request for %s' % query)
            if query <= self.balance:
                self.balance -= query
                print('Purchase: %s. Balance: %s' % (query, self.balance))
            else:
                print('Purchase declined. Not enough funds')
                self.lock.acquire()
            sleep(0.001)


mmm = Bank()
thread1 = threading.Thread(target=Bank.deposit, args=(mmm,))
thread2 = threading.Thread(target=Bank.take, args=(mmm,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print('\nFinal balance:', mmm.balance)


# noinspection SpellCheckingInspection
"""
Цель: освоить блокировки потоков, используя объекты класса Lock и его методы.

Задача "Банковские операции":
Необходимо создать класс Bank со следующими свойствами:

Атрибуты объекта:
balance - баланс банка (int)
lock - объект класса Lock для блокировки потоков.

Методы объекта:
Метод deposit:
Будет совершать 100 транзакций пополнения средств.
Пополнение - это увеличение баланса на случайное целое число от 50 до 500.
Если баланс больше или равен 500 и замок lock заблокирован - lock.locked(), то разблокировать его методом release.
После увеличения баланса должна выводится строка "Пополнение: <случайное число>. Баланс: <текущий баланс>".
Также после всех операций поставьте ожидание в 0.001 секунды, тем самым имитируя скорость выполнения пополнения.
Метод take:
Будет совершать 100 транзакций снятия.
Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
В начале должно выводится сообщение "Запрос на <случайное число>".
Далее производится проверка: если случайное число меньше или равно текущему балансу, то произвести снятие, уменьшив balance на соответствующее число и вывести на экран "Снятие: <случайное число>. Баланс: <текущий баланс>".
Если случайное число оказалось больше баланса, то вывести строку "Запрос отклонён, недостаточно средств" и заблокировать поток методом acquire.
Далее создайте объект класса Bank и создайте 2 потока для его методов deposit и take. Запустите эти потоки.
После конца работы потоков выведите строку: "Итоговый баланс: <баланс объекта Bank>".

По итогу вы получите скрипт разблокирующий поток до баланса равному 500 и больше или блокирующий, когда происходит попытка снятия при недостаточном балансе.
"""