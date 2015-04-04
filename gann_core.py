#!/usr/bin/env python
"""
Core module with key methods
"""
__author__ = 'galarius'

import datetime


def f(x):
    """
    Helper function to determine number on a Gann square at coords: x, 0.
    If x = 0 -> 1
    If x < 0 -> f(-x) - 4 * (-x)
    Else -> f(x-1) + 8 * x - 3
    :param x: x position
    :return: value
    """
    return 1 if x == 0 else (f(-x) - 4 * (-x) if x < 0 else f(x-1) + 8 * x - 3)


def get_number_by_pos(x, y):
    """
    Function to determine number on a Gann square at coordinates: x, y.

    Assuming Gann square coordinates system is:
     ____ ____ ____
    |-1 1|0  1|1  1|
    |-1 0|0  0|1  0|
    |-1-1|0 -1|1 -1|

    (0, 0) = 1

    ToDo: simplify, refactor

    :param x: x position
    :param y: y position
    :return: value
    """
    if x >= 0:                      # x >= 0
        if y <= x:                  # y <= x
            if y >= 0:              # y >= 0
                val = f(x) - y
            else:
                if abs(y) <= x:     # |y| <= x
                    val = f(x) + abs(y)
                else:
                    val = f(abs(y)) + 2 * abs(y) - x
        else:
            val = f(y) - 2 * y + x
    else:
        if y >= 0:                  # y >= 0
            if y <= abs(x):         # y <= |x|
                val = f(x) + y
            else:
                val = f(y) - 2 * y + x
        else:                       # x < 0, y < 0
            if abs(y) < abs(x):     # |y| < |x|
                val = f(x) + y
            elif abs(y) == abs(x):  # |y| == |x|
                val = (abs(y) * 2 + 1) ** 2
            else:
                val = (abs(y) * 2 + 1) ** 2 - (abs(y) - abs(x))
    return val


def get_date_from_pos(x, y, base):
    """
    Function to determine date on a Gann square at coordinates: x, y with base date 'base'

    Assuming Gann square coordinates system is:
     ____ ____ ____
    |-1 1|0  1|1  1|
    |-1 0|0  0|1  0|
    |-1-1|0 -1|1 -1|

    :param x: x position
    :param y: y position
    :param base: base date at position (0, 0)
    :return: date for (x, y)
    """
    days = get_number_by_pos(x, y)
    d = base + datetime.timedelta(days=days-1)  # -1 because origin is 1
    return d