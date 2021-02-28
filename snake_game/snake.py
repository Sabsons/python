from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    #On creation create the segments list and add the first 3 squares using create_snake and assigning the first square as the head.
    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    #Create the snake by looping through the positions and adding them to the segments
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    #Create a white square and add it to the segments list.
    def add_segment(self,position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    #Add segment when we eat food at the end of the segments list.
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Make the last element replace the next element and making the head of the snake move so the body will follow it.
    def move(self):
        #For loop which will let us swap the last elements to the before last elements arriving to the first.
        for seg_number in range(len(self.segments) - 1, 0, -1):  # we swap the last element of the list which is len -1 , arriving to the first which is 0 and we step -1.
            new_x = self.segments[seg_number - 1].xcor()  # We get a hold of the next before last element x
            new_y = self.segments[seg_number - 1].ycor()  # We get a hold of the next before last element y
            self.segments[seg_number].goto(new_x, new_y)  # We swap the last element of the list x and y to the next one.
        self.head.forward(MOVE_DISTANCE)  # We move the first element by 20

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
