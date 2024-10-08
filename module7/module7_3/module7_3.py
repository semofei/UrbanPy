class WordsFinder:
    def __init__(self, *names):
        self.file_names = names

    def get_all_words(self):
        all_words = dict()
        for name in self.file_names:
            with open(name, 'r', encoding='UTF-8') as record:
                line = record.read()
                line = line.lower()
                for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:     # replacing punctuation marks
                    line = line.replace(char, '')
                list_line = line.split()        # splitting into separate words
            all_words[name] = list_line
        return all_words

    def find(self, word):
        word = word.lower()
        found = dict()
        for name, listed in self.get_all_words().items():       # get filename and list of words
            i = 1
            for item in listed:         # search for exact word
                if item == word:
                    found[name] = i
                    break
                else:
                    i += 1
            if found.__len__() == 0:     # if there are no search words we return None as key
                found[name] = None
        return found

    def count(self, word):
        word = word.lower()
        count = dict()
        for name, listed in self.get_all_words().items():
            i = 0
            for item in listed:
                if item == word:
                    i += 1
            count[name] = i     # no search words = 0
        return count


finder = WordsFinder('test_file.txt')
print(finder.get_all_words())
print(finder.find('TEXT'))
print(finder.count('teXT'))

finder2 = WordsFinder('Mother Goose - Monday’s Child.txt')
print(finder2.get_all_words())
print(finder2.find('grAcE'))
print(finder2.count('chILD'))

# noinspection SpellCheckingInspection
"""
Задача "Найдёт везде":
Напишите класс WordsFinder, объекты которого создаются следующим образом:
WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут file_names в виде списка или кортежа.

Также объект класса WordsFinder должен обладать следующими методами:
get_all_words - подготовительный метод, который возвращает словарь следующего вида:
{'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
Где:
'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
Алгоритм получения словаря такого вида в методе get_all_words:
Создайте пустой словарь all_words.
Переберите названия файлов и открывайте каждый из них, используя оператор with.
Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами, это не дефис в слове).
Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.

find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item().

for name, words in get_all_words().items():
  # Логика методов find или count"""