# Brayan Penaherrera, 04/14/2026, BrayanPenaherrera_PE5_2.py
# This program uses turtle graphics to draw a modular snowman.

import turtle


def drawBase(t):
    t.penup()
    t.goto(0, -240)
    t.pendown()
    t.circle(100)


def drawMidsection(t):
    t.penup()
    t.goto(0, -40)
    t.pendown()
    t.circle(60)


def drawHead(t):
    t.penup()
    t.goto(0, 80)
    t.pendown()
    t.circle(40)

    # left eye
    t.penup()
    t.goto(-15, 130)
    t.pendown()
    t.circle(4)

    # right eye
    t.penup()
    t.goto(15, 130)
    t.pendown()
    t.circle(4)

    # mouth
    t.penup()
    t.goto(-15, 105)
    t.pendown()
    t.forward(30)


def drawArms(t):

    # left arm
    t.penup()
    t.goto(-55, 10)
    t.pendown()
    t.goto(-115, 35)
    t.goto(-130, 80)

    t.penup()
    t.goto(-130, 80)
    t.pendown()
    t.goto(-145, 75)

    t.penup()
    t.goto(-130, 80)
    t.pendown()
    t.goto(-128, 95)

    # right arm
    t.penup()
    t.goto(55, 10)
    t.pendown()
    t.goto(115, 35)
    t.goto(130, 80)

    t.penup()
    t.goto(130, 80)
    t.pendown()
    t.goto(145, 75)

    t.penup()
    t.goto(130, 80)
    t.pendown()
    t.goto(128, 95)


def drawHat(t):
    t.fillcolor("black")

    # brim
    t.penup()
    t.goto(-65, 160)
    t.pendown()
    t.begin_fill()
    for count in range(2):
        t.forward(130)
        t.left(90)
        t.forward(20)
        t.left(90)
    t.end_fill()

    # top of hat
    t.penup()
    t.goto(-35, 180)
    t.pendown()
    t.begin_fill()
    for count in range(2):
        t.forward(70)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.end_fill()


def drawButtons(t):
    t.penup()
    t.goto(0, 40)
    t.pendown()
    t.circle(4)

    t.penup()
    t.goto(0, 15)
    t.pendown()
    t.circle(4)

    t.penup()
    t.goto(0, -10)
    t.pendown()
    t.circle(4)


def drawScarf(t):
    t.color("red")
    t.pensize(6)

    # scarf aroudn neck
    t.penup()
    t.goto(-35, 78)
    t.pendown()
    t.goto(35, 78)

    # scarf hanging down
    t.penup()
    t.goto(10, 78)
    t.pendown()
    t.goto(10, 45)

    t.pensize(1)
    t.color("black")


def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(3)

    drawBase(t)
    drawMidsection(t)
    drawHead(t)
    drawArms(t)
    drawHat(t)
    drawButtons(t)
    drawScarf(t)

    turtle.done()


main()
