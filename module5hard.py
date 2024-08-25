import time
class User():
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == hash(other.password)

    def __str__(self):
        return self.nickname

class Video():
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = int(duration)
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __str__(self):
        return self.title

class UrTube():
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        user = User(nickname, password, age=0)
        for i in self.users:
            if i == user:
                self.current_user = i
                return
        print("Неверный логин и пароль")

    def register(self, nickname, password, age):
        for i in self.users:
            if i.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.current_user = user

    def add(self, *args):
        for j in args:
            if j not in self.videos:
                self.videos.append(j)

    def get_videos(self, others):
        for video in self.videos:
            if others.lower() in video.title.lower():
                return video.title

    def log_out(self):
        self.current_user = None

    def watch_video(self, name_film):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for film in self.videos:
            if film.title == name_film:
                if film.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                for i in range(film.time_now + 1, film.duration + 1):
                    print(i, end=" ", flush=True)
                    time.sleep(1)
                print("Конец видео")
                film.time_now = 0


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
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
ur.current_user = None
print(ur.current_user)

# # Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
