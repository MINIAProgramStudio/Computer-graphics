import turtle
import json
import os
import io
import PIL
from tkinter import *

if not os.path.isdir("data"):
    os.mkdir("data")

if os.path.isfile("data/memory.json"):
    file = open("data/memory.json","r+")
    memory = json.loads(file.read())
    file.close()
    del(file)
else:
    file = open("data/memory.json","x")
    file.close()
    del(file)
    memory = {"counter": 0}

turtle.setup(1000, 1000, 10, 10)
def draw_l_fractal(l_string,step,angle, name = ""):
    key = str(l_string)+";"+str(step)+";"+str(angle)
    if key in memory.keys():
        print("loaded")
        file_name = memory[key]
        if os.path.isfile("data/"+file_name):
            turtle.bgpic("data/"+file_name)
            input()
    else:
        turtle.speed(0)
        turtle.hideturtle()
        turtle.tracer(False)
        turtle.pendown()
        turtle.title(name)
        turtle.setworldcoordinates(-500,-500,1000,1000)
        for character in l_string:
            match(character):
                case "F":
                    turtle.forward(step)
                case "+":
                    turtle.left(angle)
                case "-":
                    turtle.right(angle)
                case _:
                    pass
        turtle.update()
        turtle_screen = turtle.getscreen()
        memory["counter"]+=1
        file_name = str(memory["counter"])+".ps"
        memory[key]=file_name
        turtle_screen.getcanvas().postscript(file="data/"+file_name)
        file = open("data/memory.json","w")
        file.write(json.dumps(memory, sort_keys=True))
        file.close()
        del(file)
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

def draw_nth_l_fractal(l_string, dictionary, step, angle, power = 0, name = ""):
    print("calculating")
    for i in range(power):
        l_string = iterate(l_string,dictionary)
    print("drawing")
    draw_l_fractal(l_string,step,angle,name)