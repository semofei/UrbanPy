def personal_sum(numbers):
    summ = 0
    incorrect_data = 0
    for arg in numbers:
        try:
            summ += arg
        except TypeError:
            incorrect_data += 1
            print("Incorrect data type: %s" % arg)
    return summ, incorrect_data         # "digits sum = %s, incorrect input data: %s"%(summ, incorrect_data)


def calculate_average(numbers):
    try:
        summ, incorrect_data = personal_sum(numbers)
        amount = len(numbers) - incorrect_data
        average = summ / amount
    except ZeroDivisionError:
        average = 0
    except TypeError as exc:
        return 'Incorrect data type: %s' % exc
    return average


dataset_1 = (1, 2, 3, '4', 'f')
dataset_2 = [1, 2, 3, 4, 5]
dataset_3 = tuple()
dataset_4 = None
dataset_5 = '1,2,3,4,5'
print('personal sum tests:')
print(personal_sum(dataset_1))
# print(personal_sum('1,2,3'))
print('calculate_average tests:')
print(calculate_average(dataset_1))


# noinspection SpellCheckingInspection
"""
Напишите 2 функции:
Функция personal_sum(numbers):
Должна принимать коллекцию numbers.
Подсчитывать сумму чисел в numbers путём перебора и увеличивать переменную result.
Если же при переборе встречается данное типа отличного от числового, то обработать исключение TypeError, увеличив счётчик incorrect_data на 1.
В конечном итоге функция возвращает кортеж из двух значений: result - сумма чисел, incorrect_data - кол-во некорректных данных.
Функция calculate_average(numbers)
Среднее арифметическое - сумма всех данных делённая на их количество.
Должна принимать коллекцию numbers и возвращать: среднее арифметическое всех чисел.
Внутри для подсчёта суммы используйте функцию personal_sum написанную ранее.
Т.к. коллекция numbers может оказаться пустой, то обработайте исключение ZeroDivisionError при делении на 0 и верните 0.
Также в numbers может быть записана не коллекция, а другие типы данных, например числа. Обработайте исключение TypeError выводя строку 'В numbers записан некорректный тип данных'. В таком случае функция просто вернёт None.

Пункты задачи:
Создайте функцию personal_sum на основе условий задачи.
Создайте функцию calculate_average на основе условий задачи.
Вызовите функцию calculate_average несколько раз, передав в неё данные разных вариаций.
"""