from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Georgia", 20, "bold")
class ScoreBoard(Turtle):
       def __init__(self):
           super().__init__()
           self.score = 0
           with open("data.txt") as data:
               self.highscore = int(data.read())
           self.color("green")
           self.penup()
           self.goto(0, 270)
           self.hideturtle()
           self.update_score()
       #to update the score and to prevent overlapping of scores on top of each other
       def update_score(self):
           # to clear the previous score and display the increased score
           self.clear()
           self.write(f"SCORE : {self.score}, HIGH SCORE : {self.highscore}", align=ALIGNMENT, font=FONT)

       def reset(self):
            if self.score>self.highscore:
                self.highscore = self.score
                with open("data.txt",mode="w") as data:
                    data.write(f"{self.highscore}")
            self.score=0
            self.update_score()
       # def game_over(self):
       #     self.goto(0,0)
       #     self.write("GAME OVER \U0001F641",align = ALIGNMENT,font = FONT)
       def increase_score(self):
           self.score += 1
           self.update_score()