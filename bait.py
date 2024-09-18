import random
from turtle import Turtle, Screen
import time
from snakeMovement import SnakeMovement
class Bait(Turtle):
    def __init__(self,score):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(0.6)
        self.penup()
        self.score = score
        self.hideturtle()
        self.screen = Screen()
        self.random_respawn()


    def random_respawn(self):
        pos_x = random.randint(-280, 280)
        pos_y = random.randint(-280, 280)
        self.goto(pos_x,pos_y)
        self.showturtle()
    def collision_bait(self,snake):
        if self.distance(snake.segments[0]) < 15:  # Assuming 15 as the threshold for collision
            self.hideturtle()  # Hide bait on collision
            self.random_respawn()  # Respawn bait to a new position
            self.score += 1













