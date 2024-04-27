import random
import numpy as np
import matplotlib.pyplot as plt

class Fractal:
    def __init__(self, sets):
        self.sets = sets
    sets = [{}]
    x = [0]
    y = [0]
    def iterate(self, times):
        for i in range(times):
            set = self.sets[int(random.random()*len(self.sets))]
            self.x.append(self.x[-1]*set["a"] + self.y[-1]*set["b"] + set["e"])
            self.y.append(self.x[-1]*set["c"] + self.y[-1]*set["d"] + set["f"])

    def draw(self):
        plt.scatter(self.x, self.y, s = 0.1)
        plt.show()