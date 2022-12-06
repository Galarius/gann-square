#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Ilya Shoshin'
__copyright__ = 'Copyright 2015, Ilya Shoshin'

from gann.core import *


def run_tests():
    print(get_number_by_pos(0, 0), get_number_by_pos(0, 0) == 1)
    print(get_number_by_pos(0,1), get_number_by_pos(0,1) == 4)
    print(get_number_by_pos(1,2), get_number_by_pos(1,2) == 16)
    print(get_number_by_pos(2,3), get_number_by_pos(2,3) == 36)
    print(get_number_by_pos(3,3), get_number_by_pos(3,3) == 37)
    print(get_number_by_pos(4,1), get_number_by_pos(4,1) == 68)
    print(get_number_by_pos(5,3), get_number_by_pos(5,3) == 103)
    print(get_number_by_pos(6,1), get_number_by_pos(6,1) == 150)
    print("-----")
    print(get_number_by_pos(1,3), get_number_by_pos(1,3) == 35)
    print(get_number_by_pos(1,7), get_number_by_pos(1,7) == 191)
    print(get_number_by_pos(7,1), get_number_by_pos(7,1) == 203)
    print("-----")
    print(f(-1), f(-1) == 2)
    print(f(-7), f(-7) == 176)
    print("-----")
    print(get_number_by_pos(-1,3), get_number_by_pos(-1,3) == 33)
    print(get_number_by_pos(-7,1), get_number_by_pos(-7,1) == 177)
    print(get_number_by_pos(-7,4), get_number_by_pos(-7,4) == 180)
    print(get_number_by_pos(-7,7), get_number_by_pos(-7,7) == 183)
    print(get_number_by_pos(-7,8), get_number_by_pos(-7,8) == 242)
    print("-----")
    print(get_number_by_pos(2, -2), get_number_by_pos(2, -2) == 21)
    print(get_number_by_pos(2, -1), get_number_by_pos(2, -1) == 20)
    print(get_number_by_pos(4, -4), get_number_by_pos(4, -4) == 73)
    print(get_number_by_pos(3, -4), get_number_by_pos(3, -4) == 74)
    print(get_number_by_pos(0, -3), get_number_by_pos(0, -3) == 46)
    print(get_number_by_pos(1, -3), get_number_by_pos(1, -3) == 45)
    print(get_number_by_pos(2, -5), get_number_by_pos(2, -5) == 114)
    print(get_number_by_pos(2, -4), get_number_by_pos(2, -4) == 75)
    print(get_number_by_pos(0, -7), get_number_by_pos(0, -7) == 218)
    print("-----")
    print(get_number_by_pos(-2, -4), get_number_by_pos(-2, -4) == 79)
    print(get_number_by_pos(-2, -1), get_number_by_pos(-2, -1) == 10)
    print(get_number_by_pos(-2, -2), get_number_by_pos(-2, -2) == 25)
    print(get_number_by_pos(-7, -2), get_number_by_pos(-7, -2) == 174)
    print(get_number_by_pos(-5, -9), get_number_by_pos(-5, -9) == 357)
    print("-----")

run_tests()
