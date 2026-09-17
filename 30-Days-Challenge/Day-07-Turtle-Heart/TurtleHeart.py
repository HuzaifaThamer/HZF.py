import turtle
import math
import time


screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("#050510")
screen.title("Python Heart")
screen.tracer(0)


pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(4)
pen.color("#ff1744", "#ff1744")


def heart_point(angle, scale=18):
    x = 16 * math.sin(angle) ** 3
    y = (
        13 * math.cos(angle)
        - 5 * math.cos(2 * angle)
        - 2 * math.cos(3 * angle)
        - math.cos(4 * angle)
    )

    return x * scale, y * scale


pen.penup()
pen.goto(heart_point(0))
pen.pendown()
pen.begin_fill()

for degree in range(361):
    angle = math.radians(degree)
    pen.goto(heart_point(angle))

    screen.update()
    time.sleep(0.004)

pen.end_fill()
screen.update()
turtle.done()
































