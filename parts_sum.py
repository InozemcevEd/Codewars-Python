# https://www.codewars.com/kata/5ce399e0047a45001c853c2b/python


def parts_sums(ls):
    output = [0]
    for i in range(len(ls) - 1, -1, -1):
        output.append(output[-1] + ls[i])
    return list(reversed(output))