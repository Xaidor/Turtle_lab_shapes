# Import Librarys 
import turtle as t

shape_selection = str()
shape_color = str()
shape_fill = str()

# Grab input from user. Ask user to select a shape, color, and decide if they want the shape filled.
shape_selection = input("Select a shape (heart, star, square): ")
shape_color = input("What color would you like your shape to be? (square, star, heart): ")
shape_fill = input("Would you like to be filled? (yes/no): ")

# Create functions for each shape. Square, heart, and star.
# SQUARE
def square(color, fill_shape):
    t.color(color)
    
    if fill_shape == "yes":
        t.begin_fill()

    for i in range(4):
        t.forward(100)
        t.right(90)

    if fill_shape == "yes":
        t.end_fill()

#HEART
def heart(color, fill_shape):
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.color(color)

    if fill_shape == "yes":
        t.begin_fill()

# Left side of heart
    t.left(140)
    t.forward(113)
# Left curve of heart
    for i in range(200):
        t.right(1)
        t.forward(1)

# Bottom 
    t.left(120)

# Right curve 
    for i in range(200):
        t.right(1)
        t.forward(1)
# Right side of the heart
    t.forward(113)

    if fill_shape == "yes":
        t.end_fill()


# process 
if shape_selection == "square":
    square(shape_color, shape_fill)

elif shape_selection == "heart":
    heart(shape_color, shape_fill)
    

t.done()
