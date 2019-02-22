
# import everything from graphics
from graphics import *

# define a window
win = GraphWin('Window 1',600,600)

point = Point(300,300)
second_point = Point(200,250)
third_point = Point(410,250)
fourth_point = Point(350,400)

# creating a circle object
circle = Circle(point,250)
circle.setOutline('black')
circle.setFill('yellow')
# draw circle in the window
circle.draw(win)

# Mouth
mouth = Line(Point(240,375),fourth_point)
mouth.draw(win)

### Left Eye ###
lefteye = Circle(second_point,50)
lefteye.setOutline("black")
lefteye.setFill("black")
lefteye.draw(win)

### Right Eye ###
righteye = Circle(third_point,50)
righteye.setOutline("black")
righteye.setFill("black")
righteye.draw(win)

# ask for user mouse input
win.getMouse()
# close the window
win.close()

# ask for user input
#input("Press any key to exit...")
