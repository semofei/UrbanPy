def test_function():
    def inner_function():
        print("i'm in test_function's namespace")
    inner_function()


print("what if we call test_func?")
test_function()
print("let's try it out")
inner_function()

# noinspection SpellCheckingInspection
"""
Ваша задача:
Создайте новую функцию test_function
Создайте внутри test_function другую функцию - inner_function, Эта функция должна печатать значение "Я в области видимости функции test_function"
Вызовите функцию inner_function внутри функции test_function
Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
"""