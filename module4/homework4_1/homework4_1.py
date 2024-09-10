import fake_math as fm
from true_math import divide as true_div


first = int(input('Введите целочисленное делимое:'))
second = int(input('Введите целочисленный делитель:'))

print('Результат, если ты школьник:', fm.divide(first, second))
print('Результат, если ты уже вырос:', true_div(first, second))


# noinspection SpellCheckingInspection
"""
Цель: закрепить навык создания и импортирования модулей, а так же функций и переменных находящихся в них.

Задача "А как делить?":
В школе нам говорили, что на 0 делить нельзя. Высшая же математика опровергает это и говорит, что результат при делении на 0 будет стремиться к бесконечности.
Давайте реализуем оба способа, чтобы у вас всегда был выбор!
Создайте модули fake_math и true_math в которых создайте функции отвечающие за деление, но разными способами.
В fake_math создайте функцию divide, которая принимает два параметра first и second. Функция должна возвращать результат деления first на second, но когда в second записан 0 - возвращать строку 'Ошибка'.
В true_math создайте функцию divide, которая принимает два параметра first и second. Функция должна возвращать результат деления first на second, но когда в second записан 0 - возвращать бесконечность.
Бесконечность можно импортировать из встроенной библиотеки math (from math import inf)
"""