# -*- coding: utf-8 -*-

"""
marks_io.py
"""

__author__    = 'Ilya Shoshin'
__copyright__ = 'Copyright 2015, Ilya Shoshin'

__all__       = ['load_marks']

import json

def load_marks(file_name):
    """
    Load file with marks to highlight specific cell in Gann square.

    :param file_name:
    :return:
    """
    marks = []
    if file_name != '':
        with open(file_name) as data_file:
            marks = json.load(data_file)
            for i,dict in enumerate(marks):
                desc = dict["description"]
                data_path = dict["data_path"]
                if desc:
                    print '\t{0}. {1}'.format(i, desc)
                with open(data_path) as sub_data_file:
                    data = []
                    for line in sub_data_file:
                        if not line.startswith('#'):
                            if '#' in line:
                                parts = line.split('#')
                                line = parts[0].lstrip()
                            line = line.rstrip()
                            if line:
                                data.append(line)
                    dict.update({"data": data})
    return marks

