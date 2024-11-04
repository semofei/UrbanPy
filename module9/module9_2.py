first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(word) for word in first_strings if len(word) > 4]
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
third_result = {key: len(key) for key in first_strings and second_strings if len(key) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)

# noinspection SpellCheckingInspection
"""
Цель: закрепить знания о списочных и словарных сборках, решив несколько небольших задач.

Задача:
Даны несколько списков, состоящих из строк
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
В переменную first_result запишите список созданный при помощи сборки состоящий из длин строк списка first_strings, при условии, что длина строк не менее 5 символов.
В переменную second_result запишите список созданный при помощи сборки состоящий из пар слов(кортежей) одинаковой длины. Каждое слово из списка first_strings должно сравниваться с каждым из second_strings. (два цикла)
В переменную third_result запишите словарь созданный при помощи сборки, где парой ключ-значение будет строка-длина строки. Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings. Условие записи пары в словарь - чётная длина строки.
"""