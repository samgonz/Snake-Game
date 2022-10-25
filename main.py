import time
from turtle import Screen
from food import Food
from gameover import game_over
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake")
screen.colormode(255)
screen.tracer(0)

# Creates the snake segments shapes and colors. 
snake = Snake()

# Creates the food segments shapes and colors
food = Food()

# Creates the scoreboard 
scoreboard = Scoreboard()

# Creates a listener to listen for keyboard events
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
# Creates a loop that updates the screen every .1 second.
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()    
        
    # Detect collision with food segments
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    
    # Detect collision with screen boundaries    
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        scoreboard.reset()
        snake.reset()
        
    # Detect collision with snake body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# end_game = game_over()


screen.exitonclick()