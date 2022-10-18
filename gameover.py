from turtle import Turtle

ALIGNMENT = 'center'
FONT_TYPE = 'Courier'
FONT_SIZE = 40
FONT_MANAGEMENT = 'normal'
FONT = (FONT_TYPE, FONT_SIZE, FONT_MANAGEMENT)

class game_over(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.write('GAME OVER', align = ALIGNMENT, font = FONT) 