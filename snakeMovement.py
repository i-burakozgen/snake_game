import logging
from turtle import Turtle, Screen
class SnakeMovement:
    def __init__(self, position):
        self.segments = []
        self.position = position
        self.screen = Screen()
        self.current_head_rot = 0
        self.speed = 10
        logging.info(f"snake initialized with position {self.position}")

    def bodyCreator(self):
        for pos in self.position:
            snake = Turtle(shape='square')
            snake.color("white")
            snake.penup()
            snake.goto(pos)
            self.segments.append(snake)

    def followHead(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            snake_x = self.segments[segment_num - 1].xcor()
            snake_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(snake_x, snake_y)
            self.border_logic()

    def set_heading(self, angle):
        current_angle = self.segments[0].heading()
        if abs(current_angle - angle) != 180:
            self.segments[0].setheading(angle)
            self.current_head_rot = angle
        logging.info("Snake heading set to %s degrees", angle)
    def heading_angle(self,angle):
        def f():
            self.set_heading(angle)
        return f

    def keyLogic(self):
        key_mapping = {
            "w":90,
            "a":180,
            "s":270,
            "d":360
        }
        for key, angle in key_mapping.items():
            self.screen.onkey(self.heading_angle(angle), key)
        self.screen.listen()

    def startMovement(self):
        self.segments[0].forward(10)


    def border_logic(self):
        head_x = self.segments[0].xcor()
        head_y = self.segments[0].ycor()
        if head_x > 370:
            self.segments[0].teleport(x = -360)
        elif head_x < -370:
            self.segments[0].teleport(x = 360)
        elif head_y > 370:
            self.segments[0].teleport(y = -360)
        elif head_y < -370:
            self.segments[0].teleport(y = 360)


    def gameIsOn(self):
        game_is_on = True
        return game_is_on
