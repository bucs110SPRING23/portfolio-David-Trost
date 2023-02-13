import turtle 
sides=input("Enter the number of sides:")
sides=int(sides)
length=input("Enter the length of sides:")
length=int(length)

pen=turtle.Turtle()
pencolor=("orange")


window=turtle.Screen()

for s in range(sides):
    pen.forward(length)
    pen.right(360/sides)
    

window.exitonclick()
