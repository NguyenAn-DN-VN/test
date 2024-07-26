from turtle import Turtle
STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)
    def lv_u(self):
        self.goto(0,-280)
    def len(self):
        y_moi = self.ycor() +20
        self.goto(0,y_moi)
        