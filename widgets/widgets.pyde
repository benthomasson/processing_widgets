

import widgets

import animated_widgets

page_width = 200
page_height = 120

widget_list = []

def setup():
    size(page_width, page_height, FX2D)
    frameRate(30)
    widgets.check(66, 30, 20)
    widgets.x_mark(66, 60, 20)
    widgets.square(66, 90, 20)

    c = animated_widgets.Check(133, 30, 20)
    x = animated_widgets.XMark(133, 60, 20)
    s = animated_widgets.Square(133, 90, 20)

    widget_list.append(c)
    widget_list.append(x)
    widget_list.append(s)

def draw():
    for i in widget_list:
        i.draw()

