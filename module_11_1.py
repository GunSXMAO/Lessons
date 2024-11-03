"""
1. Библиотека requests
Установка:
pip install requests
Основные возможности:
Отправка HTTP-запросов.
Получение данных с API.
Удобное управление заголовками, параметрами и сессиями.
Пример кода:

import requests

# Запрос данных с сайта
response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()  # Преобразуем ответ в JSON

# Выводим первые 5 записей
for item in data[:5]:
    print(f"Title: {item['title']}\nBody: {item['body']}\n")
Функции:
requests.get(): отправляет GET-запрос к указанному URL.
response.json(): преобразует ответ в JSON.
Поддержка параметров запроса и заголовков.
___________________________________________________________________________________________________________________
2. Библиотека pandas
Установка:
pip install pandas
Основные возможности:
Работа с данными в табличном формате.
Легкое считывание и запись данных из/в CSV и Excel.
Функции для анализа и визуализации данных.
Пример кода:
import pandas as pd

# Считывание данных из CSV файла
df = pd.read_csv('data.csv')  # Замените на действительное имя файла

# Вывод информации о данных
print(df.info())
print(df.describe())  # Статистический анализ

# Фильтрация данных
filtered_data = df[df['column_name'] > 50]  # Замените 'column_name' на имя вашего столбца
print(filtered_data.head())
Функции:
pd.read_csv(): считывает данные из CSV файла в DataFrame.
df.describe(): описывает статистику данных.
Фильтрация и манипуляции с данными с помощью операций над DataFrame.
_____________________________________________________________________________________________________________________
3. Библиотека matplotlib
Установка:
pip install matplotlib
Основные возможности:
Визуализация данных в виде графиков и диаграмм.
Пользовательская настройка графиков.
Поддержка разных форматов вывода.
Пример кода:
import matplotlib.pyplot as plt
import numpy as np

# Генерация данных
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Визуализация данных
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X')
plt.ylabel('Sin(X)')
plt.grid()
plt.savefig('sine_wave.png')  # Сохранение графика в файл
plt.show()
Функции:
plt.plot(): создает график.
plt.title(), plt.xlabel(), plt.ylabel(): добавляют заголовки и подписи осей.
plt.savefig(): сохраняет график в указанный файл.
"""
