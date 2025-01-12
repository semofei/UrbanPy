import threading
from time import sleep, time
from os import remove


def write_words(word_count: int, file_name: str):
    with open(file_name, 'w', encoding="UTF-8") as f:
        for i in range(0, word_count):
            f.write(f'Cobra № {i}\n')
            sleep(0.1)
        print('Finished writing to file ', file_name)


timestamp_start = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
elapsed_time= time() - timestamp_start
print('time for funcs = ', elapsed_time)

timestamp_start2 = time()
thr1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thr2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thr3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thr4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thr1.start()
thr2.start()
thr3.start()
thr4.start()
thr1.join()
thr2.join()
thr3.join()
thr4.join()
elapsed_time2 = time() - timestamp_start2
print('time for funcs = ', elapsed_time2)

# Deleting test files
# remove('example1.txt')
# remove('example2.txt')
# remove('example3.txt')
# remove('example4.txt')
# remove('example5.txt')
# remove('example6.txt')
# remove('example7.txt')
# remove('example8.txt')


# noinspection SpellCheckingInspection
"""
Цель: понять как работают потоки на практике, решив задачу

Задача "Потоковая запись в файлы":
Необходимо создать функцию write_words(word_count, file_name), где word_count - количество записываемых слов, file_name - название файла, куда будут записываться слова.
Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

После создания файла вызовите 4 раза функцию write_words, передав в неё следующие значения:
10, example1.txt
30, example2.txt
200, example3.txt
100, example4.txt
После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
10, example5.txt
30, example6.txt
200, example7.txt
100, example8.txt
Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
Также измерьте время затраченное на выполнение функций и потоков. Как это сделать рассказано в лекции к домашнему заданию.
"""