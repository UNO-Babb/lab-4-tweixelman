#TurtleGraphics.py
#Name:Tim Weixelman
#Date: 2/16/2025
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
        
def drawPolygon(polygon, sides):
    for s in range(sides):
        polygon.forward(50)
        polygon.right(360/sides)

def fillCorner(marty, corner):
    drawSquare(marty, 100)
    
    if corner == 1:
        marty.begin_fill()
        drawSquare(marty, 50)
        marty.end_fill()
    elif corner == 2:
        marty.forward(50)
        marty.begin_fill()
        drawSquare(marty, 50)
        marty.end_fill()
    elif corner == 3: 
        marty.forward(50)
        marty.right(90)
        marty.forward(50)
        penup()
        marty.begin_fill()
        pendown()
        drawSquare(marty, 50)
        marty.end_fill()
    elif corner == 4:
        marty.forward(100)
        marty.right(90)
        marty.forward(50)
        marty.being_fill()
        drawSquare(marty, 50)
        marty.end_fill()
    def squaresInSquares(myTurtle, num):
        size = 150
        for i in range(num): 
            myTurtle.penup()
            myTurtle.goto(-size / 2,size / 2)
            myTurtle.pendown()
            drawSquare(myTurtle, size)
            size -= 20
            myTurtle.penup()
            myTurtle.goto(-size / 2,size / 2)
            myTurtle.pendown()
        
        
    
        


def main():
    myTurtle = turtle.Turtle()
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
