"""
This script demonstrates drawing a table, cake, and decorations using the Turtle graphics library.
Author: Aryaan Roy, Ashton Pinto
Date: September 22, 2023
"""
import turtle

#Global variables to store coordinates
xCor, yCor = 0, 0

def update_coordinates(z,f):
    global xCor, yCor
    xCor, yCor = z, f
   


def table(length,y,size,color):
    '''Drawing a table''' 
    turtle.up()
    turtle.goto(-length/2,y)
    turtle.down()
    # Fill the table with the specified color
    turtle.fillcolor(color)
    turtle.begin_fill()
    # Draw the base of table starting as rectangle
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length/size)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length/size)
    turtle.right(90)
    turtle.forward(length/2)
    turtle.end_fill()
    # Update global coordinates after drawing the table for later use
    z, f = turtle.pos()
    update_coordinates(z,f)
    turtle.backward(length/2)
    
    

def rectangle(length,color):
    ''' Drawing a rectangle'''
    turtle.up()
    turtle.down()
    #Draws a rectangle shape
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length/9)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length/9)

def legs(length,color):
    '''Drawing table legs'''
    turtle.fillcolor(color)
    turtle.begin_fill()
    #Draws the table's legs
    turtle.forward(10)
    rectangle(length,color)
    turtle.forward(length/5)
    rectangle(length,color)
    turtle.forward(length/2)
    rectangle(length,color)
    turtle.forward(length/5)
    rectangle(length,color)
    turtle.end_fill()

def cake_piece(length,color):
    '''Draws a piece of cake'''
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(-length/2,yCor)
    #Draws a section of cake
    turtle.forward(33.3)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(33.3)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(33.3)
    turtle.end_fill()

def candle(length,size,color):
    '''Draws a candle on the cake'''
    turtle.up()
    turtle.goto(-length/7,yCor)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.left(90)
    #Draws a rectangular candle
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length/size)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length/size)
    turtle.right(90)  
    turtle.end_fill()

def draw_circle(size,x,y):
    ''' Draws a circle '''
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    for i in range(4):
        turtle.circle(size)
        turtle.right(90)


def add_flame(size):
    '''Adds a small flame on top of candle'''
    turtle.pencolor("red")
    draw_circle(size, xCor, yCor + 34)
    draw_circle(size, xCor, yCor + 34)
    turtle.hideturtle()

def circle_deco(colour,radius,w,x,y,): #for a normal size cake (greater than size 65)
    '''Draws circle decorations for a big size cake'''
    for i in range(1):
        #Creates a circular design for a cake section
        turtle.color(colour)
        draw_circle(radius/3,xCor,yCor*y)
        draw_circle(radius/3,xCor+w,yCor*y)
        draw_circle(radius/3,xCor-w,yCor*y)
        draw_circle(radius/3,xCor+x,yCor*y)
        draw_circle(radius/3,xCor-x,yCor*y)
        turtle.up()
        turtle.goto(xCor, yCor)
        turtle.down()
        turtle.color("black")

def circle_deco2(colour,radius,w,y,): #for a smaller size cake (less than size 65)
    '''Draws circle decorations for a small size cake'''
    for i in range(1):
        #Creates a circular design for a cake section
        turtle.color(colour)
        draw_circle(radius/3,xCor,yCor*y)
        draw_circle(radius/3,xCor+w,yCor*y)
        draw_circle(radius/3,xCor-w,yCor*y)
        turtle.up()
        turtle.goto(xCor, yCor)
        turtle.down()
        turtle.color("black")

def draw_deco(radius,length,color): #for a big sized cake
    '''Draws the decorations on a big cake'''
    turtle.up()
    turtle.hideturtle()
    turtle.goto(0, 0)
    turtle.setheading(0)
    turtle.up()
    turtle.color("brown")
    table(length,20,4,color)
    turtle.down()
    circle_deco("red",radius/10,15,30,1.5)
    circle_deco("blue",radius/10,15,30,3.3)
    circle_deco("purple",radius/10,15,30,4.8)

def draw_deco2(radius,length,color): #for a smaller sized cake
    '''Draws the decorations on a small cake'''
    turtle.up()
    turtle.hideturtle()
    turtle.goto(0, 0)
    turtle.setheading(0)
    turtle.up()
    turtle.color("brown")
    table(length,20,4,color)
    turtle.down()
    circle_deco2("red",radius/10,15,1.5)
    circle_deco2("blue",radius/10,15,3.3)
    circle_deco2("purple",radius/10,15,4.8)


def cake(radius):
    '''Forms and draws the cake'''
    turtle.goto(xCor,yCor)
    turtle.left(90)
    #Draws the first cake section
    cake_piece(radius,"beige")
    z, f = turtle.pos()
    update_coordinates(z, f)
    turtle.goto(z,f)
    #Draws the second cake section
    cake_piece(radius,"pink")
    z, f = turtle.pos()
    update_coordinates(z, f)
    #Draws the final cake section
    cake_piece(radius,"beige")
    turtle.right(90)
    turtle.forward(radius/2)
    z, f = turtle.pos()
    update_coordinates(z, f)
    candle(30,3,"beige")
    add_flame(1.5)
    turtle.up()


def main():
    '''Main function to draw a table, legs, a cake, and decorations'''
    #asks user for length of table
    length = int(input("Please enter the length of one side of a table (between 10-150): "))
    #asks for color of table
    color = str(input("Please enter the color of the table: "))
    #asks for size/radius of cake
    radius = int(input("Please enter the size of the cake (between 30-150) Note that the cake size should be equal to or smaller than the table size:"))
    turtle.speed(40)
    turtle.bgcolor("lightblue")
    #draws the table
    table(length,20,4,color)
    #draws table legs
    legs(length,color)
    #draws cake
    cake(radius)
    #checks for cake size and draws decorations accordingly
    if radius < 65:
        draw_deco2(radius,length,color)
    else:
        draw_deco(radius,length,color)
    print("Your cake is loading... Happy Birthday!")
    print("Please close the drawing canvas window to exit.")
    turtle.done()

main()