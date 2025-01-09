def all_variants(text: str):
    i = 1
    while i < len(text):
        for k in range(0, len(text)):
            if len(text) < (i+k):
                continue
            else:
                val = text[k:k+i]
                yield val
        i += 1
        if i == len(text):
            yield text


line = 'abc'
generator = all_variants(line)
for item in generator:
    print(item)


# noinspection SpellCheckingInspection
"""
Цель: более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.

Задача:
Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор, при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

Пункты задачи:
Напишите функцию-генератор all_variants(text).
Опишите логику работы внутри функции all_variants.
Вызовите функцию all_variants и выполните итерации.
Пример результата выполнения программы:
Пример работы функции:
a = all_variants("abc")
for i in a:
print(i)
Вывод на консоль:
a
b
c
ab
bc
abc

Примечания:
Для функции генератора используйте оператор yield."""