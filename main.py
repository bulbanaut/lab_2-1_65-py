#! /bin/python
import math

a = int(input('Значение k:'))
b = -1
c = int(input('Значение b:'))
r = int(input('Значение r:'))

x0 = -(a*c / (a*a + b*b))
y0 = -(b*c / (a*a + b*b))

if (c*c > r*r*(a*a+b*b) + 0.00000001):
    print('нет точек')
elif (abs(c*c - r*r*(a*a - b*b)) < 0.00000001):
    print('одна точка')
    print(x0, y0)
else:
    d = r*r - c*c/(a*a + b*b)
    mult = math.sqrt(d / (a*a + b*b))
    ax = x0 + b*mult
    bx = x0 - b*mult
    ay = y0 - a*mult
    by = y0 + a*mult
    print('две точки\n', ax, ay, '\n', bx, by)