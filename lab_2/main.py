import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import shape_handler
# task 1
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

cube_small = cube_shape.transform([
    [0.5,0,0,0],
    [0,0.5,0,0],
    [0,0,0.5,0]
])
cube_small.draw()
# task 2
cube_big_mirrored_zero = cube_big.transform([
    [-1,0,0,0],
    [0,-1,0,0],
    [0,0,-1,0]
])
cube_big_mirrored_zero.draw()

cube_big_mirrored_X = cube_big.transform([
    [-1,0,0,0],
    [0,1,0,0],
    [0,0,1,0]
])
cube_big_mirrored_X.draw()
# task 4
