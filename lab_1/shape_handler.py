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

    def __init__(self, shape = None):
        self.shape = shape

    def draw(self):
        self.shape.plot(x = 'X', y = 'Y')
        plt.show()

    def transform(self, matrix):
        return ShapeContainer(pd.DataFrame([[float(row[0])*matrix[0][0]+float(row[1])*matrix[0][1]+matrix[0][2],
                                             float(row[0])*matrix[1][0]+float(row[1])*matrix[1][1]+matrix[1][2]]
                                            for row in self.shape.values.tolist()], columns=['X','Y']))