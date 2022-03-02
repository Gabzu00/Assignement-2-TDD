"""Lägga till ny spelare -> Spara spelare"""

class Player_class:
    

    def __init__(self, name, score):
        self.name = name
        self.score = score
    

    def show_score(self):
        print(self.name, "has", self.score, "points")


    def change_score(self, new_score):
        self.score = new_score
