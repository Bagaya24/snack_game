from turtle import Screen
import time

from score import Score
from snake import Snake
from food import Food

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


screen.listen()


screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detecte colision with food
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        score.add_score()

    #Detecte colision with wall:
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        food.refresh()
        snake.reset_position()
        score.reset_score()

    #Detecte colision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            food.refresh()
            snake.reset_position()
            score.reset_score()
screen.exitonclick()
