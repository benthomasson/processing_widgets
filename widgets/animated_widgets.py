

from math import pi

class Animated(object):

    @property
    def frameSpeed(self):
        return frameRate/self.speed

    @property
    def phasePercent(self):
        return 1.0 * (self.frame - self.frameSpeed * self.phase) / self.frameSpeed

    def draw(self):
        if self.frame < self.max_phase * self.frameSpeed:
            phase = getattr(self, "phase{0}".format(int(self.frame/self.frameSpeed)))
            phase()
            self.frame += 1
        else:
            self.final_phase()


class Check(Animated):

    def __init__(self, x, y, size=20, color="#00833C", speed=10):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = speed
        self.frame = 0
        self.phase = 0
        self.max_phase = 3

    def phase0(self):
        self.phase = 0
        pushMatrix()
        stroke(self.color)
        fill(255)
        translate(self.x, self.y)
        strokeWeight(self.size/10)
        ellipse(0, 0, self.size, self.size)
        popMatrix()

    def phase1(self):
        self.phase = 1
        pushMatrix()
        stroke(self.color)
        fill(255)
        translate(self.x, self.y)
        strokeWeight(self.size/10)
        ellipse(0, 0, self.size, self.size)
        strokeWeight(self.size/5)
        translate(0, self.size/4)
        rotate(pi/6)
        line(-self.size/4, 0, -self.size/4 * (1 - self.phasePercent), 0)
        popMatrix()

    def phase2(self):
        self.phase = 2
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
        line(-self.size * 0.6 * self.phasePercent, 0, 0, 0)
        popMatrix()

    def final_phase(self):
        self.phase = 3
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


class XMark(Animated):

    def __init__(self, x, y, size=20, color="#FF5000", speed=10):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = speed
        self.frame = 0
        self.phase = 0
        self.max_phase = 3

    def phase0(self):
        self.phase = 0
        pushMatrix()
        stroke(self.color)
        fill(255)
        translate(self.x, self.y)
        strokeWeight(self.size/10)
        ellipse(0, 0, self.size, self.size)
        popMatrix()

    def phase1(self):
        self.phase = 1
        pushMatrix()
        stroke(self.color)
        fill(255)
        translate(self.x, self.y)
        strokeWeight(self.size/10)
        ellipse(0, 0, self.size, self.size)
        strokeWeight(self.size/5)
        rotate(pi/4)
        translate(-self.size/2, 0)
        line(0, 0, self.size * self.phasePercent, 0)
        popMatrix()

    def phase2(self):
        self.phase = 2
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
        translate(-self.size/2, 0)
        line(0, 0, self.size * self.phasePercent, 0)
        popMatrix()

    def final_phase(self):
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
