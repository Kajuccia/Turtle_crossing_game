from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
y_position = random.randint(-300, 300)

class CarManager():
    def __init__(self):
        self.cars = []
        self.move_speed = 0.1

    def create_car(self):
        rand = random.randint(0,6)
        if rand == 6:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.penup()
            y_position = random.randint(-300, 300)
            car.goto((290, y_position))
            self.cars.append(car)

    def more_cars(self):
        rand = random.randint(0, 8)
        if rand == 6 or rand==8:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.penup()
            y_position = random.randint(-300, 300)
            car.goto((290, y_position))
            self.cars.append(car)

    def move_car(self):
        for i in self.cars:
            new_x = i.xcor() - 5
            i.goto(new_x, i.ycor())

    def increase_difficulty(self):
        self.move_speed *= 0.9