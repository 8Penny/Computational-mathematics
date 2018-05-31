import numpy as np
from matplotlib import pyplot as plt

a = 0
b = 10
y0 = 0
h = 0.1

def f(x,y):
    return 1 + 0.2 * y * np.sin(x)


def Eulers_method(y0):
    xi = a
    x_list = []
    y_list = []
    while xi < b:
        x_list.append(xi)
        y_list.append(y0)
        y0 += h * f(xi,y0)

        xi += h
    return x_list, y_list

x, y = Eulers_method(y0)

plt.plot(x, y, '-k')
plt.grid(True)
plt.show()

def Runge_Kuttas2_method(y0):

    xi = a
    x_list = []
    y_list = []
    while xi < b:
        x_list.append(xi)
        y_list.append(y0)
        k1 = f(xi, y0)
        k2 = f(xi + h, y0 + k1 * h)

        y0 += (0.5 * k1 + 0.5 * k2) * h
        xi += h


    return x_list, y_list


x, y = Runge_Kuttas2_method(y0)

plt.plot(x, y, '-k')
plt.grid(True)
plt.show()

def Runge_Kuttas4_method(y0):

    xi = a
    x_list = []
    y_list = []
    while xi < b:
        k1 = h * f(xi, y0)
        k2 = h * f(xi + 0.5 * h, y0 + 0.5 * k1)
        k3 = h * f(xi + 0.5 * h, y0 + 0.5 * k2)
        k4 = h * f(xi + h, y0 + k3)
        x_list.append(xi)
        y_list.append(y0)
        y0 = y0 + (k1 + k2 + k2 + k3 + k3 + k4) / 6

        xi += h


    return x_list, y_list


x, y = Runge_Kuttas4_method(y0)

plt.plot(x, y, '-k')

plt.grid(True)
plt.show()