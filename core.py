__author__ = 'galarius'

import datetime

def f(x):
    if x == 0:
        val = 1
    elif x < 0:
        val = f(-x) - 4 * (-x)
    else:
        val = f(x-1) + 8 * x - 3
    return val


def get_number_by_pos(x, y):
    if x >= 0:
        if y <= x:
            if y >= 0:
                val = f(x) - y
            else:
                if abs(y) <= x:
                    val = f(x) + abs(y)
                else:
                    val = f(abs(y)) + abs(y)*2 - x
        else:
            val = f(y) - 2*y + x
    else:
        if y >= 0:
            if y <= abs(x):
                val = f(x) + y
            else:
                val = f(y) - 2*y + x
        else:
            if abs(y) < abs(x):  # e.g. (-2,-1)
                val = f(x) + y
            elif abs(y) == abs(x):
                val = (abs(y) * 2 + 1) ** 2  # e.g. (-2, -2)
            else:
                val = (abs(y) * 2 + 1) ** 2 - abs(x)
    return val


def get_date_from_pos(x, y, base):
    days = get_number_by_pos(x, y)
    d = base + datetime.timedelta(days=days-1)
    return d