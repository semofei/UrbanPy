first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(word1)-len(word2)) for word1, word2 in zip(first, second) if len(word1) != len(word2))
second_result = (len(first[i]) <= len(second[i]) for i in range(0, len(first)) if len(first) >= len(second))

print(list(first_result))
print(list(second_result))


# noinspection SpellCheckingInspection
"""
Цель: понять механизм создания генераторных сборок и использования встроенных функций-генераторов.
Задача:
Дано 2 списка:
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
Необходимо создать 2 генераторных сборки:
В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк из списков first и second, если их длины не равны. 
Для перебора строк попарно из двух списков используйте функцию zip.
В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения длин строк в одинаковых позициях из списков first и second. 
Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len.
"""