# BrayanPenaherrera_turtle.py
# Name: Brayan Penaherrera
# Date: 03/19/2026
# program: BrayanPenaherrera_turtle.py
# Description: This program uses turtle graphics to draw two objects: Olympic style rings and
# a compass rose with direction labels.

import turtle

# =========================
# SETUP
# =========================
screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)
pen.hideturtle()

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# ==========================
# FUNCTIONS
# ==========================


def draw_circle(x, y, radius):
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.circle(radius)


def draw_line(x1, y1, x2, y2):
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)


def write_text(x, y, text_value):
    writer.goto(x, y)
    writer.write(text_value, align="center", font=("Arial", 16, "normal"))


# ==========================
# DRAW OLYMPIC STYLE RINGS
# ==========================
radius = 40

# Top row
draw_circle(-200, 120, radius)
draw_circle(-100, 120, radius)
draw_circle(0, 120, radius)

# Bottom row
draw_circle(-150, 80, radius)
draw_circle(-50, 80, radius)

# ==========================
# DRAW COMPASS ROSE
# ==========================
draw_line(120, 20, 120, -160)
draw_line(30, -70, 210, -70)
draw_circle(120, -70, 25)

write_text(120, 35, "North")
write_text(120, -195, "South")
write_text(-5, -78, "West")
write_text(245, -78, "East")

# ==========================
# FINISH
# ==========================
turtle.done()
