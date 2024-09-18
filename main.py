from turtle import Turtle, Screen
import time
from snakeMovement import SnakeMovement
from bait import Bait
from scoreBoard import ScoreBoard

screen = Screen()
screen.title("Snake Game")
screen.screensize(600,600, "black")
screen.tracer(0)
start_pos = ((0,0), (-20,0), (-40,0))


snake = SnakeMovement(start_pos)
snake.bodyCreator()
snake.keyLogic()
bait = Bait(score=0)
score_board = ScoreBoard(bait)
score = 0


while snake.gameIsOn():
    screen.update()
    snake.followHead()
    time.sleep(0.1)
    snake.startMovement()
    bait.collision_bait(snake)
    if bait.distance(snake.segments[0]) < 15:
        score+=1
screen.exitonclick()


