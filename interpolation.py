import numpy as np
n = 34
a=-10
b=10
#b=2*np.pi
x = np.linspace(a, b,n+1)
y = 0.72*x**3+0.054*x
#y = np.sin(x)
print(y)
A = np.zeros((n+1, n+1))
for i in range(n+1):
    for j in range(n+1):
        A[i, j] = x[i]**j

import numpy.linalg as linalg

B = linalg.inv(A)

#print(A.dot(B))

c = B.dot(y)
c = c[::-1]
print(c)

def P(x):
    y=0
    for i in range(n+1):
        y+=c[i]*(x**(n-i))
    return y
print(P(x))

from matplotlib import pyplot as plt

xnew = np.linspace(a,b, 100)
ynew = P(xnew)
yfun = 0.72*xnew**3+0.054*xnew
#yfun = np.sin(xnew)

plt.plot(xnew, ynew, '-k', xnew, yfun, '-r', x, y, '-o')
plt.grid(True)
plt.show()

d = yfun - ynew
plt.plot(xnew, d, '-b')
plt.grid(True)
plt.show()

MSE = np.sqrt(((yfun - ynew)**2).mean())
print(MSE)

#ИНТЕРПОЛЯЦИЯ ЛАГРАНЖА

#n=10
#a=-3
#b=3
#n = 3
#a = 0
#b = 10

x = np.linspace(a, b, n+1)

def f(x):
    return 0.72*x**3+0.054*x
    #return np.exp(-x**2)

y = f(x)

def R(t,i):
    p1 = 1
    p2 = 1

    for j in range(n+1):
        if j!=i:
            p1 *= t-x[j]
            p2 *= x[i] - x[j]
    return p1/p2

def L(t):
    z = 0
    for i in range(n + 1):
        z += y[i]*R(t, i)
    return z

xnew = np.linspace(a, b, 100)
ynew = L(xnew)
yfun = f(xnew)

plt.plot(xnew, ynew, '-k', xnew, yfun, '-r', x, y, '-o')
plt.grid(True)
plt.show()

d = yfun - ynew

plt.plot(xnew, d, '-b')
plt.grid(True)
plt.show()

MSE = np.sqrt(((yfun - ynew)**2).mean())
print(MSE, "средняя квадратичная ошибка интерполяции")