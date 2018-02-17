from graphics import *
import time

def bresenham_circle_algorithm():
    # w = GraphWin("Bresenham's Circle algorithm",1000,800)
    # try:
    #     w.getMouse()
    # except:
    #     pass
    centerx = 400
    centery = 200
    r = int(input("Enter radius : "))

    x = 0
    y = r
    d = 3-2*r

    win = GraphWin("Bresenham's Circle algorithm",1000,800)
    x_coordinate = Line(Point(centerx - 500, centery), Point(centerx + 500, centery))
    y_coordinate = Line(Point(centerx, centery - 500), Point(centerx, centery + 500))
    x_coordinate.draw(win)
    y_coordinate.draw(win)
    while(x<=y):

        win.plotPixel(x+centerx,y+centery)
        win.plotPixel(y+centerx,x+centery)
        win.plotPixel(-y+centerx,x+centery)
        win.plotPixel(-x+centerx,y+centery)
        win.plotPixel(-x+centerx,-y+centery)
        win.plotPixel(-y+centerx,-x+centery)
        win.plotPixel(y+centerx,-x+centery)
        win.plotPixel(x+centerx,-y+centery)
        time.sleep(.2)

        if(d<0):
            d = d+4*x+6
        else:
            d = d+4*(x-y)+10
            y = y-1
        x = x+1

    try:
        win.getMouse()
    except:
        pass

bresenham_circle_algorithm()