from time import time
import multiprocessing


def read_info(name: str) -> None:
    all_data = list()
    try:
        with open(name, 'r') as r:
            for line in r:
                line = line.removesuffix('\n')
                if line:
                    all_data.append(line)
    except FileNotFoundError as e:
        print('Extract Files.7z', e)
        return


filenames = [f'file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    start = time()
    for file in filenames:
        read_info(file)
    print('linear processing lasts:', time() - start)

    start = time()
    with multiprocessing.Pool() as p:
        p.map(read_info, filenames)
    print('multiprocessing lasts:', time() - start)


# noinspection SpellCheckingInspection
"""
Цель: понять разницу между линейным и многопроцессным подходом, выполнив операции обоими способами.

Задача "Многопроцессное считывание":
Необходимо считать информацию из нескольких файлов одновременно, используя многопроцессный подход.
Подготовка:
Скачайте архив с файлами для считывания данных и распакуйте его в проект для дальнейшего использования.
Выполнение:
Создайте функцию read_info(name), где name - название файла. Функция должна:
Создавать локальный список all_data.
Открывать файл name для чтения.
Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
Во время считывания добавлять каждую строку в список all_data.
Этих операций достаточно, чтобы рассмотреть преимущество многопроцессного выполнения программы над линейным.
Создайте список названий файлов в соответствии с названиями файлов архива.
Вызовите функцию read_info для каждого файла по очереди (линейно) и измерьте время выполнения и выведите его в консоль.
Вызовите функцию read_info для каждого файла, используя многопроцессный подход: контекстный менеджер with и объект Pool. Для вызова функции используйте метод map, передав в него функцию read_info и список названий файлов. Измерьте время выполнения и выведите его в консоль.
Для избежания некорректного вывода запускайте линейный вызов и многопроцессный по отдельности, предварительно закомментировав другой.
"""