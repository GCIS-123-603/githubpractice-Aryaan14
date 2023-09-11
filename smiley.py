import turtle

def draw_circle(x,y,r,z):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.fillcolor(z)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

def main():
    draw_circle(100,100,40,"red")
    input("enter to enter")

main()