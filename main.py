import turtle
import time
tt=turtle.Turtle()
turtle.bgcolor("black")
tt.pencolor('white')
#tt.hideturtle()
tt.penup()
tt.setx(-150)
tt.sety(-150)
tt.pendown()
tt.lt(90)
tt.speed(64)
for i in range(0,50):
 tt.rt(10)
 tt.fd(200)
 tt.rt(80)
 tt.fd(50-i)
 tt.rt(100)
 tt.fd(200)
 tt.rt(80)
 tt.fd(50-i)
 tt.rt(90)
tt.penup()
tt.fd(210)
tt.pendown()
tt.fd(2)
tt.rt(2)
tt.fd(1)
tt.rt(2)
tt.fd(3)
tt.rt(5)
tt.fd(2)
tt.rt(5)
tt.fd(6)
tt.rt(5)
tt.fd(4)
tt.rt(4)
tt.rt(20)
tt.fd(10)
tt.rt(4)
tt.fd(17)
tt.rt(4)
tt.fd(17)
tt.rt(2)
tt.fd(10)
tt.rt(4)
tt.fd(15)
tt.rt(6)
tt.fd(20)
tt.rt(8)
tt.fd(20)
tt.rt(10)
tt.fd(20)
tt.rt(10)
tt.fd(10)
tt.rt(10)
tt.fd(25)
tt.speed(2)
print('loop l')
for l in range(0,18):
 tt.rt(4)
 tt.fd(9)
turtle.done()