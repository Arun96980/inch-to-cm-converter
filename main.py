from turtle import Screen, Turtle
from snake import *
from food import *
from scoreboard import *
import time

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create snake
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for key presses
screen.listen()
screen.onkey(snake.up, "Up")    # Use "Up" instead of "up"
screen.onkey(snake.down, "Down")  # Use "Down" instead of "down"
screen.onkey(snake.left, "Left")  # Use "Left" instead of "left"
screen.onkey(snake.right, "Right")  # Use "Right" instead of "right"

# Main game loop
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.inc_score()


    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()


    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()




screen.exitonclick()

