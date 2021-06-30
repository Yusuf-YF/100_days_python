from turtle import Turtle


# inherit Turtle class from Paddle to make two objects.
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        # paddle attributes.
        self.shape("square")
        self.color("cyan")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
