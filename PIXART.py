from turtle import Screen, Turtle
import os
# Change the current working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))


"""
This program demonstrates drawing from strings in a file, drawing from user input, and drawing a checkerboard.
Author: Aryaan Roy, Ashton Pinto
Date: October 17, 2023
"""

PIXEL_SIZE = 30
CURSOR_SIZE = 20

# Initializing list to store the pixels
PIXELS = []

# For returning True/False depending on user input validation
check = 0
# Dictionary to assign strings to their colours
# STEP 3 
COLORS = {
    'B': 'blue',
    '0': 'black',
    '4': 'orange',
    'R': 'red',
    'T': 'brown',
    '1': 'white',
    '3': 'yellow',
    '2': "red",
    '7': "sienna",
    '8': "tan",
    '6': "yellowgreen",
    '5': "green",
    'A': "gray",
    '9': "darkgray",
}

#STEP 4 in Activity2 Document
def drawrainbow(x):
    """Appends  characters/sequence to the PIXELS list for drawing."""
    global PIXELS
    draw = '01A753421'
    if x == "@":
        PIXELS.append(draw)
    else:
        PIXELS.append(x)
    return PIXELS

def startrainbow():
    """Function to initialize drawing a simple coloured row"""
    draw = input("Please enter ! to draw row (Step 4)")
    if draw == "!":
        drawrainbow("@")
        print("True")
    else:
        print("False")

#STEP 5 in Activity2 Document
def drawings_py():
        """Allows the user to input a sequence of characters for drawing and adds them to PIXELS list.
        The input should consist of valid characters from 0-9.
        If the input is '!', it ends the loop and starts drawing using collected user input."""
        global PIXELS
        global check
        while True:
            text1 = input("Please enter a variation of 0123456789 THEN ENTER ! TO DRAW.... OR JUST ENTER '@' TO DRAW A SIMPLE COLOURED ROW: ")
            if text1 == "!":
                check += 1
                break
            if text1 == "@":
                startrainbow()
                break

            elif not text1.isdigit() and  len(text1) > 1:
                print("False")
                break
            drawrainbow(text1)
            print("Enter more or submit with '!': ")
        return PIXELS


def textdraw():
    """Asks the user to input a filename, reads the content of the file, and returns the contents as a list of rows. """
    file_name = input("Please enter the name of the file (in the same folder, without extension .txt.... e.g \"drawing01\" \"drawing02\" etc...): ")
    file_name += ".txt"

    with open(file_name, 'r') as file:
        PIXELS = [line.strip() for line in file.readlines()]
        return PIXELS

def drawcheckers(): #step 2 in Activity2 document
    """Reads the content of "checkers.txt" file and returns the contents as a list of rows, drawing a checkerboard. STEP 2 in Activity2 DOCUMENT."""
    with open("checkers.txt", 'r') as file:
        PIXELS = [line.strip() for line in file.readlines()]
        return PIXELS

#User input for choosing what they would like to do
print("NOTE!: must extract zip folder to have draw file feature work")
choice = input("Enter '1' to draw from a text file. '2' to draw a simple checker board. '3' to draw your own rows: ")


if choice == '1':
    PIXELS = textdraw()
elif choice == '2':
    PIXELS = drawcheckers()
elif choice == '3':
    PIXELS = drawings_py()
else:
    print("Invalid choice.")


try: 
    WIDTH, HEIGHT = len(PIXELS[0]), len(PIXELS)
    print(WIDTH)
    print(HEIGHT)

    screen = Screen()
    screen.setup((WIDTH + 3) * PIXEL_SIZE, (HEIGHT + 3) * PIXEL_SIZE)
    screen.tracer(True)


    turtle = Turtle()
    turtle.speed(1000)
    turtle.hideturtle()
    turtle.shape('square')
    turtle.shapesize(PIXEL_SIZE / CURSOR_SIZE)
    turtle.penup()

    x0 = -WIDTH/2 * PIXEL_SIZE
    y0 = HEIGHT/2 * PIXEL_SIZE

    for i, row in enumerate(PIXELS):
        turtle.setposition(x0, y0 - i * PIXEL_SIZE)

        for pixel in row:
            turtle.color("black",COLORS[pixel])
            turtle.stamp()
            turtle.forward(PIXEL_SIZE)

    if check == 1:
        print("True")

    screen.tracer(True)
    screen.exitonclick()

except IndexError:
    print("")
