from turtle import Turtle

STARTING_POSITIONS = [(0.00, 0.00), (-20.00, 0.00), (-40.00, 0.00)]
MOVE_DISTANCE = 20

class Snake():
    def __init__(self):
        
        self.segments = []       
        self.create_snake()
        
    def create_snake(self):    
        for position in STARTING_POSITIONS: 
            new_snake_body = Turtle()
            new_snake_body.color(224, 234, 255)
            new_snake_body.penup()
            new_snake_body.goto(position)
            new_snake_body.shape('square')
            self.segments.append(new_snake_body)
            
    def move(self):
        global segments
        # Sets body of the snake to follow the head of the snake.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
        
    