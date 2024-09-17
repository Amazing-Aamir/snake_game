from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self,player):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,260)
        self.write(arg=f"Player Name: {player}          Score: {self.score}",align="center",font=("Courier",18,"bold"))
        self.hideturtle()

    def reset(self):
        self.clear()

    def increase_score(self,player):
        self.score += 1
        self.write(arg=f"Player Name: {player}          Score: {self.score}",align="center",font=("Courier",18,"bold"))

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"Game Over!", align="center", font=("Courier", 18, "bold"))

