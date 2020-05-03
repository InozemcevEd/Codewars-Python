# https://www.codewars.com/kata/55c6126177c9441a570000cc


def order_weight(strng):
    weights = strng.split()
    weights.sort()
    weights = sorted(weights, key = (lambda a: (sum(map(int, a)))))
    s = ''
    for i in weights:
        s += i + ' '
    return s[:len(s) - 1]
