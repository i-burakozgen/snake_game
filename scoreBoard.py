from turtle import Turtle, Screen
from bait import Bait

class ScoreBoard(Turtle):
    def __init__(self, bait):
        super().__init__()
        self.bait = bait
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.update_score_board()
    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.bait.score}", align="center", font=("Arial", 24, "normal"))

    def score_board_increase(self):
        self.update_score_board()
