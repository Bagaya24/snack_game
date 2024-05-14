from turtle import Turtle
ALIGN = "center"
FONT = ("Calibri", 18, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.high_score = self.read_high_score()
        self.score = 0
        self.update_score()

    @staticmethod
    def read_high_score():
        with open("data.txt") as file:
            return int(file.read())

    def write_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.score}")
        self.high_score = self.read_high_score()

    def update_score(self):
        self.clear()
        self.write(f"score: {self.score}   High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.write_high_score()

        self.score = 0
        self.update_score()

    def game_over(self):

        self.home()
        self.write("Game over", align=ALIGN, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()