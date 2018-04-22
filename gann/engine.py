# -*- coding: utf-8 -*-

"""
Tool to build Gann square.
"""

__author__ = 'Ilya Shoshin'
__copyright__ = 'Copyright 2015, Ilya Shoshin'
__all__ = ['create_gann_square_classic', 'create_gann_square_dates',
           'create_gann_square_dates_slice', 'create_gann_sub_square_dates']

import math

import core as gc
from   svg_builder import Builder

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
    square_size_2 = int(math.ceil(square_size / 2.0))
    sub_range = (-square_size_2+1, -square_size_2+1, square_size_2, square_size_2)
    create_gann_square_dates_slice(square_size, cell_size, base, marks, stream, sub_range)


def create_gann_sub_square_dates(sub_rect, cell_size, base, marks, stream):
    square_size = max(sub_rect[2] - sub_rect[0], sub_rect[3] - sub_rect[1])
    create_gann_square_dates_slice(square_size, cell_size, base, marks, stream, sub_rect)


def create_gann_square_dates_slice(square_size, cell_size, base, marks, stream, sub_rect):
    # setup
    size = square_size * cell_size + 1
    builder = Builder(square_size, cell_size)
    # draw grid
    build_grid(stream, builder, size, cell_size)
    # fill the grid
    origin_y, offset_x = size - cell_size - 1, 0
    for x in range(sub_rect[0], sub_rect[2]):
        offset_y = origin_y
        for y in range(sub_rect[1], sub_rect[3]):
            val = gc.get_date_from_pos(x, y, base)
            if x == y or -x == y:
                stream.write(builder.build_mark(offset_x, offset_y, Builder.none, Builder.blue_color, 1.5))
            if x == 0 or y == 0:
                stream.write(builder.build_mark(offset_x, offset_y, Builder.yellow_color, Builder.yellow_color))
            # marks highlighting
            in_off, highlighted_times = 0, 0
            for sub_marks in marks:
                if val.strftime("%d/%m/%Y") in sub_marks["data"]:
                    stream.write(builder.build_mark(offset_x, offset_y, sub_marks["color"], sub_marks["color"], 1,
                                                    in_off))
                    highlighted_times += 1
                if highlighted_times > 0:
                    in_off += 3

            stream.write(builder.build_text(offset_x+2, offset_y + cell_size * 0.5, val.strftime("%d/%m")))
            stream.write(builder.build_text(offset_x+2, offset_y + cell_size - 2, val.strftime("%Y")))
            offset_y -= cell_size
        offset_x += cell_size
    stream.write(builder.footer)