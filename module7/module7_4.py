class Team:
    def __init__(self, name: str, num: int, score: int, time: float):
        self.name = name
        self.num = num
        self.score = score
        self.time = time


def introduction(tm1: Team, tm2: Team) -> None:       # printing results using % operator
    print("В команде %s участников: %s !" % (tm1.name, tm1.num))
    print("Другая команда: %s, в ней участников: %s !" % (tm2.name, tm2.num))
    print("Да сойдутся они в легендарной битве %s на %s!" % (tm1.num, tm2.num))


def results(tm1: Team, tm2: Team) -> None:      # printing results using .format operator
    print("Команда {} решила задач: {}".format(tm1.name, tm1.score))
    print("Их противник, команда {} решила задач: {}".format(tm2.name, tm2.score))
    print("{} решили задачи за {} секунд".format(tm1.name, tm1.time))
    print("{} тоже постарались и решили задачи за {} секунд".format(tm2.name, tm2.time))


def challenge_result(tm1: Team, tm2: Team) -> None:
    print(f"Команды решили {tm1.score} и {tm2.score} задач")
    summ = tm1.score + tm2.score
    avr_time = (tm1.time + tm2.time) / summ

    def define_challenger(team1: Team, team2: Team) -> str:        # defining winner of the challenge
        if team1.score > team2.score or (team1.score == team2.score and team1.time < team2.time):
            return f"победа за командой {team1.name}"
        elif team1.score < team2.score or (team1.score == team2.score and team1.time > team2.time):
            return f"победа за командой {team2.name}"
        else:
            return "НИЧЬЯ!"

    print(f"Результат битвы: {define_challenger(tm1, tm2)}!")
    print(f"Команды в сумме сегодня решили {summ} задач, потратив в стреднем по {avr_time:.3f} на задачу")


code_masters = Team('Мастера кода', 5, 40, 1552.5)
data_wizards = Team('Волшебники Данных', 6, 42, 2153.3)

introduction(code_masters, data_wizards)
results(code_masters, data_wizards)
challenge_result(code_masters, data_wizards)

# noinspection SpellCheckingInspection
"""
Цель задания:

Освоить различные методы форматирования строк в Python.
Научиться применять эти методы в контексте описания соревнования. История: соперничество двух команд - Мастера кода и Волшебники данных.

Задание:
Создайте новый проект или продолжите работу в текущем проекте.
Напишите код, который форматирует строки для следующих сценариев.
Укажите переменные, которые должны быть вставлены в каждую строку:

Использование %:

Переменные: количество участников первой команды (team1_num).
Пример итоговой строки: "В команде Мастера кода участников: 5 ! "

Переменные: количество участников в обеих командах (team1_num, team2_num).
Пример итоговой строки: "Итого сегодня в командах участников: 5 и 6 !"

Использование format():
Переменные: количество задач решённых командой 2 (score_2).
Пример итоговой строки: "Команда Волшебники данных решила задач: 42 !"

Переменные: время за которое команда 2 решила задачи (team1_time).
Пример итоговой строки: " Волшебники данных решили задачи за 18015.2 с !"

Использование f-строк:
Переменные: количество решённых задач по командам: score_1, score_2
Пример итоговой строки: "Команды решили 40 и 42 задач.”

Переменные: исход соревнования (challenge_result).
Пример итоговой строки: "Результат битвы: победа команды Мастера кода!"

Переменные: количество задач (tasks_total) и среднее время решения (time_avg).
Пример итоговой строки: "Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!."

Комментарии к заданию:
В русском языке окончания слов меняются (1 участник, 2 участника), пока что давайте не обращать на это внимания.
Переменные challenge_result, tasks_total, time_avg можно задать вручную или рассчитать. Например, для challenge_result:
"""