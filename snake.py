from turtle import Turtle

STARTING_POSITIONS = [(0.00, 0.00), (-20.00, 0.00), (-40.00, 0.00)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segments = []       
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):    
        for position in STARTING_POSITIONS: 
            self.add_snake_body(position)
    
    def add_snake_body(self, position):
            new_snake_body = Turtle()
            new_snake_body.color(224, 234, 255)
            new_snake_body.penup()
            new_snake_body.goto(position)
            new_snake_body.shape('square')
            self.segments.append(new_snake_body)
    
    def extend(self):
        self.add_snake_body(self.segments[-1].position())
            
    def move(self):
        # Sets body of the snake to follow the head of the snake.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
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
    