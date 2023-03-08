#PartA
import random
x= random.randrange(1,10)
print(x)
import turtle 

screen=turtle.Screen()


turtle1=turtle.Turtle()
turtle2=turtle.Turtle()

turtle1.penup()
turtle1.goto(-100,20)
turtle1.pendown()

turtle2.penup()
turtle2.goto(-100,-20)
turtle2.pendown()

turtle1.forward(random.randint(1,100))
turtle2.forward(random.randint(1,100))


turtle1.penup()
turtle1.goto(-100,20)
turtle1.pendown()

turtle2.penup()
turtle2.goto(-100,-20)
turtle2.pendown()

for i in range(10):
    turtle1.forward(random.randrange(1,11))
    turtle2.forward(random.randrange(1,11))


screen.exitonclick()

# Race 2 is better and more correct when it comes to portraying a race as both start at the same time and the distance are still random.

#PartB

import pygame
import math


pygame.init()


window_size = (800, 600)


window = pygame.display.set_mode(window_size)


polygons = [
    {"sides": 3, "color": (255, 0, 0), "xpos": 50, "ypos": 50, "side_length": 50},
    {"sides": 4, "color": (0, 255, 0), "xpos": 150, "ypos": 50, "side_length": 50},
    {"sides": 6, "color": (0, 0, 255), "xpos": 250, "ypos": 50, "side_length": 50},
    {"sides": 20, "color": (255, 255, 0), "xpos": 350, "ypos": 50, "side_length": 20},
    {"sides": 100, "color": (255, 0, 255), "xpos": 450, "ypos": 50, "side_length": 10},
    {"sides": 360, "color": (0, 255, 255), "xpos": 550, "ypos": 50, "side_length": 5},
]


running = True
while running:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    for polygon in polygons:
        points = []
        for i in range(polygon["sides"]):
            angle = 360 / polygon["sides"]
            radians = math.radians(angle * i)
            x = polygon["xpos"] + polygon["side_length"] * math.cos(radians)
            y = polygon["ypos"] + polygon["side_length"] * math.sin(radians)
            points.append([x, y])
        pygame.draw.polygon(window, polygon["color"], points)
        pygame.display.flip()
        window.fill((0,0,0))
        pygame.time.wait(2000)

   


