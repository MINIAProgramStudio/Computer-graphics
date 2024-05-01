import random
import matplotlib.pyplot as plt
import matplotlib.animation as anime
import math

class Fractal:
    def __init__(self, sets):
        self.sets = sets
        self.x = [0]
        self.y = [0]
        self.animation = {"counter": 0, "wait":0, "steps":0}
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

    def iterate_classical(self, times):
        for i in range(times):
            set_r = random.random()
            set_pos = -1
            while set_r > 0:
                set_pos += 1
                set_r -= self.sets[set_pos]["p"]

            set = self.sets[set_pos]
            self.x.append(self.x[-1] * set["r"] * math.cos(set["teta"]) - self.y[-1] * set["s"] * math.sin(set["fi"]) + set["e"])
            self.y.append(self.x[-2] * set["r"] * math.sin(set["teta"]) + self.y[-1] * set["s"] * math.cos(set["fi"]) + set["f"])

    def draw(self,min_dot = 0):
        fig, ax = plt.subplots()
        ax.scatter(self.x[min_dot:], self.y[min_dot:], s = 0.025)
        #plt.show()
        plt.close(fig)

    def animate(self, wait, steps):
        fig, ax = plt.subplots()
        x = []
        y = []
        def frame(frame):
            ax.clear()
            if wait != self.animation["wait"] or steps != self.animation["steps"] or frame == 0:
                self.animation["counter"] = 0
                self.animation["wait"] = wait
                self.animation["steps"] = steps
            window = len(self.x) // steps
            self.animation["counter"] += 1
            self.animation["counter"] %= steps
            x = self.x[:self.animation["counter"] * window]
            y = self.y[:self.animation["counter"] * window]
            ax.scatter(x,y,s = 0.025)
        an = anime.FuncAnimation(fig, frame, interval = wait,frames = steps)
        plt.show()
        plt.close(fig)


