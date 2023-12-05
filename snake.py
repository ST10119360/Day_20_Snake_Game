import random
from turtle import Turtle, Screen


class SnakeAtt:
    def __init__(self, shape, color, x, y):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.screen = Screen()
        self.colors = color
        self.shapes = shape
        self.turtle_instance = Turtle()
        self.start_width = int(x)
        self.start_height = int(y)
        self.snake_score = 0

    def setup_snake(self):

        for position in self.starting_positions:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move_forward(self):
        self.segments[0].setheading(90)

    def turn_left(self):
        self.segments[0].setheading(180)

    def turn_right(self):
        self.segments[0].setheading(0)

    def move_down(self):
        self.segments[0].setheading(270)

    def extend(self):
        # Add a new segment to the snake
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        self.segments.append(new_segment)

    def score(self):
        snake_score = Turtle()
        snake_score.color("white")
        snake_score.penup()
        snake_score.hideturtle()
        snake_score.goto(0, 280)
        return snake_score
    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

        self.screen.listen()
        self.screen.onkeypress(self.move_down, "Down")
        self.screen.onkeypress(key="Up", fun=self.move_forward)
        self.screen.onkeypress(key="Left", fun=self.turn_left)
        self.screen.onkeypress(key="Right", fun=self.turn_right)
