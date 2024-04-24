import turtle
import json
import os

if os.path.isfile("memory.json"):
    file = open("memory.json","r")
    memory = json.loads(file.read())
    print("memory loaded")
    file.close()
    del(file)
else:
    file = open("memory.json","x")
    file.close()
    del(file)
    memory = {}

turtle.setup(1000, 1000, 10, 10)
def draw_l_fractal(l_string,step,angle, name = ""):
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
    input()
    turtle.reset()

def iterate(l_string, dictionary):
    if str(l_string)+str(dictionary) in memory.keys():
        return memory[str(l_string)+str(dictionary)]
    else:
        keys = dictionary.keys()
        new_l_string = ""
        for character in l_string:
            if character in keys:
                new_l_string += dictionary[character]
            else:
                new_l_string += character
        memory[str(l_string)+str(dictionary)] = new_l_string
        file = open("memory.json","w")
        file.write(json.dumps(memory))
        file.close()
        del(file)
        return new_l_string

def draw_nth_l_fractal(l_string, dictionary, step, angle, power = 0, name = ""):
    for i in range(power):
        l_string = iterate(l_string,dictionary)
    draw_l_fractal(l_string,step,angle,name)