import cv2
import turtle


# Binary Image

img = cv2.imread('./image.jpg',0)
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
width = int(img.shape[1])
height = int(img.shape[0])
print(bw_img)
print(img)

# Turtle Setup

my_screen = turtle.Screen()
my_screen.screensize(width, height)
my_screen.bgcolor('black')
my_pen = turtle.Turtle()
my_pen.color('white')
my_screen.tracer(16)
#my_pen.hideturtle()
my_pen.pencolor("white")
# Printing Loop

for i in range(int(height/2), int(height/-2),  -1):
    my_pen.penup()
    my_pen.goto(-(width / 2), i)

    for l in range(-int(width/2), int(width/2), 1):
        pix_width = int(l + (width/2))
        pix_height = int(height/2 - i)
        if bw_img[pix_height, pix_width] == 0:
            my_pen.pendown()
            my_pen.forward(1)
        else:
            my_pen.penup()
            my_pen.forward(1)
    my_screen.update()

turtle.done()
