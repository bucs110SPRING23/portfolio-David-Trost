import turtle

def draw_rectangle(turtle, width, height, color):
    turtle.color("black", color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_triangle(turtle, length, color):
    turtle.color("black", color)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)
    turtle.end_fill()

def draw_door(turtle):
    turtle.penup()
    turtle.goto(-30, 0)
    turtle.pendown()
    draw_rectangle(turtle, 60, 100, "brown")

def draw_window(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    draw_rectangle(turtle, 40, 40, "white")

def draw_roof(turtle):
    turtle.penup()
    turtle.goto(-112.5, 200)
    turtle.pendown()
    draw_triangle(turtle, 225, "black")

def draw_house(turtle):
    draw_rectangle(turtle, 200, 200, "gray")
    draw_roof(turtle)
    draw_door(turtle)
    draw_window(turtle, -80, 45)
    draw_window(turtle, 40, 45)

# Create a turtle instance
house = turtle.Turtle()

# Move turtle to starting position
house.penup()
house.goto(-100, 0)
house.pendown()

# Draw the house
draw_house(house)

# Hide the turtle
house.hideturtle()

# Keep the window open until closed manually
turtle.done()
