import turtle
import math
import random
n = float(input(" PLease enter a positive integer n more than 1: n = "))
while n <= 1 or n % 1 != 0 :
    n = float(input("The number must be more than 1 and integer, n = : "))
n = int(n)

screen = turtle.Screen()
screen.title("Random Points On OYX Plane")
screen.setup(width=600, height=600)
screen.setworldcoordinates(-1.5, -1.5, 1.5, 1.5)
screen.bgcolor("white")

oxy_drawer = turtle.Turtle()
oxy_drawer.hideturtle()
oxy_drawer.speed(0)

oxy_drawer.penup()
oxy_drawer.goto(-1.5, 0)
oxy_drawer.pendown()
oxy_drawer.goto(1.5, 0)
oxy_drawer.penup()
oxy_drawer.goto(0, -1.5)
oxy_drawer.pendown()
oxy_drawer.goto(0, 1.5)

oxy_drawer.penup()
oxy_drawer.goto(1.4, -0.1)
oxy_drawer.write("X", align="center", font=("Arial", 12, "bold"))

oxy_drawer.goto(-0.1, 1.4)
oxy_drawer.write("Y", align="center", font=("Arial", 12, "bold"))

oxy_drawer.goto(0.1, -0.1)
oxy_drawer.write("O", align="center", font=("Arial", 12, "bold"))

point_drawer = turtle.Turtle()
point_drawer.hideturtle()
point_drawer.speed(0)
point_drawer.penup()

def plot_point(x, y, color):
    point_drawer.goto(x, y)
    point_drawer.dot(5, color)

for i in range(n):
    while True:
        a = random.random()   # ნულზე მკაცრად მეტი რომ იყო რიცხვი ამიტომ გამოვიყენე ეს ციკლი.
        if a != 0:
            break
    while True:
        b = random.random()
        if b != 0:
            break
    if math.sqrt(a**2 + b**2) <= 1:
        plot_point(a, b, "red")
    else:
        plot_point(a, b, "green")

turtle.done()