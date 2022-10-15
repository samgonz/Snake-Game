import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake")
screen.colormode(255)
screen.tracer(0)

# Creates the snake segments shapes and colors. 
snake = Snake()

game_is_on = True
# Creates a loop that updates the screen every .1 second.


while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()    
        
screen.exitonclick()