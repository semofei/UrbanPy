import numpy as np
import matplotlib.pyplot as plt
from atmosphere import get_atm_params_from_alt

# Начальные условия
vel_0 = 250  # начальная скорость, м/с
h_0 = 1000  # начальная высота, м
Theta = np.radians(10)  # Угол тангажа в радианах
Gamma_a = np.radians(5)  # Угол атаки в радианах
Psi = np.radians(2)  # Угол рысканья в радианах
L = 0  # Начальная продольная координата
Z = 0  # Начальная вторая горизонтальная координата

# Константы
G = 9.81  # Ускорение свободного падения (м/с^2)
M = 0.55  # Число Маха
mass = 10000  # Масса аппарата (кг)
dt = 1  # Шаг по времени (с)
S = 30  # Площадь крыла (м²)

# Тяга в зависимости от высоты (число Маха 0.55)
altitudes_M055 = np.arange(0, 12000, 1000)
thrust_values_M055 = np.array([63, 60, 58, 55, 53, 50, 47, 45, 41, 36, 34, 30])


# Функция интерполяции для тяги
def thrust_interp(altitude):
    return np.interp(altitude, altitudes_M055, thrust_values_M055)


# Массивы для хранения результатов
time = np.arange(0, 1001, dt)
L_values = []
H_values = []
Z_values = []

# Начальные параметры
V = vel_0
H = h_0

for t in time:
    # Получение атмосферных параметров
    T, P, rho, a = get_atm_params_from_alt(H)

    # Расчет скорости звука и скорости аппарата
    V = M * a

    # Расчет аэродинамических сил
    Cy = 0.9  # Примерное значение для M=0.55, угол атаки 5 градусов
    Cxa = 0.06  # Примерное значение
    Ya = Cy * S * rho * V ** 2 / 2
    Xa = Cxa * S * rho * V ** 2 / 2

    # Тяга двигателей
    thrust = thrust_interp(H) * 1000  # Перевод в Ньютоны

    # Продольная и вертикальная перегрузки
    N_x = (thrust - Xa) / (mass * G)
    N_ya = (Ya - mass * G) / (mass * G)

    # Обновление параметров движения
    dV = G * (N_x - np.sin(Theta)) * dt
    dTheta = G / V * (N_ya * np.cos(Gamma_a) - np.cos(Theta)) * dt
    dPsi = (G / (V * np.cos(Theta))) * (N_ya * np.sin(Gamma_a)) * dt
    dL = V * np.cos(Theta) * np.cos(Psi) * dt
    dH = V * np.sin(Theta) * dt
    dZ = -V * np.cos(Theta) * np.sin(Psi) * dt

    # Обновление состояния
    V += dV
    # Theta += dTheta
    # Psi += dPsi
    L += dL
    H += dH
    Z += dZ

    # Сохранение значений
    L_values.append(L)
    H_values.append(H)
    Z_values.append(Z)

# Построение графиков
plt.figure(figsize=(12, 6))
plt.plot(time, L_values, label="Продольная координата (L)")
plt.plot(time, H_values, label="Высота (H)")
plt.plot(time, Z_values, label="Горизонтальная координата (Z)")
plt.xlabel("Время, с")
plt.ylabel("Координаты, м")
plt.legend()
plt.title("Траектория полета аппарата")
plt.grid()
plt.show()

# # Построение графика продольной координаты (L)
# plt.figure(figsize=(8, 5))
# plt.plot(time, L_values, label="Продольная координата (L)", color="blue")
# plt.xlabel("Время, с")
# plt.ylabel("Координата L, м")
# plt.title("Продольная координата (L) от времени")
# plt.grid()
# plt.legend()
# plt.show()
#
# # Построение графика высоты (H)
# plt.figure(figsize=(8, 5))
# plt.plot(time, H_values, label="Высота (H)", color="green")
# plt.xlabel("Время, с")
# plt.ylabel("Высота H, м")
# plt.title("Высота (H) от времени")
# plt.grid()
# plt.legend()
# plt.show()
#
# # Построение графика второй горизонтальной координаты (Z)
# plt.figure(figsize=(8, 5))
# plt.plot(time, Z_values, label="Горизонтальная координата (Z)", color="red")
# plt.xlabel("Время, с")
# plt.ylabel("Координата Z, м")
# plt.title("Горизонтальная координата (Z) от времени")
# plt.grid()
# plt.legend()
# plt.show()

