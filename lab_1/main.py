import matplotlib
import pandas as pd
import shape_handler as sh

shape_oct = sh.ShapeContainer(shape=pd.DataFrame(
    [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2]], columns=['X','Y']
))

shape_gcode = sh.ShapeContainer(path="gcode.csv")
shape_oct.draw()