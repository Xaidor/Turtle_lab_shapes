# Import Libraries 
import turtle as t
import numpy as np

# Declare Variables 
select_shape = str()
square_shape = str()
star_shape = str()
sun_shape = str()
select_color = str()
num_rays = int()

# Input statement 
select_shape = input("Select a shape (Star, Square, or Sun ")
select_color = input("What color would you like your shape? ")

# Proccess
num_rays = 7

# Draw circle for sun
if select_shape not 'star' | "square":
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.color(select_color)
    t.begin_fill()
    t.circle(70)
    t.end_fill()
# Draw sun rays 
t.penup()
t.goto(0,0)
t.pendown()

for ray in range(num_rays):
    t.penup()
    t.forward(70)
    t.pendown()
    t.forward(30)
    t.penup()
    
    for i in range(num_rays):
        t.left(60)
        t.forward(70)   


# Add sun rays to circle



# Output