import matplotlib
import pandas as pd
import shape_handler as sh
import math

shape_oct = sh.ShapeContainer(shape=pd.DataFrame(
    [[1,3],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2],[1,3]], columns=['X','Y']
))

shape_gcode = sh.ShapeContainer(pd.read_csv("gcode.csv", delimiter=';'))
print(shape_gcode.shape.head())
shape_oct.draw()

#task2
small_oct = shape_oct.transform([
    [1/1.5,0,0],
    [0, 1/1.5, 0],
    [0,0,1]
])
small_oct.draw()

#task3
mirrored_oct = small_oct.transform([
    [-1,0,0],
    [0,-1,0],
    [0,0,1]
])
mirrored_oct.draw()

#task4
x1 = 1
y1 = 2
x2 = -1
y2 = 3

#move point 1 to 0
x0 = 0
y0 = 0
x2 = x2-x1
y2 = y2-y1
shape_oct.draw()
moved_oct = shape_oct.transform([
    [1,0,-x1],
    [0,1,-y1],
    [0,0,1]
])
moved_oct.draw()
#turn line to X
sinus = y2/math.sqrt(x2**2+y2**2)
angle = math.asin(sinus)
turned_oct = moved_oct.transform([
    [math.cos(angle), -math.sin(angle), 0],
    [math.sin(angle), math.cos(angle),0],
    [0,0,1]
])
turned_oct.draw()
#mirror oct around X
mirrored_oct_line = turned_oct.transform([
    [1,0,0],
    [0,-1,0],
    [0,0,1]
])
mirrored_oct_line.draw()
#unturn
unturned_oct = mirrored_oct_line.transform([
    [math.cos(angle), math.sin(angle), 0],
    [-math.sin(angle), math.cos(angle),0],
    [0,0,1]
])
unturned_oct.draw()
#unmove
final_oct = unturned_oct.transform([
    [1,0,x1],
    [0,1,y1],
    [0,0,1]
])
final_oct.draw()

#task 6
#task2
shape_gcode.draw()
small_gcode = shape_gcode.transform([
    [1/1.5,0,0],
    [0, 1/1.5, 0],
    [0,0,1]
])
small_gcode.draw()

#task3
mirrored_gcode = small_gcode.transform([
    [-1,0,0],
    [0,-1,0],
    [0,0,1]
])
mirrored_gcode.draw()

#task4
x1 = 1
y1 = 2
x2 = -1
y2 = 3

#move point 1 to 0
x0 = 0
y0 = 0
x2 = x2-x1
y2 = y2-y1
shape_gcode.draw()
moved_gcode = shape_gcode.transform([
    [1,0,-x1],
    [0,1,-y1],
    [0,0,1]
])
moved_gcode.draw()
#turn line to X
sinus = y2/math.sqrt(x2**2+y2**2)
angle = math.asin(sinus)
turned_gcode = moved_gcode.transform([
    [math.cos(angle), -math.sin(angle), 0],
    [math.sin(angle), math.cos(angle),0],
    [0,0,1]
])
turned_gcode.draw()
#mirror oct around X
mirrored_gcode_line = turned_gcode.transform([
    [1,0,0],
    [0,-1,0],
    [0,0,1]
])
mirrored_gcode_line.draw()
#unturn
unturned_gcode = mirrored_gcode_line.transform([
    [math.cos(angle), math.sin(angle), 0],
    [-math.sin(angle), math.cos(angle),0],
    [0,0,1]
])
unturned_gcode.draw()
#unmove
final_gcode = unturned_gcode.transform([
    [1,0,x1],
    [0,1,y1],
    [0,0,1]
])
final_gcode.draw()