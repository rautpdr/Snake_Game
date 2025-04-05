#keeping scoreboard
#using Turtle as a superclass to utilise its functionalities.


from turtle import Turtle

class scoreboard(Turtle):

    #initilaising scoreboard
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,285)
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.update_score()

    #updating scoreboard
    def update_score(self):
        self.clear()#clear old score to avoid overlapping of texts
        self.write(f"SCORE = {self.score}" , False , "center")

    #incrementing score(used for successful collision with food)
    def score_inc(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)#printing game over message to center of the screen
        self.write("GAME OVER!" , False , "center" )




