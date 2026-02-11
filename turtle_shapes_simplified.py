# Import Libraries 
import turtle as t
import random as r

# Declare Variables Not needed, just for practice purposes
select_shape = str()
square_shape = str()
star_shape = str()
sun_shape = str()
select_color = str()

# Input statement 
select_shape = input("Select a shape (Star, Square, or Sun ")
select_color = input("What color would you like your shape? ")

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



# Add sun rays to circle



# Output