from graphics import *
import time

def manipulate():
    filename = input("Enter filename : ")
    file = open(filename+".txt","r")

    values = file.read()

    values= values.split("\n")

    xvalue =values[0].split(" ")
    yvalue = values[1].split(" ")
    cx =int(values[2])
    cy = int(values[3])


    win = GraphWin("line from file",width=800,height=1000)

    x_coordinate = Line(Point(cx-500,cy),Point(cx+500,cy))
    y_coordinate= Line(Point(cx,cy-500),Point(cx,cy+500))

    x_coordinate.draw(win)
    y_coordinate.draw(win)
    xvalue.remove("")
    yvalue.remove("")

    for i in range(len(xvalue)):
        point = Point(int(xvalue[i]),int(yvalue[i]))
        point.draw(win)
        time.sleep(.002)



    win.getMouse()
    win.close()

if __name__=="__main__":
    manipulate()