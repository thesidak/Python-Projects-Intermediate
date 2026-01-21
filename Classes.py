from turtle import *

screen=Screen()
class paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)

    def go_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)


class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.xmove= 10
        self.ymove=10
        self.movespeed=0.1

    def move(self):
        newx= self.xcor()+ self.xmove
        newy= self.ycor()+ self.ymove
        self.goto(newx,newy)

    def bounce(self):
        self.ymove *= -1

    def collision(self):
        if self.ycor()>280 or self.ycor()<-280:
            self.bounce()

    def bouncex(self):
        self.xmove *= -1
        self.movespeed *=0.9

    def resetposition(self):
        self.goto(0,0)
        self.movespeed = 0.1
        self.bouncex()


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore=0
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("Courier", 80, "normal"))

    def lpoint(self):
        self.lscore+=1
        self.updatescore()
    def rpoint(self):
        self.rscore+=1
        self.updatescore()
