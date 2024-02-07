import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування


def f(x):
    return np.sin(x)


a = 0  # Нижня межа
b = np.pi  # Верхня межа

# Обчислення точного значення інтеграла за допомогою функції quad
integral_exact, _ = spi.quad(f, a, b)

# Створення графіка
x = np.linspace(a, b, 400)
y = f(x)

# Обчислення інтеграла методом Монте-Карло
n_points = 10000
x_points = np.random.uniform(a, b, n_points)
y_points = np.random.uniform(min(y), max(y), n_points)
points_under_curve = sum(y_points < f(x_points))
area = (b - a) * (max(y) - min(y))
integral_approx = points_under_curve / n_points * area

# Виведення результатів
print("Наближене значення інтеграла методом Монте-Карло:", integral_approx)
print("Точне значення інтеграла, обчислене за допомогою функції quad:", integral_exact)

# Створення графіка
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([min(y) - 0.1, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Графік інтегрування f(x) = sin(x) від {a} до {b}')
ax.text(1.5, 0.5,
        f'Наближене значення інтеграла: {integral_approx:.2f}', fontsize=12, horizontalalignment='center')
ax.text(1.5, 0.4, f'Точне значення інтеграла: {integral_exact:.2f}',
        fontsize=12, horizontalalignment='center')
plt.grid()
plt.show()
