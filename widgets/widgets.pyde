

import widgets
import random

import animated_widgets

page_width = 1024
page_height = 768

widget_list = []
l = None


def setup():
    global widget_list, l
    widget_list = []
    background(255)
    size(page_width, page_height, FX2D)
    frameRate(30)

    c = animated_widgets.Check(133, 30, 20)
    x = animated_widgets.XMark(133, 60, 20)
    s = widgets.Circle(133, 90, 20)
    l = animated_widgets.SparkLine("CPU", "%", [
                                   0, 5, 100, 2, 30, 90, 50, 10, 20, 10, 100, 20, 100, 10, 30, 100, 10, 10, 0, 100], 133, 120, 40)

    widget_list.append(c)
    widget_list.append(x)
    widget_list.append(s)
    widget_list.append(l)


def draw():
    clear()
    background(255)
    widgets.check(66, 30, 20)
    widgets.x_mark(66, 60, 20)
    widgets.square(66, 90, 20)
    for i in widget_list:
        i.draw()


def mousePressed():
    l.data.append(random.randint(0, 100))
