import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


f1 = 1  # частота первого сигнала
f2 = 3  # частота второго сигнала
delta = np.pi / 2  # сдвиг фаз

# Создаем массив значений времени
t = np.linspace(0, 2 * np.pi, 500)

# Создаем функцию, которая будет обновлять наш график
def update(frame):
    # Вычисляем новые значения для фигуры Лиссажу
    x = np.sin(f1 * t + delta + np.pi/4)
    y = np.sin(f2 * t)

    # Очищаем предыдущие значения графика
    ax.clear()

    # Создаем график с новыми значениями
    ax.plot(x, y)

    # Добавляем заголовок и метки осей
    ax.set_title("Фигура Лиссажу")


    # Добавляем оси координат
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.grid(True)

# Создаем график и анимацию
fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 100), interval=100)

# Показываем анимацию
plt.show()
