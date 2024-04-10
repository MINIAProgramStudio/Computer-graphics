import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import shape_handler

# task 2
print("task 2")
cube_shape = pd.DataFrame([
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1]
], columns=['X', 'Y', 'Z'])
cube_shape = shape_handler.ShapeContainer3D(cube_shape)
cube_shape.draw("Початковий куб")

cube_big = cube_shape.transform([
    [2, 0, 0, 0],
    [0, 2, 0, 0],
    [0, 0, 2, 0]
    #четвертий рядок з 0 0 0 1 може бути записаний, але не впливає на обчислення, тож не буде використовуватись
])
cube_big.draw("Збільшений у 2 рази куб")

cube_small = cube_shape.transform([
    [0.5, 0, 0, 0],
    [0, 0.5, 0, 0],
    [0, 0, 0.5, 0]
])
cube_small.draw("Зменшений у 2 рази куб")
# task 3 //////////////////////////////////////////////////////////////////////////////////////////////////// task 3
print("task 3")
cube_big_mirrored_zero = cube_big.transform([
    [-1, 0, 0, 0],
    [0, -1, 0, 0],
    [0, 0, -1, 0]
])
cube_big_mirrored_zero.draw("Куб симетрично відображений відносно початку координат")

cube_big_mirrored_YOZ = cube_big.transform([
    [-1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0]
])
cube_big_mirrored_YOZ.draw("Куб симетрично відображений відносно YOZ")
# task 4 /////////////////////////////////////////////////////////////////////////////////////////////////// task 4
print("task 4")
line_dot = [1, 2, 3]
line_vector = [2, 1, 3]
fi = 3.1415 / 3

cube_moved_to_center = cube_shape.transform([
    [1, 0, 0, -line_dot[0]],
    [0, 1, 0, -line_dot[1]],
    [0, 0, 1, -line_dot[2]]
])
cube_moved_to_center.draw("Початок координат зміщено так, щоб він належав прямій")

divide_by = math.sqrt(line_vector[1] ** 2 + line_vector[2] ** 2)
RX = [
    [1, 0, 0, 0],
    [0, line_vector[2] / divide_by, line_vector[1] / divide_by, 0],
    [0, -line_vector[1] / divide_by, line_vector[2] / divide_by, 0]
]

cube_rotated_ox = cube_moved_to_center.transform(RX)
cube_rotated_ox.draw("Куб повернений навколо OX")

line_vector_shape = shape_handler.ShapeContainer3D(
    pd.DataFrame([[line_vector[0], line_vector[1], line_vector[2]]], columns=['X', 'Y', 'Z']))
line_vector_shape = line_vector_shape.transform(RX)
line_vector_new = [line_vector_shape.shape.X[0], line_vector_shape.shape.Y[0], line_vector_shape.shape.Z[0]]
divide_by_2 = math.sqrt(line_vector_new[0] ** 2 + line_vector_new[2] ** 2)
RY = [
    [line_vector_new[0] / divide_by_2, 0, line_vector_new[2] / divide_by_2, 0],
    [0, 1, 0, 0],
    [-line_vector_new[2] / divide_by_2, 0, line_vector_new[0] / divide_by_2, 0]
]

cube_rotated_oy = cube_rotated_ox.transform(RY)
cube_rotated_oy.draw("Куб повернений навколо OY")

RZ = [
    [math.cos(fi), -math.sin(fi), 0, 0],
    [math.sin(fi), math.cos(fi), 0, 0],
    [0, 0, 1, 0]
]

cube_rotated_oz = cube_rotated_oy.transform(RZ)
cube_rotated_oz.draw("Куб повернений навколо прямої (що співпадає з OZ)")

RY = [
    [line_vector_new[0] / divide_by_2, 0, -line_vector_new[2] / divide_by_2, 0],
    [0, 1, 0, 0],
    [line_vector_new[2] / divide_by_2, 0, line_vector_new[0] / divide_by_2, 0]
]

cube_rerotated_oy = cube_rotated_oz.transform(RY)
cube_rerotated_oy.draw("Поворот в попереднє положення навколо OY")

RX = [
    [1, 0, 0, 0],
    [0, line_vector[2] / divide_by, -line_vector[1] / divide_by, 0],
    [0, line_vector[1] / divide_by, line_vector[2] / divide_by, 0]
]

cube_rerotated_ox = cube_rerotated_oy.transform(RX)
cube_rerotated_ox.draw("Поворот в попереднє положення навколо OX")

cube_rotated_line = cube_rerotated_ox.transform([
    [1, 0, 0, line_dot[0]],
    [0, 1, 0, line_dot[1]],
    [0, 0, 1, line_dot[2]]
])
cube_rotated_line.draw("Зміщення початку координат в початкове положення")

# task 5 /////////////////////////////////////////////////////////////////////////////////////////////////// task 5
print("task 5")
point_1 = [1, 1, 2]
point_2 = [3, 5, 8]
point_3 = [13, 21, 34]
A = (point_2[1] - point_1[1]) * (point_3[2] - point_1[2]) - (point_2[2] - point_1[2]) * (point_3[1] - point_1[1])
B = -((point_2[0] - point_1[0]) * (point_3[2] - point_1[2]) - (point_2[2] - point_1[2]) * (point_3[0] - point_1[0]))
C = (point_2[0] - point_1[0]) * (point_3[1] - point_1[1]) - (point_2[1] - point_1[1]) * (point_3[0] - point_1[0])
D = -point_1[0] * A - point_1[1] * B - point_1[2] * C
divide_by = math.sqrt(A ** 2 + B ** 2 + C ** 2)
vector = [A / divide_by, B / divide_by, C / divide_by]
print(vector)
print(D)

cube_moved = cube_shape.transform([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, D / C]
])
cube_moved.draw("Зміщення початку координат так, щоб він належав площині")

cos_fi = A / math.sqrt(A ** 2 + B ** 2)
sin_fi = B / math.sqrt(A ** 2 + B ** 2)

cube_rotated_oz = cube_moved.transform([
    [cos_fi, sin_fi, 0, 0],
    [-sin_fi, cos_fi, 0, 0],
    [0, 0, 1, 0]
])
cube_rotated_oz.draw("Куб повернений навколо OZ")

cos_ksi = C / divide_by
sin_ksi = math.sqrt(A ** 2 + B ** 2) / divide_by

cube_rotated_oy = cube_rotated_oz.transform([
    [cos_ksi, 0, -sin_ksi, 0],
    [0, 1, 0, 0],
    [sin_ksi, 0, cos_ksi, 0]
])
cube_rerotated_oy.draw("Куб повернений навколо OY")

cube_inverted = cube_rotated_oy.transform([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, -1, 0]
])
cube_inverted.draw("Куб симетрично відображений відносно XOY")

cube_rerotated_oy = cube_inverted.transform([
    [cos_ksi, 0, sin_ksi, 0],
    [0, 1, 0, 0],
    [-sin_ksi, 0, cos_ksi, 0]
])
cube_rerotated_oy.draw("Повернення в попереднє положення навколо OY")

cube_rerotated_oz = cube_rerotated_oy.transform([
    [cos_fi, -sin_fi, 0, 0],
    [sin_fi, cos_fi, 0, 0],
    [0, 0, 1, 0]
])
cube_rerotated_oz.draw("Поверенення в попереднє положення навколо OY")

cube_inverted_plane = cube_rerotated_oz.transform([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, -D / C]
])
cube_inverted_plane.draw("Поверення початку координат в початкове положення")

# task 6/7 ////////////////////////////////////////////////////////////////////////////////////////////////task 6/7
print("task 6/7")
first_point = cube_shape.shape.values.tolist()[0]
distance = (A * first_point[0] + B * first_point[1] + C * first_point[2] + D) / divide_by
first_point_desired_position = [first_point[0] + distance * vector[0], first_point[1] + distance * vector[1],
                                first_point[2] + distance * vector[2]]
cube_moved_to_center = cube_shape.transform([
    [1, 0, 0, -first_point[0]],
    [0, 1, 0, -first_point[1]],
    [0, 0, 1, -first_point[2]]
])
cube_moved_to_center.draw("Переміщення початку координат так, щоб він належав площині")

divide_by_3 = math.sqrt(A ** 2 + C ** 2)
cos_psi = A / divide_by_3
sin_psi = C / divide_by_3
print([cos_psi, sin_psi])
cube_rotated_oy = cube_moved_to_center.transform([
    [cos_psi, 0, sin_psi, 0],
    [0, 1, 0, 0],
    [-sin_psi, 0, cos_psi,0]
])
cube_rotated_oy.draw("Куб повернений навколо OY")

cos_fi = B / divide_by
sin_fi = divide_by_3 / divide_by
print([cos_fi,sin_fi])
cube_rotated_oz = cube_moved_to_center.transform([
    [cos_fi, sin_fi, 0, 0],
    [-sin_fi, cos_fi, 0, 0],
    [0, 0, 1, 0]
])
cube_rotated_oz.draw("Куб повернений навколо OZ")

cube_mirrored_xoz = cube_rotated_oz.transform([
    [1,0,0,0],
    [0,-1,0,0],
    [0,0,1,0]
])
cube_mirrored_xoz.draw("Куб симетрично відображений відносно XOZ")

cube_rerotated_oz = cube_moved_to_center.transform([
    [cos_fi, -sin_fi, 0, 0],
    [sin_fi, cos_fi, 0, 0],
    [0, 0, 1, 0]
])
cube_rerotated_oz.draw("Повернення в попереднє положення навколо OZ")

cube_rerotated_oy = cube_moved_to_center.transform([
    [cos_psi, 0, -sin_psi, 0],
    [0, 1, 0, 0],
    [sin_psi, 0, cos_psi, 0]
])
cube_rerotated_oy.draw("Повернення в попереднє положення навколо OY")

cube_alternatively_inverted_plane = cube_rerotated_oy.transform([
    [1, 0, 0, first_point[0]],
    [0, 1, 0, first_point[1]],
    [0, 0, 1, first_point[2]]
])
cube_alternatively_inverted_plane.draw("Повернення початку координат в початкове положення")

# task 8 /////////////////////////////////////////////////////////////////////////////////////////////////////// task 8
print("task 8")
points_list = cube_shape.shape.values.tolist()
for i in range(len(points_list)):
    offset = (A*points_list[i][0] + B*points_list[i][1]+C*points_list[i][2]+D)/math.sqrt(A**2+B**2+C**2)
    points_list[i][0] -= 2*offset*vector[0]
    points_list[i][1] -= 2 * offset * vector[1]
    points_list[i][2] -= 2 * offset * vector[2]

cube_alg_inverted = shape_handler.ShapeContainer3D(pd.DataFrame(points_list, columns=['X', 'Y', 'Z']))
cube_alg_inverted.draw("Куб симетрично відображений відносно площини методами аналітичної геометрії")

print(cube_inverted_plane.shape)
print(cube_alg_inverted.shape)
print((abs(cube_inverted_plane.shape - cube_alg_inverted.shape)<0.001).all())

# task 10 /////////////////////////////////////////////////////////////////////////////////////////////////// task 10
print("task 10")
cube_moved = cube_shape.transform([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, D / C]
])
cube_moved.draw("Переміщення початку координат так щоб він належав площині")

cos_fi = A / math.sqrt(A ** 2 + B ** 2)
sin_fi = B / math.sqrt(A ** 2 + B ** 2)

cube_rotated_oz = cube_moved.transform([
    [cos_fi, sin_fi, 0, 0],
    [-sin_fi, cos_fi, 0, 0],
    [0, 0, 1, 0]
])
cube_rotated_oz.draw("Куб повернений навколо OZ")

cos_ksi = C / divide_by
sin_ksi = math.sqrt(A ** 2 + B ** 2) / divide_by

cube_rotated_oy = cube_rotated_oz.transform([
    [cos_ksi, 0, -sin_ksi, 0],
    [0, 1, 0, 0],
    [sin_ksi, 0, cos_ksi, 0]
])
cube_rerotated_oy.draw("Куб повернений навколо OY")

cube_flat = cube_rotated_oy.transform([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
])
cube_flat.draw("Проєкція куба на XOY (Z=0)")

cube_rerotated_oy = cube_inverted.transform([
    [cos_ksi, 0, sin_ksi, 0],
    [0, 1, 0, 0],
    [-sin_ksi, 0, cos_ksi, 0]
])
cube_rerotated_oy.draw("Поворот в попереднє положення навколо OY")

cube_rerotated_oz = cube_rerotated_oy.transform([
    [cos_fi, -sin_fi, 0, 0],
    [sin_fi, cos_fi, 0, 0],
    [0, 0, 1, 0]
])
cube_rerotated_oz.draw("Поворот в попереднє положення OZ")

cube_flat_plane = cube_rerotated_oz.transform([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, -D / C]
])
cube_inverted_plane.draw("Повернення початку координат в початкове положення")