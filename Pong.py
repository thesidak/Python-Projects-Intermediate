from turtle import *

from pygame.examples.stars import move_stars

from classes import *
import time
screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
p1=paddle()
p1.goto(350,0)
p2=paddle()
p2.goto(-350,0)
b1=ball()
scoreboard=scoreboard()
screen.listen()
screen.onkeypress(p1.go_down, "Down")
screen.onkeypress(p1.go_up, "Up")
screen.onkeypress(p2.go_down, "s")
screen.onkeypress(p2.go_up, "w")
p1.go_up()
p1.go_down()


gameon=True
while gameon:
    time.sleep(b1.movespeed)
    screen.update()
    b1.move()
    b1.collision()
    if (b1.distance(p1)< 40 and b1.xcor() >300 or b1.distance(p2) < 40 and b1.xcor() < -300) :
        b1.bouncex()

    if b1.xcor() > 380:
        b1.resetposition()
        scoreboard.lpoint()

    if b1.xcor() < -380:
        b1.resetposition()
        scoreboard.rpoint()
screen.exitonclick()
