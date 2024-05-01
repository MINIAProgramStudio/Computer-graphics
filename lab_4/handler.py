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
            set_r = random.random()
            set_pos = -1
            while set_r > 0:
                set_pos+=1
                set_r -= self.sets[set_pos]["p"]

                
            set = self.sets[set_pos]
            self.x.append(self.x[-1]*set["a"] + self.y[-1]*set["b"] + set["e"])
            self.y.append(self.x[-2]*set["c"] + self.y[-1]*set["d"] + set["f"])

    def draw(self,min_dot = 0):
        fig, ax = plt.subplots()
        ax.scatter(self.x[min_dot:], self.y[min_dot:], s = 0.01)
        plt.show()
        plt.close(fig)