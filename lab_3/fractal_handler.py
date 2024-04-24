import turtle
import time

turtle.setup(1000, 1000, 10, 10)


def draw_l_fractal(l_string, step, angle, name="",t_reset = True, wait = True):
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
    if wait:
        input()
    if t_reset:

        turtle.reset()

def animate(l_string, step, angle_min, angle_max, angle_step = 1, sleep = 1, name = ""):
    angle = angle_min
    while angle<=angle_max:
        start = time.time()
        turtle.reset()
        draw_l_fractal(l_string,step, angle, name = name, t_reset=False, wait = False)
        turtle.update()
        sleep_time = sleep - time.time() + start
        if sleep_time > 0:
            time.sleep(sleep_time)
        angle+=angle_step
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
    for i in range(power):
        l_string = iterate(l_string, dictionary)
    draw_l_fractal(l_string, step, angle, name)

def animate_nth_fractal(l_string,dictionary, step, angle_min, angle_max, power = 0, angle_step = 1, sleep = 1, name = ""):
    for i in range(power):
        l_string = iterate(l_string, dictionary)
    animate(l_string,step,angle_min,angle_max,angle_step,sleep,name)
