import turtle

def draw_rectangle(pos_x, pos_y, rotation, size_x, size_y, step = 10):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.tracer(False)
    turtle.penup()
    turtle.goto(pos_x*step,pos_y*step)
    turtle.pendown()
    turtle.setheading(rotation)
    turtle.forward(size_x*step)
    turtle.right(90)
    turtle.forward(size_y*step)
    turtle.right(90)
    turtle.forward(size_x * step)
    turtle.right(90)
    turtle.forward(size_y * step)
    turtle.update()