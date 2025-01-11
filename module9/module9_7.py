def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result == 1 or result == 2 or result == 3:
            print('prime')
        else:
            # switch = True
            for i in range(2, result):
                if result % i == 0:
                    print('not prime')
                    return result
            print('prime')
        return result
    return wrapper


@is_prime
def sum_three(*args: int) -> int:
    if len(args) != 3:
        raise ValueError('must be only 3 arguments')
    summary = 0
    for num in args:
        summary += num
    return summary


print(sum_three(3, 9, 7))
print(sum_three(6, 6, 6))
print(sum_three(1,1,1))

# noinspection SpellCheckingInspection
"""Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three).
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.
Пример:
result = sum_three(2, 3, 6)
print(result)

Результат консоли:
Простое
11

Примечания:
Не забудьте написать внутреннюю функцию wrapper в is_prime
Функция is_prime должна возвращать wrapper
@is_prime - декоратор для функции sum_three
"""