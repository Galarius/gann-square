# -*- coding: utf-8 -*-
#!/usr/bin/env python

__author__ = 'Ilya Shoshin'
__copyright__ = 'Copyright 2015, Ilya Shoshin'

# to capture console args
import sys, getopt
import math
from core import *
from tests import *

from datetime import datetime


def draw_grid(square_size, cell_size, base, marks, stream):
    size = square_size * cell_size + 1
    header = """<?xml version="1.0"?>
    <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
    <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="%i" height="%i">
    """ % (size, size)
    stream.write(header)

    color = 'black'
    x_text = '<line x1="0" y1="%i" x2="' + str(size) + '" y2="%i" stroke-width="0.5" stroke="%s"/>\n'
    y_text = '<line x1="%i" y1="0" x2="%i" y2="' + str(size) + '" stroke-width="0.5" stroke="%s"/>\n'

    for i in range(0, size + 1, cell_size):
        stream.write(x_text % (i, i, color))
        stream.write(y_text % (i, i, color))

    wtext = '<text x="%i" y="%i" font-size ="10px">%s</text>\n'
    bl = 'blue'
    yl = 'yellow'
    rd = 'red'
    wmark = '<rect x="%i" y="%i" width="%i" height="%i" fill="%s" stroke="%s" stroke-width="1" />'


    square_size_2 = square_size / 2
    originx = 0
    originy = square_size_2 + cell_size * square_size - 15
    offsetx = originx
    for x in range(-square_size_2, square_size_2+1):
        offsety = originy
        for y in range(-square_size_2, square_size_2+1):
            val = get_date_from_pos(x, y, base)
            if x == y or -x == y:
                stream.write(wmark % (offsetx, offsety-cell_size+9, cell_size, cell_size, 'none', bl))
            if x == 0 or y == 0:
                stream.write(wmark % (offsetx, offsety-cell_size+9, cell_size, cell_size, yl, yl))
            if val.strftime("%d/%m/%Y\n") in marks:
                stream.write(wmark % (offsetx, offsety-cell_size+9, cell_size, cell_size, rd, rd))
            stream.write(wtext % (offsetx, offsety, val.strftime("%d/%m")))
            offsety -= cell_size
        offsetx += cell_size


    stream.flush()


def main(argv):
    date_format = "%d/%m/%Y"
    a = datetime.strptime('7/04/2001', date_format)
    b = datetime.strptime('15/03/2015', date_format)
    delta = b - a
    square_size = int(math.ceil(math.sqrt(delta.days)))
    # square_size = 19
    cell_size = 30  #max(30, square_size / 2)

    print "cells: %i" % (square_size * square_size)
    print "square size: %i" % square_size
    print "cell size: %i" % cell_size

    filename = 'test.html'
    wr = open(filename, 'w')
    fmarks = open('marks.txt', 'r')
    marks = list(fmarks)
    draw_grid(square_size, cell_size, a, marks, wr)
    wr.close()


if __name__ == "__main__":
    main(sys.argv[1:])