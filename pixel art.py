import cv2
import turtle


# Binary Image

img = cv2.imread('./praticolortext.jpg', cv2.IMREAD_COLOR)

width = int(img.shape[1])
height = int(img.shape[0])

# Turtle Setup

my_screen = turtle.Screen()
my_screen.screensize(width, height)
my_screen.colormode(255)
my_screen.bgcolor('black')
my_pen = turtle.Turtle()
my_pen.color('white')
my_screen.tracer(128)
# Printing Loop

pixR, pixG, pixB = 0, 0, 0

for i in range(int(height/2), int(height/-2),  -1):
    my_pen.penup()
    my_pen.goto(-(width / 2), i)
    my_pen.pendown()

    for l in range(-int(width/2), int(width/2), 1):
        pix_width = int(l + (width/2))
        pix_height = int(height/2 - i)
        pixB = img[pix_height][pix_width][0]
        pixG = img[pix_height][pix_width][1]
        pixR = img[pix_height][pix_width][2]
        my_pen.pencolor(pixR, pixG, pixB)
        my_pen.forward(1)

turtle.done()
