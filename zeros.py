# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34


def zeros(n):
    return int(n / 5) + zeros(int(n / 5)) if n > 0 else 0
