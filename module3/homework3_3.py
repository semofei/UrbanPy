def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params()
print_params(2, 3)
print_params(87, False,'blahblah')
print_params(b=25)
print_params(c= [1,2,3])

print('Printing from list:')
values_list = [[1,2,'3'], False, 'string12']
print_params(*values_list)
print('Printing from dict')
values_dict = {'a': 453, 'b': False, 'c': 'stoKa'}
print_params(**values_dict)

print('3rd task, values_list2 with 2 params:')
values_list2 = ['str', False]
print_params(*values_list2, 42)


# noinspection SpellCheckingInspection
"""
Цель задания: Освоить создание функций с параметрами по умолчанию и практику вызова этих функций с различным количеством аргументов.

Задача "Распаковка":
1.Функция с параметрами по умолчанию:
Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
Функция должна выводить эти параметры.
Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
2.Распаковка параметров:
Создайте список values_list с тремя элементами разных типов.
Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
3.Распаковка + отдельные параметры:
Создайте список values_list_2 с двумя элементами разных типов
Проверьте, работает ли print_params(*values_list_2, 42)
"""