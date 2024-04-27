import turtle
import copy

depth = 0

def draw_rectangle(pos_x, pos_y, rotation, size_x, size_y, step=10):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.tracer(False)
    turtle.penup()
    turtle.goto(pos_x * step, pos_y * step)
    turtle.setheading(rotation)
    turtle.back(size_x * step / 2)
    turtle.left(90)
    turtle.forward(size_y * step / 2)
    turtle.pendown()
    turtle.setheading(rotation)
    turtle.forward(size_x * step)
    turtle.right(90)
    turtle.forward(size_y * step)
    turtle.right(90)
    turtle.forward(size_x * step)
    turtle.right(90)
    turtle.forward(size_y * step)
    turtle.update()


class Rectangle():
    def __init__(self, pos_x, pos_y, rotation, size_x, size_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rotation = rotation
        self.size_x = size_x
        self.size_y = size_y


class RectangleGroup():
    def __init__(self, pos_x, pos_y, rotation, size_x, size_y, contains=[]):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rotation = rotation
        self.size_x = size_x
        self.size_y = size_y
        self.contains = contains

    def draw(self, step, pos_x=0, pos_y=0, rotation=0, size_x=1, size_y=1):
        for element in self.contains:

            if isinstance(element, RectangleGroup):
                global depth
                print(depth)
                depth += 1
                element.draw(step, self.pos_x + pos_x * size_x, self.pos_y + pos_y*size_y, self.rotation * rotation,
                             self.size_x * size_x, self.size_y)
            else:
                draw_rectangle(pos_x + element.pos_x * self.size_x, pos_y + element.pos_y * self.size_y,
                               self.rotation + element.rotation, self.size_x * element.size_x,
                               self.size_y * element.size_y, step)

    def iterate(self, generator):
        for i in range(len(self.contains)):
            if isinstance(self.contains[i],RectangleGroup):
                global depth
                print(depth)
                depth += 1
                self.contains[i].iterate(generator)
            else:
                rect = copy.deepcopy(self.contains[i])
                self.contains[i] = copy.deepcopy(generator)
                self.contains[i].pos_x += rect.pos_x
                self.contains[i].pos_y += rect.pos_y
                self.contains[i].size_x *= rect.size_x
                self.contains[i].size_y *= rect.size_y
                self.contains[i].rotation += rect.rotation