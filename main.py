#Develop a snake game
#create a screen
#use sqaure segments to visualise snake and its movements
# segment 3 goes to 2 and segment 2 goes to 1
import time
from turtle import Turtle,Screen
from snake import snake_class
from food import  food_class
from score import scoreboard

#set-up
screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("Snake Game...")
screen.tracer(0) #stops updating screen, needs to use screen.update() to manually update.

#creating snake object
snake = snake_class()

#Assigning keys for movement of snake
screen.listen()
screen.onkey(snake.up , "w")
screen.onkey(snake.down , "s")
screen.onkey(snake.right , "d")
screen.onkey(snake.left , "a")

#creating food object
food = food_class()

#creating score object
score = scoreboard()


#flag for while loop to check whether game is on or off
is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    snake.move_snake()


    #detect collision with food using distance method
    if snake.head_of_snake.distance(food) < 17:#distance between head of the snake and food
        food.food_placement()
        snake.extend()
        score.score_inc() #increment score

    #detect collision with boundaries
    if snake.head_of_snake.xcor() > 285 or snake.head_of_snake.xcor() < -285 or snake.head_of_snake.ycor() > 285 or snake.head_of_snake.ycor() < -285:
        is_game_on = False
        score.game_over()

    #detect collision with itself
    for seg in snake.segments_obj_list[1:]:#skipping first element in list as first element is head

        if snake.head_of_snake.distance(seg) < 10:
            is_game_on = False
            score.game_over()





screen.exitonclick()