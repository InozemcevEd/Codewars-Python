# https://www.codewars.com/kata/556deca17c58da83c00002db/train/python


def tribonacci(signature, n):
    for i in range(3, n):
        signature.append(sum(signature[i - 3:i]))
    return signature[0:n]
