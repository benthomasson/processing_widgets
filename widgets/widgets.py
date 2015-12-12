

from math import pi


class Widget(object):

    def mouseOver(self):
        pass

    def mouseOut(self):
        pass

    def mousePressed(self):
        pass

    def mouseReleased(self):
        pass

    @property
    def top_extent(self):
        pass

    @property
    def bottom_extent(self):
        pass

    @property
    def left_extent(self):
        pass

    @property
    def right_extent(self):
        pass


class Button(Widget):

    def __init__(self, x, y, label, text_size=20, size=20, color="#5A5A5A", fill="#B9B9B9", pressed_color="#7F7F7F"):
        self.x = x
        self.y = y
        self.text_size = text_size
        self.label = label
        self.color = color
        self.fill = fill
        self.size = size
        self.pressed_color = pressed_color
        self.pressed = False
        self.active = False

    def mouseOver(self):
        self.active = True

    def mouseOut(self):
        self.active = False

    def mousePressed(self):
        self.pressed = True

    def mouseReleased(self):
        self.pressed = False

    @property
    def top_extent(self):
        return self.y

    @property
    def left_extent(self):
        return self.x

    @property
    def right_extent(self):
        textSize(self.text_size)
        return self.x + textWidth(self.label) + self.size

    @property
    def bottom_extent(self):
        return self.y + self.size + self.text_size

    def draw(self):
        self.draw_button()
        self.draw_icon()
        self.draw_label()

    def draw_button(self):
        pushMatrix()
        translate(self.x, self.y)
        if self.active:
            stroke(self.color)
        else:
            stroke(self.fill)
        if self.pressed:
            fill(self.pressed_color)
        else:
            fill(self.fill)
        textSize(self.text_size)
        rect(0, 0, textWidth(self.label) + self.size, self.size + self.text_size)
        popMatrix()

    def draw_icon(self):
        pass

    def draw_label(self):
        pushMatrix()
        translate(self.x, self.y)
        translate((textWidth(self.label) + self.size) / 2,
                  (self.size + self.text_size) / 2 - self.text_size / 4)
        textAlign(CENTER, CENTER)
        fill(self.color)
        text(self.label, 0, 0)
        popMatrix()
        textAlign(LEFT, BASELINE)


def button(x, y, label, text_size=20, size=20, color="#5A5A5A", fill="#B9B9B9"):
    Button(x, y, label, text_size, size, color, fill).draw()


class NotificationCount(object):

    def __init__(self, x, y, count=0, size=20):
        self.x = x
        self.y = y
        self.count = count
        self.size = size

    def draw(self):
        pushMatrix()
        translate(self.x, self.y)
        textAlign(CENTER, CENTER)
        stroke("#FF5000")
        fill("#FF5000")
        count_str = str(self.count)
        textSize(int(self.size * 3 / 4))
        ellipse(-textWidth(count_str) / 2, 0, self.size, self.size)
        rect(-textWidth(count_str) / 2, -self.size /
             2, textWidth(count_str), self.size)
        ellipse(textWidth(count_str) / 2, 0, self.size, self.size)
        translate(0, -self.size / 10)
        fill(255)
        text(count_str, 0, 0)
        popMatrix()
        textAlign(LEFT, BASELINE)


def notification_count(x, y, count):
    NotificationCount(x, y, count).draw()


class ToolBar(object):

    def __init__(self, tools, x=0, y=0, size=40, color="#5A5A5A", fill="#B9B9B9"):
        self.x = x
        self.y = y
        self.color = color
        self.fill = fill
        self.size = size
        self.tools = []
        self.tools.extend(tools)

    def draw(self):
        pushMatrix()
        translate(self.x, self.y)
        strokeWeight(2)
        fill(self.fill)
        stroke(self.color)
        rect(0, 0, self.size * len(self.tools), self.size)
        translate(self.size/2, self.size/2)
        for tool in self.tools:
            tool.draw()
            translate(self.size, 0)
        popMatrix()


class SelectionTool(object):

    def __init__(self, x, y, size=20, color="#5A5A5A"):
        self.size = size
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        x = self.x
        y = self.y
        strokeWeight(2)
        stroke(self.color)
        fill(self.color)
        translate(x, y)
        rotate(pi/3)
        rotate(pi)
        translate(-self.size/2, 0)
        line(self.size, 0, 0, 0)
        pushMatrix()
        translate(self.size, 0)
        triangle(0, 0, -10, 5, -10, -5)
        popMatrix()


class MoveTool(object):

    def __init__(self, x, y, size=20, color="#5A5A5A"):
        self.size = size
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        x = self.x
        y = self.y
        strokeWeight(2)
        stroke(self.color)
        pushMatrix()
        translate(x, y)
        for r in xrange(4):
            rotate(pi/2)
            line(self.size/2, 0, 0, 0)
            pushMatrix()
            translate(self.size/2, 0)
            triangle(0, 0, -4, 2, -4, -2)
            popMatrix()
        popMatrix()


class MagnifyingGlassTool(object):

    def __init__(self, x, y, size=20, color="#5A5A5A"):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self):
        x = self.x
        y = self.y
        strokeWeight(2)
        noFill()
        stroke(self.color)
        ellipse(x, y, self.size, self.size)
        pushMatrix()
        translate(x, y)
        rotate(pi / 4)
        translate(self.size / 2, 0)
        line(self.size / 2, 0, 0, 0)
        popMatrix()
        pushMatrix()
        translate(x, y)
        rotate(pi / 2)
        for r in xrange(2):
            rotate(pi)
            pushMatrix()
            translate(self.size, 0)
            line(self.size / 2, 0, 0, 0)
            translate(self.size / 2, 0)
            triangle(0, 0, -4, 2, -4, -2)
            popMatrix()
        popMatrix()


class MagnifyingGlassMousePointer(object):

    def __init__(self, size=20, color="#5A5A5A"):
        self.size = size
        self.color = color

    def draw(self):
        x = mouseX
        y = mouseY
        strokeWeight(2)
        noFill()
        stroke(self.color)
        ellipse(x, y, self.size, self.size)
        pushMatrix()
        translate(x, y)
        rotate(pi / 4)
        translate(self.size / 2, 0)
        line(self.size / 2, 0, 0, 0)
        popMatrix()


class MoveMousePointer(object):

    def __init__(self, size=20, color="#5A5A5A"):
        self.size = size
        self.color = color

    def draw(self):
        x = mouseX
        y = mouseY
        strokeWeight(2)
        stroke(self.color)
        pushMatrix()
        translate(x, y)
        for r in xrange(4):
            rotate(pi / 2)
            line(self.size / 2, 0, 0, 0)
            pushMatrix()
            translate(self.size / 2, 0)
            triangle(0, 0, -4, 2, -4, -2)
            popMatrix()
        popMatrix()


class Check(object):

    def __init__(self, x, y, size=20, color="#00833C"):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self):
        pushMatrix()
        stroke(self.color)
        fill(255)
        translate(self.x, self.y)
        strokeWeight(self.size / 10)
        ellipse(0, 0, self.size, self.size)
        strokeWeight(self.size / 5)
        translate(0, self.size / 4)
        rotate(pi / 6)
        line(-self.size / 4, 0, 0, 0)
        rotate(pi / 2)
        line(-self.size * 0.6, 0, 0, 0)
        popMatrix()


def check(x, y, size=20, color="#00833C"):
    Check(x, y, size, color).draw()


class XMark(object):

    def __init__(self, x, y, size=20, color="#FF5000"):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self):
        pushMatrix()
        stroke(self.color)
        fill(255)
        translate(self.x, self.y)
        strokeWeight(self.size / 10)
        ellipse(0, 0, self.size, self.size)
        strokeWeight(self.size / 5)
        rotate(pi / 4)
        line(-self.size / 2, 0, self.size / 2, 0)
        rotate(pi / 2)
        line(-self.size / 2, 0, self.size / 2, 0)
        popMatrix()


def x_mark(x, y, size=20, color="#FF5000"):
    XMark(x, y, size, color).draw()


class Square(object):

    def __init__(self, x, y, size, color="#5A5A5A", fill="#B9B9B9"):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.fill = fill

    def draw(self):
        pushMatrix()
        stroke(self.color)
        fill(self.fill)
        translate(self.x, self.y)
        translate(-self.size / 2, -self.size / 2)
        strokeWeight(self.size / 10)
        rect(0, 0, self.size, self.size)
        popMatrix()


def square(x, y, size, color="#5A5A5A", fill="#B9B9B9"):
    Square(x, y, size, color, fill).draw()


class Circle(object):

    def __init__(self, x, y, size, color="#5A5A5A", fill="#B9B9B9"):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.fill = fill

    def draw(self):
        pushMatrix()
        stroke(self.color)
        fill(self.fill)
        translate(self.x, self.y)
        strokeWeight(self.size / 10)
        ellipse(0, 0, self.size, self.size)
        popMatrix()


def circle(x, y, size, color="#5A5A5A", fill="#B9B9B9"):
    Circle(x, y, size, color, fill).draw()
