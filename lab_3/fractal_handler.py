import turtle

def draw_l_fractal(l_string,step,angle):
    fractal = turtle.Turtle()
    for character in l_string:
        match(character):
            case "F":
                fractal.forward(step)
            case "+":
                fractal.left(angle)
            case "-":
                fractal.right(angle)
            case _:
                pass

def iterate(l_string, dictionary):
    keys = dictionary.keys()
    new_l_string = ""
    for character in l_string:
        if character in keys:
            new_l_string += dictionary[character]
        else:
            new_l_string += character
    return new_l_string

def draw_nth_l_fractal(l_string, dictionary, step, angle, power = 0):
    for i in range(power):
        l_string = iterate(l_string,dictionary)
    draw_l_fractal(l_string,step,angle)