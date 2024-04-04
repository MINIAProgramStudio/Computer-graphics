import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import shape_handler
# task 2
print("task 2")
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
# task 3
print("task 3")
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
print("task 4")
line_dot = [0,0,0]
line_vector = [2,1,3]
fi = 3.1415/3

cube_moved_to_center = cube_shape.transform([
    [1,0,0,-line_dot[0]],
    [0,1,0,-line_dot[1]],
    [0,0,1,-line_dot[2]]
])
cube_moved_to_center.draw()

divide_by = math.sqrt(line_vector[1]**2+line_vector[2]**2)
RX = [
    [1,0,0,0],
    [0,line_vector[2]/divide_by,line_vector[1]/divide_by,0],
    [0,-line_vector[1]/divide_by, line_vector[2]/divide_by,0]
]

cube_rotated_ox = cube_moved_to_center.transform(RX)
cube_rotated_ox.draw()

line_vector_shape = shape_handler.ShapeContainer3D(pd.DataFrame([[line_vector[0],line_vector[1],line_vector[2]]], columns = ['X','Y','Z']))
line_vector_shape = line_vector_shape.transform(RX)
line_vector_new = [line_vector_shape.shape.X[0],line_vector_shape.shape.Y[0],line_vector_shape.shape.Z[0]]
divide_by_2 = math.sqrt(line_vector_new[0]**2+line_vector_new[2]**2)
RY = [
    [line_vector_new[0]/divide_by_2,0,line_vector_new[2]/divide_by_2,0],
    [0,1,0,0],
    [-line_vector_new[2]/divide_by_2,0,line_vector_new[0]/divide_by_2,0]
]

cube_rotated_oy = cube_rotated_ox.transform(RY)
cube_rotated_oy.draw()

RZ = [
    [math.cos(fi),-math.sin(fi),0,0],
    [math.sin(fi),math.cos(fi),0,0],
    [0,0,1,0]
]

cube_rotated_oz = cube_rotated_oy.transform(RZ)
cube_rotated_oz.draw()

RY = [
    [line_vector_new[0]/divide_by_2,0,-line_vector_new[2]/divide_by_2,0],
    [0,1,0,0],
    [line_vector_new[2]/divide_by_2,0,line_vector_new[0]/divide_by_2,0]
]

cube_rerotated_oy = cube_rotated_oz.transform(RY)
cube_rerotated_oy.draw()

RX = [
    [1,0,0,0],
    [0,line_vector[2]/divide_by,-line_vector[1]/divide_by,0],
    [0,line_vector[1]/divide_by, line_vector[2]/divide_by,0]
]

cube_rerotated_ox = cube_rerotated_oy.transform(RX)
cube_rerotated_ox.draw()

cube_rotated_line = cube_rerotated_ox.transform([
    [1,0,0,line_dot[0]],
    [0,1,0,line_dot[1]],
    [0,0,1,line_dot[2]]
])
cube_rotated_line.draw()

#task 5
print("task 5")
point_1 = [1,1,2]
point_2 = [3,5,8]
point_3 = [13,21,29]
A = (point_2[1]-point_1[1])*(point_3[2]-point_1[2]) - (point_2[2]-point_1[2])*(point_3[1]-point_1[1])
B = -((point_2[0]-point_1[0])*(point_3[2]-point_1[2]) - (point_2[2]-point_1[2])*(point_3[0]-point_1[0]))
C = (point_2[0]-point_1[0])*(point_3[1]-point_1[1]) - (point_2[1]-point_1[1])*(point_3[0]-point_1[0])
D = -point_1[0]*A - point_1[1]*B - point_1[2]*C
divide_by = math.sqrt(A**2 + B**2 + C**2)
vector = [A/divide_by, B/divide_by, C/divide_by]

cube_moved = cube_shape.transform([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1, D/C]
])
cube_moved.draw()

cos_fi = A/math.sqrt(A**2+B**2)
sin_fi = B/math.sqrt(A**2+B**2)

cube_rotated_oz = cube_moved.transform([
    [cos_fi, sin_fi,0,0],
    [-sin_fi, cos_fi,0,0],
    [0,0,1,0]
])
cube_rotated_oz.draw()

cos_ksi = C/divide_by
sin_ksi = math.sqrt(A**2+B**2)/divide_by

cube_rotated_oy = cube_rotated_oz.transform([
    [cos_ksi,0,-sin_ksi,0],
    [0,1,0,0],
    [sin_ksi, 0, cos_ksi,0]
])
cube_rerotated_oy.draw()

cube_inverted = cube_rotated_oy.transform([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,-1,0]
])
cube_inverted.draw()

cube_rerotated_oy = cube_inverted.transform([
    [cos_ksi,0,sin_ksi,0],
    [0,1,0,0],
    [-sin_ksi, 0, cos_ksi,0]
])
cube_rerotated_oy.draw()

cube_rerotated_oz = cube_rerotated_oy.transform([
    [cos_fi, -sin_fi,0,0],
    [sin_fi, cos_fi,0,0],
    [0,0,1,0]
])
cube_rerotated_oz.draw()

cube_inverted_plane = cube_rerotated_oz.transform([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1, -D/C]
])
cube_inverted_plane.draw()