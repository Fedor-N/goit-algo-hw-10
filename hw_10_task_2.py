import numpy as np
import scipy.integrate as spi


def monte_carlo_integration(f, a, b, n_points=10000):
    # Генерація випадкових точок всередині області інтегрування
    x_points = np.random.uniform(a, b, n_points)
    # у нас функція має максимальне значення 1
    y_points = np.random.uniform(0, 1, n_points)

    # Обчислення кількості точок, які попали під криву
    points_under_curve = sum(y_points < f(x_points))

    # Обчислення відношення точок під кривою до загальної кількості точок
    ratio = points_under_curve / n_points

    # Обчислення площі області інтегрування
    area = (b - a) * 1  # площа області, у нашому випадку вона має висоту 1

    # Обчислення наближеного значення інтеграла
    integral_approx = ratio * area

    return integral_approx


def compare_integrals(f, a, b, n_points=10000):
    # Обчислення інтеграла за допомогою методу Монте-Карло
    integral_approx = monte_carlo_integration(f, a, b, n_points)

    # Обчислення інтеграла за допомогою функції quad
    result, _ = spi.quad(f, a, b)

    print("Наближене значення інтеграла методом Монте-Карло:", integral_approx)
    print("Точне значення інтеграла:", result)

# Приклад використання:


def f(x):
    return np.sin(x)


a = 0  # Нижня межа
b = np.pi  # Верхня межа

compare_integrals(f, a, b)
