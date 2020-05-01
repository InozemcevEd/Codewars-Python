# https://www.codewars.com/kata/5511b2f550906349a70004e1/train/python


# Можно использовать встроенную функцию pow: pow(n1, n2, 10)
def last_digit(n1, n2):
    n1 %= 10
    if n2 == 0:
        return 1
    else:
        res = 1
        while n2 > 1:
            if n2 % 2 == 0:
                n1 = n1 * n1 % 10
                n2 //= 2
            else:
                n2 //= 2
                res = res * n1 % 10
                n1 = n1 * n1 % 10
    return n1 * res % 10