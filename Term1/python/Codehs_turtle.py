from turtle import *

# Circles

circle(20)
penup()
forward(40)
pendown()
circle(20)
penup()
forward(40)
pendown()
circle(20)
penup()
forward(40)
pendown()
circle(20)
penup()
forward(40)
pendown()
circle(20)

# Square

forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

# X and Y axis

penup()
left(90)
forward(200)
right(90)
right(90)
pendown()
forward(400)
penup()
right(90)
forward(200)
right(90)
forward(200)
right(90)
pendown()
forward(400)

# loops

penup()
backward(200)

for i in range (40):
    pendown()
    forward(5)
    penup()
    forward(5)

# asterik

speed(5)

left(30)
for i in range(6):
    forward(100)
    backward(100)
    left(60)

# four circle

speed(5)

penup()
setposition(-50,-100)

for i in range (2):
    pendown()
    circle(50)
    penup()
    forward(100)

setposition(-50,0)

for i in range (2):
    pendown()
    circle(50)
    penup()
    forward(100)

# Circle pyramid

circle(50)
penup()
setposition(-50,-100)
pendown()

for i in range(2):
    circle(50)
    penup()
    forward(100)
    pendown()

penup()    
setposition(-100,-200)
pendown()

for i in range(3):
    circle(50)
    penup()
    forward(100)
    pendown()

# Circle ring

penup()
setposition(0,-100)
pendown()

def circle_ring():
    for i in range(36):
        circle(10)
        penup()
        left(10)
        forward(20)
        pendown()

circle_ring()

# Shape stack

penup()
setposition(0,-200)
pendown()

def square():
    for i in range(4):
        forward(50)
        left(90)

for i in range(4):
    square()
    penup()
    forward(50)
    left(90)
    forward(75)
    pendown()
    circle(25)
    penup()
    forward(25)
    left(90)
    forward(50)
    left(180)
    pendown()

# Rainbow octagon

# This program will draw an octagon where each side is a different color.

speed(5)
pensize(5)
"""
Draw one side of shape, then change color and turn 60 degrees before
drawing next line. Continue for 8 lines to complete octagon.
"""
color("red")
forward(50)
left(45)
color("orange")
forward(50)
left(45)
color("yellow")
forward(50)
left(45)
color("green")
forward(50)
left(45)
color("blue")
forward(50)
left(45)
color("indigo")
forward(50)
left(45)
color("purple")
forward(50)
left(45)
color("pink")
forward(50)

# Circle square triangle

"""
This program draws three shapes from the same position. Each shape is a 
different color.
"""

speed(5)

# Draws a red circle
color("red")
begin_fill()
circle(75)
end_fill()

# Draws a blue square due to 4 steps
color("blue")
begin_fill()
circle(75,360,4)
end_fill()

# Draws a yellow triangle due to 3 steps
color("yellow")
begin_fill()
circle(75,360,3)
end_fill()

# Four coloured triangle

speed(5)
def multicolored_triangle():
    for i in range(4):
        pendown()
        left(120)
        color("blue")
        forward(50)
        color("green")
        left(120)
        forward(50)
        color("red")
        left(120)
        forward(50)
        penup()
        forward(50)
        
       
        
penup()
pensize(5)
backward(100)
pendown()
multicolored_triangle()
