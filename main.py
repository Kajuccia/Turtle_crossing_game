import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()


screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(car_manager.move_speed)
    screen.update()
    if scoreboard.score < 5:
        car_manager.create_car()
        car_manager.move_car()
    else:
        car_manager.more_cars()
        car_manager.move_car()

    if player.ycor() > player.finish_line:
        player.new_level()
        scoreboard.gain_score()
        car_manager.increase_difficulty()


    for car in car_manager.cars:
        if player.distance(car) < 15:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()