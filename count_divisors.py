# https://www.codewars.com/kata/58b16300a470d47498000811


import math

def count_divisors(n):
    sum = 0
    h = int(math.sqrt(n))
    for i in range(1, h + 1):
        sum += n // i
    return 2 * sum - h * h