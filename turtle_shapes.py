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
def square(color, fill_shape):
    t.color(color)
    
    if fill_shape == "yes":
        t.begin_fill()

    for i in range(4):
        t.forward(100)
        t.right(90)

    if fill_shape == "yes":
        t.end_fill()

def heart(color, fill_shape):
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.color(color)

    if fill_shape == "yes":
        t.begin_fill()

    for i in range(200):
        t.right(1)
        t.forward(1)


# process 
if shape_selection == "square":
    square(shape_color, shape_fill)
    

t.done()
