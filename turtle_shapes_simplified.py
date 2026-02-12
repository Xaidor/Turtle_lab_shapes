# Import Libraries 
import turtle as t
import random as r

# Declare Variables Not needed, just for practice purposes
select_shape = str()
select_color = str()

# Input statement 
select_shape = input("Select a shape (Star, Square, or Sun) ").lower()
select_color = input("What color would you like your shape? ").lower()

# Set color
t.color(select_color)

# square shape 
if select_shape == "square":
    t.penup()
    t.goto(-50,-50)
    t.pendown()
    
    for i in range(4): 
        t.forward(100)
        t.right(90)

elif select_shape == "star":
    t.penup()
    t.goto(0,-50)
    t.pendown()

    for i in range(5):
        t.forward(100)
        t.right(144)

# Draw circle for sun
elif select_shape == "sun":
    t.penup()
    t.goto(0,-50)
    t.pendown()
    t.cirlce(50)

# Add sun rays to circle
    num_rays = 10
    ray_length = 30

    t.penup()
    t.goto(0,0)
    
    angle_rays = 360 / num_rays

    for i in range(num_rays):
        t.pendown()
        t.forward(50)
        t.forward(ray_length)
        t.backward(50 + ray_length)
        t.penup()
        t.left(angle_rays) 

    else:
        t.write("Invalid shape selected!")
