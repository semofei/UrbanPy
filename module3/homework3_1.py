calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string: str):
    count_calls()
    tuple_ = ()
    tuple_ += (len(string),)
    tuple_ += (string.upper(),)
    tuple_ += (string.lower(),)
    return tuple_


def is_contains(string: str, list_to_search: list):
    count_calls()
    string = string.lower()

    for i in range(0, len(list_to_search)):
        list_to_search[i].lower

    if string in list_to_search:
        return True
    else:
        return False


temp_string = input('Enter 1st string: ')
print('Modifying 1st string: ', string_info(temp_string))
temp_string = input('Enter 2nd string: ')
print('Modifying 2nd string: ', string_info(temp_string))

print('Calling is_contains func 1st time: ', is_contains('ban', ['ban', 'toDo', 'toSearch']))
print('Calling is_contains func 2nd time: ', is_contains('bOOk', ['brake', 'rocket', 'CHIP']))
print('Number of func calls: ', calls)

# noinspection SpellCheckingInspection
'''
Задача "Счётчик вызовов":
    Порой необходимо отслеживать, сколько раз вызывалась та или иная функция. 
    К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.
    Давайте реализуем данную фишку самостоятельно!

Вам необходимо написать 3 функции:
    1 Функция count_calls подсчитывающая вызовы остальных функций.
    2 Функция string_info принимает аргумент - строку и возвращает кортеж из: 
длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
    3 Функция is_contains принимает два аргумента: 
строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. 
Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

Пункты задачи:
    1 Создать переменную calls = 0 вне функций.
    2 Создать функцию count_calls и изменять в ней значение переменной calls. 
Эта функция должна вызываться в остальных двух функциях.
    3 Создать функцию string_info с параметром string и реализовать логику работы по описанию.
    4 Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
    5 Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
    6 Вывести значение переменной calls на экран(в консоль).
'''
