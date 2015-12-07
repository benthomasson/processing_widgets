

import widgets
import random

from math import pi

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
    l = animated_widgets.SparkLine("CPU", "%", [], 133, 120, 40)


    widget_list.append(c)
    widget_list.append(x)
    widget_list.append(s)
    widget_list.append(l)


f = 0

def draw():
    global f
    clear()
    background(255)
    noFill()
    f+=1
    arc(250, 255, 50, 50, pi*3/2, pi*3/2 + f / 5.0)
    widgets.check(66, 30, 20)
    widgets.x_mark(66, 60, 20)
    widgets.square(66, 90, 20)
    for widget in widget_list:
        widget.draw()


def mousePressed():
    l.data.append(random.randint(0, 100))
