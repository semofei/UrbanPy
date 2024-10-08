class IncorrectVinNumber(Exception):
    def __init__(self, msg):
        self.msg = msg


class IncorrectCarNumbers(Exception):
    def __init__(self, msg):
        self.msg = msg


class Car:
    def __init__(self, model: str, vin, plate):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(plate):
            self.__plate = plate

    def __is_valid_vin(self, vin_num):
        if not isinstance(vin_num, int):
            raise IncorrectVinNumber('Incorrect datatype for vin number')
        elif not 1000000 <= vin_num <= 9999999:
            raise IncorrectVinNumber('Incorrect range for vin number')
        else:
            return True

    def __is_valid_numbers(self, plate):
        if not isinstance(plate, str):
            raise IncorrectCarNumbers('Incorrect datatype for licence plate')
        elif len(plate) != 6:
            raise IncorrectCarNumbers('Incorrect licence plate length')
        else:
            return True

    def __repr__(self):
        return 'Ur car is: {}, VIN number is: {}, licence: {}'.format(self.model, self.__vin, self.__plate)


print('positive cases')
car1 = Car('x', 1000000, 'aaa001')
print(car1)
car2 = Car('Niva', 9999999, 'aaa002')
print(car2)
print('Negative cases')
try:
    car3 = Car('1', 100000, 'aaa003')
except IncorrectVinNumber as exc:
    print('BUG SIGN! BUG SIGN! Type: %s' % exc.msg)
try:
    car4 = Car('GT500', 1234567, 'bububaba')
except IncorrectCarNumbers as exc:
    print('Вас остановило ГАИ, причина: {}'.format(exc.msg))


# noinspection SpellCheckingInspection
"""
Задача "Некорректность":

Создайте 3 класса (2 из которых будут исключениями):
Класс Car должен обладать следующими свойствами:
Атрибут объекта model - название автомобиля (строка).
Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность. Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
Атрибут __numbers - номера автомобиля (строка).
Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность. Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
Классы исключений IncorrectVinNumber и IncorrectCarNumbers, объекты которых обладают атрибутом message - сообщение, которое будет выводиться при выбрасывании исключения.

Работа методов __is_valid_vin и __is_valid_numbers:
__is_valid_vin
Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер', если передано не целое число. (тип данных можно проверить функцией isinstance).
Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера', если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
Возвращает True, если исключения не были выброшены.
__is_valid_numbers
Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров', если передана не строка. (тип данных можно проверить функцией isinstance).
Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера', переданная строка должна состоять ровно из 6 символов.
Возвращает True, если исключения не были выброшены.

ВАЖНО!
Методы __is_valid_vin и __is_valid_numbers должны вызываться и при создании объекта (в __init__ при объявлении атрибутов __vin и __numbers).
"""