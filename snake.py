from turtle import Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []

        for pos in STARTING_POSITIONS:
            self.add_part(pos)

        self.head = self.segments[0]

    def add_part(self, position):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(position)
        self.segments.append(new_part)

    def extend(self):
        self.add_part(self.segments[-1].position())

    def move(self):
        for part_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[part_num - 1].xcor()
            new_y = self.segments[part_num - 1].ycor()
            self.segments[part_num].goto(new_x, new_y)  # Follow the snake part in front

        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:  # If it is not going down
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def pass_wall(self , width):
        if abs( self.head.xcor() ) > width/2 - 20:
            self.head.goto(x= -self.head.xcor(), y= self.head.ycor())

        elif abs( self.head.ycor() ) > width/2 - 20:
            self.head.goto(x= self.head.xcor(), y= -self.head.ycor())

