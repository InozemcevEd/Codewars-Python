# https://www.codewars.com/kata/550f22f4d758534c1100025a/python


def dirReduc(arr):
    d = {"NORTH": 1, "SOUTH": -1, "WEST": 2, "EAST": -2}
    new_arr = []
    for direction in arr:
        if new_arr and d[direction] + d[new_arr[-1]] == 0:
            new_arr.pop()
        else:
            new_arr.append(direction)
    return new_arr
