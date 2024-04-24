import turtle

turtle.setup(1000, 1000, 10, 10)


def draw_l_fractal(l_string, step, angle, name=""):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.tracer(False)
    turtle.pendown()
    turtle.title(name)
    turtle.setworldcoordinates(-500, -500, 1000, 1000)
    for character in l_string:
        match (character):
            case "F":
                turtle.forward(step)
            case "+":
                turtle.left(angle)
            case "-":
                turtle.right(angle)
            case _:
                pass
    turtle.update()
    input()
    turtle.reset()


def iterate(l_string, dictionary):
    keys = dictionary.keys()
    new_l_string = ""
    for character in l_string:
        if character in keys:
            new_l_string += dictionary[character]
        else:
            new_l_string += character
    return new_l_string


def draw_nth_l_fractal(l_string, dictionary, step, angle, power=0, name=""):
    print("calculating")
    for i in range(power):
        l_string = iterate(l_string, dictionary)
    print("drawing")
    draw_l_fractal(l_string, step, angle, name)
