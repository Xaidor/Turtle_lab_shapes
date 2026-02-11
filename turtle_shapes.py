# Import Librarys 
import turtle as t
import random as r

shape_selection = str()
shape_color = str()
shape_fill = str()

# Grab input from user. Ask user to select a shape, color, and decide if they want the shape filled.
shape_selection = input("Select a shape (heart, star, square): ")
shape_color = input("What color would you like your shape to be? ")
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
        
    


