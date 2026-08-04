# Brayan Penhaerrera         03/23/2026            hitTheTarget.py

'''
# This program launches a projectule toward a target using turtle graphics.
# If the projectile misses, the program gives hints about wether the angle or force should be increased or decreased. 
'''
# ========================Hit the Target Game
import turtle as t

# =============================Named constants
SCREEN_WIDTH = 600    # Screen width
SCREEN_HEIGHT = 600   # Screen height
TARGET_LLEFT_X = 100  # Target's lower-left X
TARGET_LLEFT_Y = 250  # Target's lower-left Y
TARGET_WIDTH = 25     # Width of the target
FORCE_FACTOR = 30     # Arbitrary force factor
PROJECTILE_SPEED = 1  # Projectile's animation speed
NORTH = 90            # Angle of north direction
SOUTH = 270           # Angle of south direction
EAST = 0              # Angle of east direction
WEST = 180            # Angle of west direction

# ============================Setup the window.
t.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# ==============================Draw the target.
t.hideturtle()
t.speed(0)
t.penup()
t.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
t.pendown()
t.setheading(EAST)
t.forward(TARGET_WIDTH)
t.setheading(NORTH)
t.forward(TARGET_WIDTH)
t.setheading(WEST)
t.forward(TARGET_WIDTH)
t.setheading(SOUTH)
t.forward(TARGET_WIDTH)
t.penup()

# =============================Center the turtle
t.goto(0, 0)
t.setheading(EAST)
t.showturtle()
t.speed(PROJECTILE_SPEED)

# =====================Get the angle and force from the user.
angle = t.numinput('Input Needed', 'Enter projectile angle')
force = t.numinput('Input needed', 'Enter launch force (1-10) ')


# ========================Calculate the distance.
distance = force * FORCE_FACTOR

# =========================Set the heading.
t.setheading(angle)

# =====================Launch the projectile.
t.pendown()
t.forward(distance)

# =======================Did it hit the target?
if (t.xcor() >= TARGET_LLEFT_X and
    t.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    t.ycor() >= TARGET_LLEFT_Y and
        t.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print('Target hit!')
else:
    print('You missed the target.')

    if t.xcor() < TARGET_LLEFT_X:
        print("Use more force.")

    if t.xcor() > (TARGET_LLEFT_X + TARGET_WIDTH):
        print("Use less force.")

    if t.ycor() < TARGET_LLEFT_Y:
        print("Try a greater angle.")

    if t.ycor() > (TARGET_LLEFT_Y + TARGET_WIDTH):
        print("Try a smaller angle.")

t.done()
