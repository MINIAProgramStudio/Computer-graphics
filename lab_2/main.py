import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import shape_handler

cube_shape = pd.DataFrame([
    [0,0,0],
    [0,0,1],
    [0,1,0],
    [0,1,1],
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1]
], columns = ['X','Y','Z'])
cube_shape = shape_handler.ShapeContainer3D(cube_shape)
cube_shape.draw()

cube_big = cube_shape.transform([
    [2,0,0,0],
    [0,2,0,0],
    [0,0,2,0]
])
cube_big.draw()