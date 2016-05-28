#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, getopt
from datetime import datetime
import math

from gann import *

def print_usage():
    print """
          classic Gann square: gann.py -o <output file name> -s <square size>
          Gann square based on date: gann.py -o <output file name> -a <base date> -b <final date> -m <path to list of dates to mark>
          Gann sub square based on date: gann.py -o <output file name> -a <base date> -b <final date> -m <path to list of dates to mark> -r "<left>;<bottom>;<right>;<up>"

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
    left, bot, right, up = 0, 0, 0, 0
    # --------------------------------------
    try:
        opts, args = getopt.getopt(argv, "ho:s:a:b:m:r:", ["ofile=", "size=", "a_date=", "b_date=", "mfile=", "rect="])
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
        elif opt in ("-r", "--rect"):
            rect = arg.split(';')
            try:
                left, bot, right, up = int(rect[0]), int(rect[1]), int(rect[2]), int(rect[3])
            except ValueError as e:
                print 'Failed to parse range!'

    if output_file_name == '':
        print_usage()
        sys.exit(2)

    if square_size != -1:
        # classic Gann square
        # Info
        print "Cells: %i" % (square_size * square_size)
        print "Square size: %i" % square_size
        print "Cell size: %i" % cell_size
        print "Building..."
        stream = open(output_file_name, 'w')
        create_gann_square_classic(square_size, cell_size, stream)
        stream.close()
        print "Done."
    elif date_a and date_b:
        # date based Gann square
        delta = date_b - date_a
        square_size = int(math.ceil(math.sqrt(delta.days)))
        if square_size % 2 == 0:
            square_size += 1
        # Info
        print "Cells: %i" % (square_size * square_size)
        print "Square size: %i" % square_size
        print "Cell size: %i" % cell_size
        # Process
        print "Loading data..."
        marks = load_marks(marks_file_name)
        print "Building..."
        stream = open(output_file_name, 'w')
        if (left != 0 or bot != 0 or right != 0 or up != 0) and left < right and bot < up:
            create_gann_sub_square_dates((left, bot, right+1, up+1), cell_size, date_a, marks, stream)
        else:
            create_gann_square_dates(square_size, cell_size, date_a, marks, stream)
        stream.close()
        print "Done."
    else:
        print_usage()
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])