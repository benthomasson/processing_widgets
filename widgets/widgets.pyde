

import processing_widgets.widgets as widgets
import random

from math import pi

import processing_widgets.animated_widgets as animated_widgets

page_width = 1024
page_height = 768

widget_list = []
l = None
glass = None
move = None
toggle = False
active_widgets = []
top_level_widgets = []


def clicked(button):
    print "Clicked! ", button


def setup():
    global widget_list, l, glass, move
    widget_list = []
    background(255)
    # https://github.com/processing/processing/issues/4198
    # noCursor fails to work on FX2D
    noCursor()
    size(page_width, page_height, FX2D)
    # It works with P2D
    # size(page_width, page_height, P2D)
    frameRate(30)

    c = animated_widgets.Check(133, 30, 20)
    x = animated_widgets.XMark(133, 60, 20)
    s = widgets.Circle(133, 90, 20)
    l = animated_widgets.SparkLine("CPU", "%", [], 133, 120, 40)

    glass = widgets.MagnifyingGlassMousePointer()
    move = widgets.MoveMousePointer()

    widget_list.append(c)
    widget_list.append(x)
    widget_list.append(s)
    widget_list.append(l)

    active_widgets.append(widgets.Button(x=0, y=0, label="Foo", call_back=clicked))
    active_widgets.append(widgets.SelectionButton(x=0, y=0, call_back=clicked))
    active_widgets.append(widgets.MoveButton(x=0, y=0, call_back=clicked))
    active_widgets.append(widgets.MagnifyingGlassButton(x=0, y=0, call_back=clicked))

    button_bar = widgets.ButtonBar(active_widgets, 400, 400)
    top_level_widgets.append(button_bar)

f = 0


def draw():
    global f
    clear()
    background(255)
    noFill()
    f += 1
    arc(250, 255, 50, 50, pi * 3 / 2, pi * 3 / 2 + f / 5.0)
    widgets.check(66, 30, 20)
    widgets.x_mark(66, 60, 20)
    widgets.square(66, 90, 20)
    widgets.notification_count(300, 300, 9999)
    for widget in active_widgets:
        if (mouseX > widget.left_extent and
                mouseX < widget.right_extent and
                mouseY > widget.top_extent and
                mouseY < widget.bottom_extent):
            widget.mouseOver()
        else:
            widget.mouseOut()
            widget.mouseReleased()
    for widget in top_level_widgets:
        widget.draw()
    for widget in widget_list:
        widget.draw()
    if toggle:
        glass.draw()
    else:
        move.draw()


def mousePressed():
    global toggle
    for widget in active_widgets:
        if (mouseX > widget.left_extent and
                mouseX < widget.right_extent and
                mouseY > widget.top_extent and
                mouseY < widget.bottom_extent):
            widget.mousePressed()
    l.data.append(random.randint(0, 100))
    toggle = not toggle


def mouseReleased():
    for widget in active_widgets:
        if (mouseX > widget.left_extent and
                mouseX < widget.right_extent and
                mouseY > widget.top_extent and
                mouseY < widget.bottom_extent):
            widget.mouseReleased()
