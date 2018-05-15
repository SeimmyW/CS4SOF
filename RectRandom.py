from shapes import Triangle, Rectangle, Oval
import random

for i in range(100):
    r = Rectangle()
    r.set_width(random.randint(10,100))
    r.set_height(random.randint(10,100))
    r.set_x(random.randint(10, 500))
    r.set_y(random.randint(10, 500))
    col = random.randint(1, 6)
    if col == 1:
        r.set_color("red")
    elif col == 2:
        r.set_color("blue")
    elif col == 3:
        r.set_color("green")
    elif col == 4:
        r.set_color("purple")
    elif col == 5:
        r.set_color("orange")
    else:
        r.set_color("yellow")
    r.draw()
