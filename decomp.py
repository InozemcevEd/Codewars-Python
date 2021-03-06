# https://www.codewars.com/kata/5a045fee46d843effa000070


import math


def is_simple(num):
    if num == 2:
        return True
    else:
        i = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
        return True


def decomp(n):
    output = ''
    number = math.factorial(n)
    digit = 2
    while number > 1:
        if is_simple(digit):
            k = 0
            while number % digit == 0:
                number //= digit
                k += 1
            if k == 1:
                output = output + str(digit) + ' * '
            else:
                output = output + str(digit) + '^' + str(k) + ' * '
        digit += 1
    output = output[:len(output) - 3]
    return output
