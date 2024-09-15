from turtle import Turtle, Screen
import time
from random import randint
from snakeMovement import SnakeMovement

screen = Screen()
screen.title("Snake Game")
screen.screensize(600,600, "black")
screen.tracer(0)
start_pos = ((0,0), (-20,0), (-40,0))


snake = SnakeMovement(start_pos)
snake.bodyCreator()
snake.keyLogic()


while snake.gameIsOn():
    screen.update()
    time.sleep(0.1)
    snake.followHead()
    snake.startMovement()



screen.exitonclick()


