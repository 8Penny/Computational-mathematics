import numpy as np
from matplotlib import pyplot as plt

#МЕТОД ГРУБОЙ СИЛЫ
def brute_force_root_finder(a, b, n):
    x = np.linspace(a, b, n)
    y = f(x)

    roots = []

    for i in range(n - 1):
        if y[i] * y[i + 1] < 0:
            root = x[i] - (x[i + 1] - x[i]) / (y[i + 1] - y[i]) * y[i]
            roots.append(root)

    return np.array(roots)


def f(x):
    y = np.exp(-x) - np.log(x + 1)
    return y

a = 0
b = 2
n = 1001

roots = brute_force_root_finder(a, b, n)
print(roots)

x = np.linspace(a, b, n)
y = f(x)

y0 = f(roots)

plt.plot(x, y, '-k', roots, y0, 'ob')

plt.grid(True)
plt.show()

#МЕТОД НЬЮТОНА

import sys


def newton(f, df, x, eps, max_iterations=100):
    f_value = f(x)
    iteration_counter = 0

    while abs(f_value) > eps and iteration_counter < max_iterations:
        try:
            x = x - float(f_value) / df(x)
        except ZeroDivisionError:
            print('Error! - derivative zero for x = ', x)  # не обращалась в ноль
            sys.exit(1)

        f_value = f(x)
        iteration_counter += 1  # счетчик итерации, что бы не было больше 100

    return x


def df(x):
    y = -np.exp(-x) - 1/(1+x)
    return y


root = newton(f, df, 1.0, 1.0e-6, 100)
print(root)

a = 0
b = 2
n = 1001

x = np.linspace(a, b, n)
y = f(x)

plt.plot(x, y, '-k', root, f(root), 'ob')

plt.grid(True)
plt.show()


#МЕТОД СЕКУЩИХ

def secant(f, x0, x1, eps, max_iterations=100):
    f_x0 = f(x0)
    f_x1 = f(x1)

    iteration_counter = 0

    while abs(f_x1) > eps and iteration_counter < max_iterations:
        try:
            denominator = float(f_x1 - f_x0) / (x1 - x0)
            x = x1 - float(f_x1) / denominator
            #print(float(f_x1 - f_x0), (x1 - x0), float(f_x1) )
        except ZeroDivisionError:
            print('Error! - denominator zero for x = ', x)
            sys.exit(1)

        x0 = x1
        x1 = x

        f_x0 = f_x1
        f_x1 = f(x1)

        iteration_counter += 1

    return x

x0 = 100
x1 = x0 - 1

root = secant(f, x0, x1, eps=1.0e-6)
print(root)

x = np.linspace(-300, 300, 1000)
y = f(x)

plt.plot(x, y, '-k', root, f(root), 'ob')

plt.grid(True)
plt.show()

#МЕТОД БИСЕКЦИИ

def bisection(f, x_L, x_R, eps):
    f_L = f(x_L)

    if f_L * f(x_R) > 0:
        print('Функция на концах интервала одного знака')
        sys.exit(1)

    x_M = float(x_L + x_R) / 2.0
    f_M = f(x_M)

    while abs(f_M) > eps:
        if f_L * f_M > 0:
            x_L = x_M
            f_L = f_M
        else:
            x_R = x_M

        x_M = float(x_L + x_R) / 2
        f_M = f(x_M)

    return x_M

root= bisection(f, 0, 1000, eps=1.0e-6)
print(root)

x = np.linspace(-10, 10, 1000)
y = f(x)

plt.plot(x, y, '-k', root, f(root), 'ob')

plt.grid(True)
plt.show()