import turtle 
import random


t = turtle.Turtle()
t.speed('fastest')
t.penup()
t.goto(0, 0)
t.pendown()


screen = turtle.Screen()
screen_width = screen.window_width() // 2
screen_height = screen.window_height() // 2


while -screen_width <= t.xcor() <= screen_width and -screen_height <= t.ycor() <= screen_height:
    if random.choice(['heads', 'tails']) == 'heads':
        t.left(90)
    else:
        t.right(90)
    
    t.forward(50)


t.penup()
t.hideturtle()
turtle.done()