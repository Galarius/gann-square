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
            for dict in marks:
                data_path = dict["data_path"]
                with open(data_path) as sub_data_file:
                    data = list(sub_data_file)
                    dict.update({"data": data})
    return marks

