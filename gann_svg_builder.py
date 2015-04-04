# -*- coding: utf-8 -*-
__author__ = 'galarius'


class Builder:
    """
    Helper xml strings for building Gann square
    """
    # templates
    header_template = """<?xml version="1.0"?>
    <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
    <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="%i" height="%i">
    """
    x_line_template = '<line x1="%i" y1="%i" x2="%i" y2="%i" stroke-width="%f" stroke="%s"/>\n'
    y_line_template = '<line x1="%i" y1="%i" x2="%i" y2="%i" stroke-width="%f" stroke="%s"/>\n'
    mark_template = '<rect x="%i" y="%i" width="%i" height="%i" fill="%s" stroke="%s" stroke-width="%f" />'
    text_template = '<text x="%f" y="%f" font-size ="%fpx">%s</text>\n'
    # consts
    line_width = 0.5
    mark_line_width = 1
    font_size = 10
    dark_color = 'black'
    blue_color = 'blue'
    yellow_color = 'yellow'
    red_color = 'red'
    none = 'none'

    def __init__(self, square_size, cell_size):
        self.size = square_size * cell_size
        self.square_size = square_size
        self.cell_size = cell_size
        self.header = self.header_template % (self.size, self.size)

    def build_line_x(self, i):
        return self.x_line_template % (0, i, self.size, i, self.line_width, self.dark_color)

    def build_line_y(self, i):
        return self.x_line_template % (i, 0, i, self.size, self.line_width, self.dark_color)

    def build_mark(self, x, y, fill_color, stroke_color, line_width=1):
        return self.mark_template % (x, y, self.cell_size, self.cell_size, fill_color, stroke_color, line_width)

    def build_text(self, x, y, text):
        return self.text_template % (x, y, self.font_size, text)