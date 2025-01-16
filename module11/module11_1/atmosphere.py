import math

# Константы
g0 = 9.80665  # Ускорение свободного падения, м/с^2
R = 287.05  # Газовая постоянная для сухого воздуха, Дж/(кг*K)
T0 = 288.15  # Температура на уровне моря, К
P0 = 101325.0  # Давление на уровне моря, Па
rho0 = 1.225  # Плотность на уровне моря, кг/м^3
L1 = -0.0065  # Температурный градиент (тропосфера), K/м
H1 = 11000.0  # Высота тропопаузы, м
T1 = 216.65  # Температура в тропопаузе, К
gamma = 1.4  # Показатель адиабаты


def get_atm_params_from_alt(altitude: float) -> tuple[float, float, float, float]:
    """ func(height in meters) -> tuple(temperature, pressure, density, speed_of_sound) """

    if altitude <= 0:
        raise ValueError(f"Incorrect altitude: {altitude}")  # Если высота меньше или равна 0

    if altitude <= H1:  # Если высота в тропосфере
        # Расчет температуры в тропосфере
        temperature = T0 + L1 * altitude
        # Расчет давления в тропосфере
        pressure = P0 * (temperature / T0) ** (-g0 / (R * L1))
        # Расчет плотности в тропосфере
        density = pressure / (R * temperature)

    else:  # Если высота в стратосфере (изотермическая)
        # Температура в тропопаузе
        temperature = T1
        # Расчет давления в стратосфере
        pressure = P0 * (T1 / T0) ** (-g0 / (R * L1)) * math.exp(-g0 * (altitude - H1) / (R * T1))
        # Расчет плотности в стратосфере
        density = pressure / (R * temperature)

    # Расчет скорости звука
    speed_of_sound = math.sqrt(gamma * R * temperature)

    return temperature, pressure, density, speed_of_sound
