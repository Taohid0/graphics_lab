from graphics import *
import matplotlib.pyplot as plot
import time

def main():
    cx,cy = map(int,input("Enter coordinate of center : ").split())
    x_coordinate = Line(Point(cx-500,cy),Point(cx+500,cy))
    y_coordinate= Line(Point(cx,cy-500),Point(cx,cy+500))

    r = int(input("Enter radius of circle : "))
    filename = input("Enter filename : ")
    x = 0
    y = r
    d =3-2*r
    win = GraphWin("Circle", width=800, height=1000)
    xvalues = list()
    yvalues = list()

    while(x<=y):
        point = Point(x+cx,y+cy)
        xvalues.append(x+cx)
        yvalues.append(y+cy)
        point.draw(win)

        point = Point(y+cx,x+cy)
        xvalues.append(y+cx)
        yvalues.append(x+cy)
        point.draw(win)

        point = Point(-y+cx,x+cy)
        xvalues.append(-y+cx)
        yvalues.append(x+cy)
        point.draw(win)

        point =Point(-x+cx,y+cy)
        xvalues.append(-x+cx)
        yvalues.append(y+cy)
        point.draw(win)

        point = Point(-x+cx,-y+cy)
        xvalues.append(-x+cx)
        yvalues.append(-y+cy)
        point.draw(win)

        point =Point(-y+cx,-x+cy)
        xvalues.append(-y+cx)
        yvalues.append(-x+cy)
        point.draw(win)

        point = Point(y+cx,-x+cy)
        xvalues.append(y+cx)
        yvalues.append(-x+cy)
        point.draw(win)

        point = Point(x+cx,-y+cy)
        xvalues.append(x+cx)
        yvalues.append(-y+cy)
        point.draw(win)
        time.sleep(.003)

        if d<0:
            d = d+4*x+6
        else:
            d = d+4*(x-y)+10
            y = y-1
        x = x+1

    x_coordinate.draw(win)
    y_coordinate.draw(win)
    file = open(filename+".txt","w")
    for i in xvalues:
        file.write(str(i)+" ")
    file.write("\n")
    for i in yvalues:
        file.write(str(i)+" ")
    file.write("\n")
    file.write(str(cx))
    file.write("\n")
    file.write(str(cy))

    file.close()
    win.getMouse()
    win.close()

if __name__=="__main__":
    main()