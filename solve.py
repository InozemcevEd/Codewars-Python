# https://www.codewars.com/kata/55c6126177c9441a570000cc/python

import math


# Считаем сумму ряда: x + 2x^2 + 3x^3 + ... = x/(1-x)^2 = m. Потом выражаем х. Учитываем, что 0 < x < 1
def solve(m):
    return 0.5 * (2 * m + 1 - math.sqrt(4 * m + 1)) / m
