import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake")
screen.colormode(255)
screen.tracer(0)

starting_positions = [(0.00, 0.00), (-20.00, 0.00), (-40.00, 0.00)]
segments = []

# Creates the snake segments shapes and colors. 
for position in starting_positions: 
    new_snake_body = Turtle()
    new_snake_body.color(224, 234, 255)
    new_snake_body.penup()
    new_snake_body.goto(position)
    new_snake_body.shape('square')
    segments.append(new_snake_body)

game_is_on = True
# Creates a loop that updates the screen every .1 second.
while game_is_on:
    screen.update()
    time.sleep(.1)
    
    # Sets body of the snake to follow the head of the snake.
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)    
        
screen.exitonclick()