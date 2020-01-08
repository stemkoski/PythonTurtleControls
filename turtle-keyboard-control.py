# keyboard-based controls for the Python turtle package
# created by Lee Stemkoski (http://stemkoski.net)

from turtle import Turtle
from math import sqrt

def printHelp():
    print(  "\n",
            "========================================= \n",
            "             List of commands             \n",
            "========================================= \n",
            "    Up --- move turtle forward            \n",
            "  Down --- move turtle backward           \n",
            "  Left --- turn turtle left               \n",
            " Right --- turn turtle right              \n",
            "     C --- set pen Color                  \n",
            "     T --- set pen Thickness              \n",
            "     U --- toggle pen Up/down             \n",
            "     V --- toggle turtle Visible          \n",
            "     S --- set turtle Shape               \n",
            "     F --- set shape Fill color           \n",
            "     R --- Rescale turtle shape           \n",
            "     D --- Draw (stamp) turtle shape      \n",
            "     O --- move turtle back to Origin     \n",
            "     E --- Erase entire screen            \n",
            "     Z --- undo turtle action             \n",
            "     I --- print turtle Info              \n",
            "     H --- print Help menu                \n",  
            "========================================= \n" )
    
def printInfo():
    print(  "\n",
            "========================== \n",
            "    Turtle Information     \n",
            "========================== \n",
            "      X position:", round(leo.xcor(), 1),        "\n",
            "      Y position:", round(leo.ycor(), 1),        "\n",
            " heading (angle):", round(leo.heading(), 1),     "\n",
            " dist from (0,0):", round(leo.distance(0,0), 1), "\n",
            "       pen color:", leo.pencolor(),              "\n",
            "   pen thickness:", leo.pensize(),               "\n",
            "        pen down?", leo.isdown(),                "\n",
            "  turtle visible?", leo.isvisible(),             "\n",
            "    turtle shape:", leo.shape(),                 "\n",
            "shape fill color:", leo.fillcolor(),             "\n",
            "     shape scale:", leo.shapesize()[0],          "\n",
            "========================== \n" )

leo = Turtle()

# using fastest speed (0)
#   because otherwise when pressing keys simultaneously
#   non-glid aligned values could accumulate
leo.speed(0)

# easy-to-see initial configuration
leo.pencolor("black")
leo.pensize(3)
leo.fillcolor("gray")
leo.shapesize(2,2,2)

screen = leo.getscreen()
screen.bgcolor("#EEEEFF")
screen.listen()

printHelp()

# actions available to the user    
def action(keyName):

    # technical note:
    # this bit of code determines if turtle is moving diagonally,
    # and if so, scales movement to align line drawings better.
    if round( leo.heading() % 90 ) == 45:
        scale = sqrt(2)
    else:
        scale = 1
        
    if keyName == "Up":
        leo.forward(20 * scale)
    elif keyName == "Down":
        leo.backward(20 * scale)
    elif keyName == "Left":
        leo.left(45)
    elif keyName == "Right":
        leo.right(45)

    elif keyName == "i":
        printInfo()
    elif keyName == "h":
        printHelp()
    elif keyName == "z":
        leo.undo()
    elif keyName == "c":
        colorName = screen.textinput("Set Pen Color", "Enter a color name (red, yellow, etc.):")
        leo.pencolor(colorName)
        screen.listen()
    elif keyName == "t":
        penThickness = screen.numinput("Set Pen Thickness", "Enter a thickness for pen lines:")
        leo.pensize(penThickness)
        screen.listen()
    elif keyName == "s":
        shapeName = screen.textinput("Set Shape", "Enter a shape name (classic, arrow, circle, square, triangle, turtle):")
        leo.shape(shapeName)
        screen.listen()
    elif keyName == "f":
        colorName = screen.textinput("Set Shape Fill Color", "Enter a color name (red, yellow, etc.):")
        leo.fillcolor(colorName)
        screen.listen()
    elif keyName == "r":
        shapeScale = screen.numinput("Rescale Shape Size", "Enter a scale factor for the shape (1, 2, etc.):")
        leo.shapesize(shapeScale, shapeScale, shapeScale)
        screen.listen()
    elif keyName == "u":
        if leo.isdown():
            leo.penup()
        else:
            leo.pendown()
    elif keyName == "v":
        if leo.isvisible():
            leo.hideturtle()
        else:
            leo.showturtle()
    elif keyName == "d":
        leo.stamp()
    elif keyName == "o":
        leo.penup()
        leo.setposition(0,0)
        leo.setheading(0)
        leo.pendown()
    elif keyName == "e":
        leo.clear()
        
                 
# apply function f to input i (later)
def apply(f, i):
    return lambda : f(i)

keyNameList = ["Up", "Down", "Left", "Right",
               "i", "h", "z", "c", "t", "s", "f", "r", "u", "v", "d", "o", "e"]

# this approach is necessary because
#   onkeypress can only call a function with no arguments
#   (and this is better than writing dozens of functions)
for keyName in keyNameList:
    screen.onkeypress( apply(action, keyName), keyName )
    

