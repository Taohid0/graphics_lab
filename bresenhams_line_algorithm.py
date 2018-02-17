from graphics import *
import time

def bresenham_line_algorithm():

    w = GraphWin("Bresenham's line algorithm",1000,800)
    # w.create_line(50,50,50,600)
    try:
        w.getMouse()
    except:
        pass

    x1, y1 = map(int,input("Starting point : ").split())
    x2, y2 = map(int,input("Ending point : ").split())
    x = x1
    y = y1
    dx = x2-x1
    dy = y2-y1
    dt = 2*(dy-dx)
    ds = 2*dy
    d = 2*dy-dx
    win = GraphWin("Bresenham's line algorithm", 1000, 600)
    win.plotPixel(x, y)

    while (x<x2):
        x = x+1

        if( d<0 ):
            d = d+ds
        else:
            y = y+1
            d = d+dt
        win.plotPixel(x, 600-y)
        time.sleep(.01)
        print(str(x) + " "+ str(y))

    try:
        win.getMouse()
    except:
        pass

bresenham_line_algorithm()