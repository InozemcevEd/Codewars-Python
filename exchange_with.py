# https://www.codewars.com/kata/55de9c184bb732a87f000055


def reverse(seq):
    for i in range((len(seq) - 1) // 2):
        reverse_i = len(seq) - 1 - i
        seq[i], seq[reverse_i] = seq[reverse_i], seq[i]

    return seq
