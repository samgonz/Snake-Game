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

for position in starting_positions:
    new_snake_body = Turtle()
    new_snake_body.color(224, 234, 255)
    new_snake_body.penup()
    new_snake_body.goto(position)
    new_snake_body.shape('square')
    segments.append(new_snake_body)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    
    for seg_num in range()
        
screen.exitonclick()