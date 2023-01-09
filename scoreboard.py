from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(-230, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.score}", align='center', font=('Arial', 25 , 'normal'))

    def gain_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", align='center', font=('Arial', 30, 'normal'))