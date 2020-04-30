# https://www.codewars.com/kata/5276c18121e20900c0000235/train/python


def find_missing_number(numbers):
    numbers_length = len(numbers) + 2
    return (numbers_length*numbers_length-numbers_length) / 2 - sum(numbers)
