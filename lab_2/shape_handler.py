import matplotlib.pyplot as plt
import pandas as pd

class ShapeContainer:
    shape = None
    def center_point(self):
        min_x = min(self.shape.X)
        min_y = min(self.shape.Y)
        max_x = max(self.shape.X)
        max_y = max(self.shape.Y)
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

class ShapeContainer3D:
    shape = None
    def center_point(self):
        min_x = min(self.shape.X)
        min_y = min(self.shape.Y)
        max_x = max(self.shape.X)
        max_y = max(self.shape.Y)
        max_z = max(self.shape.Z)
        min_z = min(self.shape.Z)
        return [(max_x+min_x)/2,(max_y+min_y)/2,(max_z+min_z)/2]

    def __init__(self, shape = None):
        self.shape = shape

    def draw(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Додавання scatter plot
        ax.scatter(self.shape.X, self.shape.Y, self.shape.Z, c='r', marker='o')

        # Налаштування міток осей
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Показати графік
        plt.show()

    def transform(self, matrix):
        return ShapeContainer3D(pd.DataFrame([[float(row[0])*matrix[0][0]+float(row[1])*matrix[0][1]+float(row[2])*matrix[0][2]+matrix[0][3],
                                             float(row[0])*matrix[1][0]+float(row[1])*matrix[1][1]+float(row[2])*matrix[1][2]+matrix[1][3],
                                             float(row[0])*matrix[2][0]+float(row[1])*matrix[2][1]+float(row[2])*matrix[2][2]+matrix[2][3]]
                                            for row in self.shape.values.tolist()], columns=['X','Y','Z']))