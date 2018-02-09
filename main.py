import read_circle
import circle_draw
text = "Press 1 to draw line from text file\n" \
           "Press 2 to draw circle from text file\n" \
           "Press 3 to draw line using Bresenham's Line algorithm\n" \
           "Press 4 to draw circle using Bresenham's Circle algorithm\n" \
           "Press 0 to close the program \n "

while True:
    inpt = int(input(text))

    if inpt ==0:
        break
    elif inpt==2:
        read_circle.manipulate()
    elif inpt==4:
        circle_draw.main()


