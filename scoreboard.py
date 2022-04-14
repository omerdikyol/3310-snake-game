from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,270)
        self.update()

    def update(self):
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 270)
        self.write(f"Keys: Up,Down,Left,Right", align="left", font=("Courier", 10, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)