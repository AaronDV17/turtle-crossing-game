from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snakey = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snakey.up)
screen.onkey(key="Down", fun=snakey.down)
screen.onkey(key="Left", fun=snakey.left)
screen.onkey(key="Right", fun=snakey.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snakey.move()

    # Detect collision with food
    if snakey.head.distance(food) < 15:
        food.refresh()
        snakey.extend()
        scoreboard.increase_score()

    # Detect collision with walls
    if abs(snakey.head.xcor()) > 280 or abs(snakey.head.ycor()) > 280:
        scoreboard.reset()
        snakey.reset()

    # Detect collision with tail
    for segment in snakey.segments[1:]:
        if snakey.head.distance(segment) < 10:
            scoreboard.reset()
            snakey.reset()

screen.exitonclick()
