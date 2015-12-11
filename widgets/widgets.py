

from math import pi


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
        translate(x, y)
        rotate(pi/4)
        translate(self.size/2, 0)
        line(self.size/2, 0, 0, 0)


class MoveMousePointer(object):

    def __init__(self, size=20, color="#5A5A5A"):
        self.size = size
        self.color = color

    def draw(self):
        x = mouseX
        y = mouseY
        strokeWeight(2)
        stroke(self.color)
        translate(x, y)
        for r in xrange(4):
            rotate(pi/2)
            line(self.size/2, 0, 0, 0)
            pushMatrix()
            translate(self.size/2, 0)
            triangle(0, 0, -4, 2, -4, -2)
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
