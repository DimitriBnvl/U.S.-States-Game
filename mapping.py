from turtle import Turtle

#------------------TEXT ON MAP------------------#
class Map(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def correct_answer(self, x, y, state):
        self.goto(x, y)
        self.write(state, align='center', font=('Times New Roman', 12, 'normal'))