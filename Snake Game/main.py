# -*- coding: utf-8 -*-
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
import winsound
screen =  Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title('My Snake Game')
screen.tracer(0)
game_is_on = True

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

def clear_text():
    snake.head.clear()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collision with food
    if snake.head.distance(food) < 15:
        #winsound.PlaySound("scoreup.wav", winsound.SND_ASYNC)
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
       # snake.head.write("nom nom nom! \U0001F40D ", align="center",font=("Courier New",18,"bold"))
        screen.ontimer(clear_text, 2000)

    #detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.reset()
        snake.reset()
        #winsound.PlaySound("gameover.wav", winsound.SND_ASYNC)


    #detect collision with body

    for segment in snake.segments[1:]:

        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            #winsound.PlaySound("gameover.wav", winsound.SND_ASYNC)





screen.exitonclick()
