class User:
    def __init__(self, nickname, password, age):
        self.nickname = hash(nickname)
        self.password = password
        self.age = age

    def __eq__(self, other):
        if self.nickname == other:
            return True
        else:
            return False


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    users = dict()
    videos = set()
    current_user = None

    def log_in(self, nickname, password):
        user = self.users.get(nickname)
        if user:
            if password == user.password:
                self.current_user = user
                print("Logged in successfully, ", nickname)
            else:
                print("Wrong password!")
        else:
            print('User does not exists')

    def register(self, nickname, password, age):
        if nickname not in self.users:
            us = User(nickname, password, age)
            self.users[nickname] = us
            print("Registration successful", nickname)
            self.log_in(nickname, password)
        else:
            print(f"User {nickname} already exists")

    def log_out(self):
        if self.current_user:
            self.current_user = None
            print("Logged out successfully")
        else:
            print("Not logged in")

    def add(self, *args: Video):
        for video in args:
            self.videos.add(video)

    def get_videos(self, search: str): #несмотря на то, что через dict было бы быстрее и проще, для практики реализую через set
        search = search.lower()
        switch = False
        result = []
        print("Search result: ")
        for video in self.videos:
            if search in video.title.lower():
                result.append(video.title)
                switch = True
        if not switch:
            print("No matches found")
            return
        return result

    def watch_video(self, title):
        current = None
        for video in self.videos:
            if title == video.title:
                current = video
                break
        if not current:
            print("Error. No matches found")
            return
        if not self.current_user:
            print("Sign in to watch video")
            return
        if current.adult_mode and self.current_user.age < 18:
            print("Parent control, please leave this page")
            return
        from time import sleep
        for i in range(current.time_now, current.duration+1):
            print(i)
            sleep(1)
        print("Video ended")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
#ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
ur.log_in('vasya_pupkin', 'F8098FM8fjm9jmi')
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('non-existing vid!')


# noinspection SpellCheckingInspection
"""
Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности.

Задание "Свой YouTube":
Университет Urban подумывает о создании своей платформы, где будут размещаться дополнительные полезные ролики на тему IT (юмористические, интервью и т.д.). Конечно же для старта написания интернет ресурса требуются хотя бы базовые знания программирования.

Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов, которые будут выполнять похожий функционал на сайте.

Всего будет 3 класса: UrTube, Video, User.

Общее ТЗ:
Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео, авторизации и регистрации пользователя и т.д.

Подробное ТЗ:

Каждый объект класса User должен обладать следующими атрибутами и методами:
Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
Каждый объект класса Video должен обладать следующими атрибутами и методами:
Атриубуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
 Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.
Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
Метод log_out для сброса текущего пользователя на None.
Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.

Для метода watch_video так же учитывайте следующие особенности:
1 Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
2 Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
3 Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
4 После воспроизведения нужно выводить: "Конец видео"
"""