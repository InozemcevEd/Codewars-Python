# https://www.codewars.com/kata/54d512e62a5e54c96200019e


def primeFactors(n):
    simple = 3
    k = 0
    output = ''
    while n > 1:
        k = 0
        while n % simple == 0:
            n //= simple
            k += 1
        if k == 1:
            output = output + '(' + str(simple) + ')'
        elif k > 1:
            output = output + '(' + str(simple) + '**' + str(k) + ')'
        simple += 2
    return output