from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score_tracker = ScoreBoard()

screen.listen()
screen.onkey(snake.move_up, "Up",)
screen.onkey(snake.move_down, "Down",)
screen.onkey(snake.move_right, "Right",)
screen.onkey(snake.move_left, "Left",)

game_is_on = True
score = 0

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_tracker.update_score()

    # detect collision with wall
    if snake.head.xcor() > 280:
        snake.head.setx(-300)
    elif snake.head.xcor() < -280:
        snake.head.setx(300)
    elif snake.head.ycor() > 280:
        snake.head.sety(-300)
    elif snake.head.ycor() < -280:
        snake.head.sety(280)

    # detect colision with tail
    # if head collied with any segment of the tail trigger game over method
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            score_tracker.game_over()

screen.exitonclick()
