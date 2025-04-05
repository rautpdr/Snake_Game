#constants
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

from turtle import Turtle

#starting snake with 3 segments
segment_starting_postions = [(0,0) , (-20,0), (-40,0)]
move_distance = 20


class snake_class:

    #constructor to initialise
    def __init__(self):
        self.segments_obj_list = [] #to save objects of segments of snakes created
        self.create_snake()
        self.head_of_snake = self.segments_obj_list[0]

    #creating a snake
    def create_snake(self):
        for seg in segment_starting_postions:
            self.add_segment(seg)


    #adding segments
    def add_segment(self,seg):
        new_seg = Turtle()
        new_seg.penup()
        new_seg.shape("square")
        new_seg.color("white")
        new_seg.goto(seg)
        self.segments_obj_list.append(new_seg)

    #icresing length upon hitting food by adding a segment at the end
    def extend(self):
        self.add_segment(self.segments_obj_list[-1].position())#adding segment to last of the snake segment




    #movement of snake
    def move_snake(self):
        for seg_num in range(len(self.segments_obj_list) - 1 , 0 , -1):
            #get last block to second last block 3 -> 2 , means moving last segment to second last segment's co-ordinate
            second_last_seg_x = self.segments_obj_list[seg_num - 1].xcor() #fetching x-cor for second last
            second_last_seg_y = self.segments_obj_list[seg_num - 1].ycor() #fetching y-cor for second last
            self.segments_obj_list[seg_num].goto(second_last_seg_x, second_last_seg_y) #last segment -> second last
        self.segments_obj_list[0].forward(move_distance)

    #moving snake up with "w" key
    def up(self):
        if self.head_of_snake.heading() != DOWN: #snake shouldn't go up when its moving down.
            self.head_of_snake.setheading(90)

    #moving snake down with "s" key
    def down(self):
        if self.head_of_snake.heading() != UP: #snake shouldn't go down when its moving up.
            self.head_of_snake.setheading(DOWN)


    #moving snake left with "a" key
    def left(self):
        if self.head_of_snake.heading() != RIGHT:#snake shouldn't go left when its moving right.
            self.head_of_snake.setheading(LEFT)


    #moving snake right with "d" key
    def right(self):
        if self.head_of_snake.heading() != LEFT: #snake shouldn't go right when its moving left
            self.head_of_snake.setheading(RIGHT)


