# -*- coding: utf-8 -*-

import math as m

# Programm_A


a = 1

first = (1 + a + a ** 2) / (2 * a + a ** 2) + 2
second = (1 - a + a ** 2) / (2 * a - a ** 2)
third = (1 / (first - second)) * (5 - 2 * a ** 2)

print('Результат вычисления первого выражения: ', third)

# Programm_B

a = m.radians(1)
b = m.radians(1)
y = m.radians(1)

first = 1/4 * (m.sin(a + b - y) + m.sin(b + y - a) + \
        m.sin(y + a - b) - m.sin(a + b + y))

result = m.degrees(first)
second = m.sin(m.radians(1))

print('Результат вычисления второго выражения: ', result, second)
