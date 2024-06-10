# Визначити фрактальну розмірність фрактала, що складається з тих точок
# відрізка [0; 1], в десятковому представленні яких відсутні цифри 3 та 7.
# Розробити програмне забезпечення для побудови даного фрактала.

import copy
import matplotlib.pyplot as plt
from tqdm import tqdm

def create_fractal(depth, digits = (0,1,2,4,5,6,8,9), y_distance = 0.01):
    x = [0, 1]
    x_level = [0, 1]
    y = [-y_distance, -y_distance]
    for level in range(depth):
        level += 1
        x_new_level = []
        addition_digits = []
        for digit in digits:
            addition_digits.append(digit*10**(-level))
        for dot in tqdm(range(len(x_level)-1)):
            for ad_digit in addition_digits:
                x_new_level.append(x_level[dot] + ad_digit)
        y+=[-y_distance*level]*((len(x_level)-1)*len(digits))
        x_level = copy.deepcopy(x_new_level) + [1]
        x += x_level
        y += [-y_distance*level]
    return [x,y]

def draw_fractal(dots):
    plt.scatter(dots[0], dots[1], 0.1)
    plt.show()

draw_fractal(create_fractal(8))