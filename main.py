from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time

scr = Screen()
scr.setup(600,600)
scr.tracer(0)
segment = []
player = scr.textinput("Snake Game", "Enter Your Name").capitalize()
time_speed = 0.9
segment_distance = -20
initial_snake_segment = 3

def snake_segment():

    global segment_distance
    global initial_snake_segment

    for _ in range(initial_snake_segment):
        snake = Snake()
        segment.append(snake)

        initial_snake_segment = 0


def init_position():

    global segment_distance

    for seg in range(1,len(segment)):
        segment[seg].position(segment_distance)
        segment_distance -= 20

snake_segment()
food = Food()
score_board = ScoreBoard(player)
food.location()

def add_segment():
    global initial_snake_segment
    global time_speed
    initial_snake_segment += 1
    snake_segment()
    if time_speed > 0.1:
        time_speed -= 0.1


scr.listen()
scr.onkey(fun=segment[0].move_up, key='Up')
scr.onkey(fun=segment[0].move_down, key='Down')
scr.onkey(fun=segment[0].move_right, key='Right')
scr.onkey(fun=segment[0].move_left, key='Left')

count = 0
game_is_on = True


while game_is_on:
    time.sleep(time_speed)
    scr.update()

    segment[0].color('dark green')

    for body in range(1,len(segment)):
        segment[body].body_color()

    segment[0].move_forward(segment)
    snake_position = (segment[0].xcor(),segment[0].ycor())

    if food.distance(snake_position) <= 15:
        food.location()
        score_board.reset()
        score_board.increase_score(player)
        count += 1
        if count >= 3:
            add_segment()
            count = 0

    for s in segment[1:]:
        if segment[0].distance(s) < 10:
            game_is_on = False
            score_board.game_over()

    snake_wall_position_x = segment[0].xcor()
    snake_wall_position_y = segment[0].ycor()

    if snake_wall_position_x >= 300:
        segment[0].goto(-300,snake_wall_position_y)
    elif snake_wall_position_x <= -300:
        segment[0].goto(300, snake_wall_position_y)
    elif snake_wall_position_y >= 250:
        segment[0].goto(snake_wall_position_x,-300)
    elif snake_wall_position_y <= -300:
        segment[0].goto(snake_wall_position_x,250)


scr.exitonclick()



