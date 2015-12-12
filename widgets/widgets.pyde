

import widgets
import random

from math import pi

import animated_widgets

page_width = 1024
page_height = 768

widget_list = []
l = None
glass = None
move = None
toggle = False
bar = None
active_widgets = []


def setup():
    global widget_list, l, glass, move, bar
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

    bar = widgets.ToolBar([widgets.MoveTool(x=0, y=0),
                           widgets.MagnifyingGlassTool(x=0, y=0),
                           widgets.SelectionTool(x=0, y=0)], x=200, y=0)
    glass = widgets.MagnifyingGlassMousePointer()
    move = widgets.MoveMousePointer()

    widget_list.append(c)
    widget_list.append(x)
    widget_list.append(s)
    widget_list.append(l)

    active_widgets.append(widgets.Button(x=300, y=400, label="Foo"))
    active_widgets.append(widgets.SelectionButton(x=400, y=400))
    active_widgets.append(widgets.MoveButton(x=500, y=400))
    active_widgets.append(widgets.MagnifyingGlassButton(x=600, y=400))

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
    bar.draw()
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
    for widget in active_widgets:
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
