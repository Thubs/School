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
