import handler as h

square = h.Rectangle(0,0,0,1,1)
rectangle_1 = h.Rectangle(-0.5,0.5,-35, 1, 0.5)
rectangle_2 = h.Rectangle(0.5,0.5,30,1.5,0.5)

generator = h.RectangleGroup(0,0,0,1,1, [
    square,
    rectangle_1,
    rectangle_2
])
square_group = h.RectangleGroup(0,0,0,1,1, [
    square
])

square_group.draw(step = 100)
input()
for i in range(5):
    square_group.iterate(generator)
    square_group.draw(step = 100)
    input()