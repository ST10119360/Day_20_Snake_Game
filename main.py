from turtle import Screen
import time
from food import Food
from snake import SnakeAtt

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = SnakeAtt("square", "white", 0, 0)
snake.setup_snake()
food = Food()
score_display = snake.score()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if (#checks if the snake is touching a wall
            snake.segments[0].xcor() > screen.window_width() / 2 - 15 or
            snake.segments[0].xcor() < -screen.window_width() / 2 + 15 or
            snake.segments[0].ycor() > screen.window_height() / 2 - 15 or
            snake.segments[0].ycor() < -screen.window_height() / 2 + 15
    ):
        game_is_on = False
        screen.bye()
        final_score = len(snake.segments) - 3# the -3 is because the snake segment always starts with 4
        print(f"Your final score was: {final_score}")
    for segment in snake.segments[1:]:#Slicing
        if snake.segments[0].distance(segment) < 15:
            game_is_on = False
            screen.bye()
            final_score = len(snake.segments) - 3
            print(f"You bit your own tail. Your final score was: {final_score}")
            break  # Exit the loop since the collision is detected
    # Detect food collision
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score_display.clear()
        score_display.write(f"Score: {len(snake.segments)-3}", align="center", font=("Arial", 12, "normal"))


