import random
from turtle import Turtle
#using Turtle as a superclass to utilise its functionalities.


class food_class(Turtle):

    def __init__(self):
        super().__init__()
        #generate food
        self.shape("circle") #setting shape for food
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)   #setting size for food
        self.speed("fastest")
        self.color("blue")
        self.food_placement()

    def food_placement(self):
        #random food placement
        food_xcorr = random.randint(-270 , 270)
        food_ycorr = random.randint(-270,270)
        self.goto(food_xcorr,food_ycorr)
