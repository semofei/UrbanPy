import os
import time

directory = '..'
# for i in os.walk(directory):      # this will show lists of dirs with subdirs and contents
#     print(i)

for root, dirs, files in os.walk(directory):
    print(os.getcwd())
    step_back = os.getcwd()
    for file in files:
        os.chdir(root)
        # print(os.getcwd())
        filepath = os.path.join(root, file)     # backslash with shielding
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        file_size = os.path.getsize(file)
        parent_dir = os.path.dirname(filepath)      # не понимаю зачем использовать это если есть os.getcwd()
        print('file: {}. Path: {}. Size: {} bytes. last modified: {}. Parent dir: {}'.format(
            file, filepath, file_size, formatted_time, parent_dir))
        os.chdir(step_back)
        # print(os.getcwd())

"""2nd option"""
# for i in os.walk(directory):
#     root, dirs, files = i   # always ValueError occurred whether its 3 or 2 values expected FIXED
#     step_back = os.getcwd()
#     for file in files:
#         os.chdir(root)
#         filepath = os.path.join(root, file)
#         filetime = os.path.getmtime(file)
#         formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#         file_size = os.path.getsize(file)
#         parent_dir = os.path.dirname(filepath)
#         print('file: {}. Path: {}. Size: {} bytes. last modified: {}. Parent dir: {}'.format(
#             file, filepath, file_size, formatted_time, parent_dir))
#         os.chdir(step_back)


# noinspection SpellCheckingInspection
"""
Цель задания:

Освоить работу с файловой системой в Python, используя модуль os.
Научиться применять методы os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize и использование модуля time для корректного отображения времени.

Задание:

Создайте новый проект или продолжите работу в текущем проекте.
Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
Примените os.path.join для формирования полного пути к файлам.
Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
Используйте os.path.getsize для получения размера файла.
Используйте os.path.dirname для получения родительской директории файла.

Комментарии к заданию:

Ключевая идея – использование вложенного for

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = ?
    filetime = ?
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = ?
    parent_dir = ?
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')



Так как в разных операционных системах разная схема расположения папок, тестировать проще всего в папке проекта (directory = “.”)
Пример возможного вывода:
Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт, Время изменения: 11.11.1111 11:11, Родительская директория.
"""