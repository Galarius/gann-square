#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool to build Gann square.
"""

__author__ = 'Ilya Shoshin'
__copyright__ = 'Copyright 2015, Ilya Shoshin'

import sys, getopt
import math
import gann_core as gc
from gann_svg_builder import Builder
from datetime import datetime


def build_grid(stream, builder, size, step):
    """
    draw grid
    :param stream:  stream to write to
    :param builder: builder instance
    :param size:    the size of grid
    :param step:    cell width
    """
    stream.write(builder.header)
    for i in range(0, size, step):
        stream.write(builder.build_line_x(i))
        stream.write(builder.build_line_y(i))


def create_gann_square_classic(square_size, cell_size, stream):
    # setup
    size = square_size * cell_size + 1
    builder = Builder(square_size, cell_size)
    # header
    stream.write(builder.header)
    # draw grid
    build_grid(stream, builder, size, cell_size)
    # fill the grid
    square_size_2 = int(math.ceil(square_size / 2.0))
    origin_y, offset_x = size - cell_size - 1, 0
    for x in range(-square_size_2+1, square_size_2):
        offset_y = origin_y
        for y in range(-square_size_2+1, square_size_2):
            val = gc.get_number_by_pos(x, y)
            if x == y or -x == y:
                stream.write(builder.build_mark(offset_x, offset_y, Builder.none, Builder.blue_color, 1.5))
            if x == 0 or y == 0:
                stream.write(builder.build_mark(offset_x, offset_y, Builder.yellow_color, Builder.yellow_color))
            stream.write(builder.build_text(offset_x+2, offset_y + cell_size * 0.5, str(val)))
            offset_y -= cell_size
        offset_x += cell_size


def create_gann_square_dates(square_size, cell_size, base, marks, stream):
    # setup
    size = square_size * cell_size + 1
    builder = Builder(square_size, cell_size)
    # header
    stream.write(builder.header)
    # draw grid
    build_grid(stream, builder, size, cell_size)
    # fill the grid
    square_size_2 = int(math.ceil(square_size / 2.0))
    origin_y, offset_x = size - cell_size - 1, 0
    for x in range(-square_size_2+1, square_size_2):
        offset_y = origin_y
        for y in range(-square_size_2+1, square_size_2):
            val = gc.get_date_from_pos(x, y, base)
            if x == y or -x == y:
                stream.write(builder.build_mark(offset_x, offset_y, Builder.none, Builder.blue_color, 1.5))
            if x == 0 or y == 0:
                stream.write(builder.build_mark(offset_x, offset_y, Builder.yellow_color, Builder.yellow_color))
            if val.strftime("%d/%m/%Y\n") in marks:
                stream.write(builder.build_mark(offset_x, offset_y, Builder.red_color, Builder.red_color))
            stream.write(builder.build_text(offset_x+2, offset_y + cell_size * 0.5, val.strftime("%d/%m")))
            stream.write(builder.build_text(offset_x+2, offset_y + cell_size - 2, val.strftime("%Y")))
            offset_y -= cell_size
        offset_x += cell_size


def print_usage():
    print """
          classic Gann square: gann.py -o <output file name> -s <square size>
          date based Gann square: gann.py -o <output file name> -a <base date> -b <final date> -m <path to list of dates to mark>

          input date format: "dd/MM/yyyy"
          """


def main(argv):

    cell_size = 30
    date_format = "%d/%m/%Y"
    # --------------------------------------
    output_file_name = ''
    marks_file_name = ''
    square_size = -1
    date_a = None
    date_b = None
    # --------------------------------------
    try:
        opts, args = getopt.getopt(argv, "ho:s:a:b:m:", ["ofile=", "size=", "a_date=", "b_date=", "mfile="])
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit()
        elif opt in ("-o", "--ofile"):
            output_file_name = arg
        elif opt in ("-s", "--size"):
            square_size = int(arg)
        elif opt in ("-a", "--a_date"):
            date_a = datetime.strptime(arg, date_format)
        elif opt in ("-b", "--b_date"):
            date_b = datetime.strptime(arg, date_format)
        elif opt in ("-m", "--mfile"):
            marks_file_name = arg

    if output_file_name == '':
        print_usage()
        sys.exit(2)

    if square_size != -1:
        # classic Gann square
        print "cells: %i" % (square_size * square_size)
        print "square size: %i" % square_size
        print "cell size: %i" % cell_size
        stream = open(output_file_name, 'w')
        create_gann_square_classic(square_size, cell_size, stream)
        stream.close()
    elif date_a and date_b:
        # date based Gann square
        delta = date_b - date_a
        square_size = int(math.ceil(math.sqrt(delta.days)))
        if square_size % 2 == 0:
            square_size += 1
        print "cells: %i" % (square_size * square_size)
        print "square size: %i" % square_size
        print "cell size: %i" % cell_size
        stream = open(output_file_name, 'w')
        marks = []
        if marks_file_name != '':
            fmarks = open(marks_file_name, 'r')
            marks = list(fmarks)
        create_gann_square_dates(square_size, cell_size, date_a, marks, stream)
        stream.close()
    else:
        print_usage()
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])