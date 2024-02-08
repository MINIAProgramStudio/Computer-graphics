import matplotlib.pyplot as plt
import pandas as pd

class ShapeContainer:
    shape = None
    def center_point(self):
        min_x = min(self.shape.X)
        min_y = min(self.shape.Y)
        max_x = max(self.shape.X)
        max_y = min(self.shape.Y)
        return [(max_x+min_x)/2,(max_y+min_y)/2]

    def __init__(self, shape = None, path = None):
        if shape.empty and path:
            raise Exception("Only one parameter can be given")
        if not shape.empty^
            self.shape = shape
        if path:
            self.shape = pd.read_csv(path, delimiter="	")

    def draw(self):
        self.shape.plot(x = 'X', y = 'Y')
        plt.show()