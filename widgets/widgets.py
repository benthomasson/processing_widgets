

from math import pi



def check(x, y, check_size=20, check_color="#00833C"):
    pushMatrix()
    stroke(check_color)
    fill(255)
    translate(x, y)
    strokeWeight(check_size/10)
    ellipse(0, 0, check_size, check_size)
    strokeWeight(check_size/5)
    translate(0, check_size/4)
    rotate(pi/6)
    line(-check_size/4, 0, 0, 0)
    rotate(pi/2)
    line(-check_size * 0.6, 0, 0, 0)
    popMatrix()

def x_mark(x, y, x_size=20, x_color="#FF5000"):
    pushMatrix()
    stroke(x_color)
    fill(255)
    translate(x, y)
    strokeWeight(x_size/10)
    ellipse(0, 0, x_size, x_size)
    strokeWeight(x_size/5)
    rotate(pi/4)
    line(-x_size/2, 0, x_size/2, 0)
    rotate(pi/2)
    line(-x_size/2, 0, x_size/2, 0)
    popMatrix()

def square(x, y, s_size, s_color="#5A5A5A", s_fill="#B9B9B9"):
    pushMatrix()
    stroke(s_color)
    fill(s_fill)
    translate(x, y)
    translate(-s_size/2, -s_size/2)
    strokeWeight(s_size/10)
    rect(0, 0, s_size, s_size)
    popMatrix()

