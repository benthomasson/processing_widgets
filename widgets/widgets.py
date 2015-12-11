

from math import pi


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
        textSize(int(self.size * 3/4))
        ellipse(-textWidth(count_str)/2, 0, self.size, self.size)
        rect(-textWidth(count_str)/2, -self.size/2, textWidth(count_str), self.size)
        ellipse(textWidth(count_str)/2, 0, self.size, self.size)
        translate(0, -self.size/10)
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
        rotate(pi/4)
        translate(self.size/2, 0)
        line(self.size/2, 0, 0, 0)
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
        ellipse(x,y, self.size, self.size)
        pushMatrix()
        translate(x, y)
        rotate(pi/4)
        translate(self.size/2, 0)
        line(self.size/2, 0, 0, 0)
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
            rotate(pi/2)
            line(self.size/2, 0, 0, 0)
            pushMatrix()
            translate(self.size/2, 0)
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
        strokeWeight(self.size/10)
        ellipse(0, 0, self.size, self.size)
        strokeWeight(self.size/5)
        translate(0, self.size/4)
        rotate(pi/6)
        line(-self.size/4, 0, 0, 0)
        rotate(pi/2)
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
        strokeWeight(self.size/10)
        ellipse(0, 0, self.size, self.size)
        strokeWeight(self.size/5)
        rotate(pi/4)
        line(-self.size/2, 0, self.size/2, 0)
        rotate(pi/2)
        line(-self.size/2, 0, self.size/2, 0)
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
        translate(-self.size/2, -self.size/2)
        strokeWeight(self.size/10)
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
        strokeWeight(self.size/10)
        ellipse(0, 0, self.size, self.size)
        popMatrix()


def circle(x, y, size, color="#5A5A5A", fill="#B9B9B9"):
    Circle(x, y, size, color, fill).draw()
