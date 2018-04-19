from math import sin

a = 1.6
b = 2.4


def rectangle(a,const,n,):
    h = (b - a) / float(n)
    sum_r = 0
    for step in range(const, n+const):
        x = a + step * h
        sum_r += f(x)

    return sum_r*h

def trapeze(a,b,n):
    h = (b - a) / float(n)
    return(h*(f(a)+f(b))/2.0+rectangle(a,1,n-1))


def simpson(f, a, b, n):
    h = (b - a) / float(n)
    sum1 = 0

    for i in range(2, n, 2):
        xi = a + h * (i - 1)
        sum1 += f(xi)

    sum1 *= 4
    sum2 = 0

    for i in range(1, n, 2):
        xi = a + h * (i - 1)
        sum2 += f(xi)

    sum2 *= 2
    result = h / 3.0 * (f(a) + f(b) + sum1 + sum2)

    return result


def f(x):
    return (x+1) * sin(x)


print('Формула прямоугольников 1')
for n in 3, 9, 27, 81, 243:
    result = rectangle(a,0,n)
    print('n={0}:   approx={1},   error={2}'.format(n, result, 2.10711 - result))

print('Формула прямоугольников 2')
for n in 3, 9, 27, 81, 243:
    result = rectangle(a,1,n)
    print('n={0}:   approx={1},   error={2}'.format(n, result, 2.10711 - result))



print('Формула трапеций')
for n in 3, 9, 27, 81, 243:
    result = trapeze(a,b,n)
    print('n={0}:   approx={1},   error={2}'.format(n, result, 2.10711 - result))


print('Формула Симпсона')
for n in 3, 9, 27, 81, 243:
    result = simpson(f, a, b, n)
    print('n={0}:   approx={1},   error={2}'.format(n, result, 2.10711 - result))