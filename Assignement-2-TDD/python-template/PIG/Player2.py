"""Lägga till ny spelare -> Spara spelare 2"""

class Player_class:
    
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show_score(self):
        print(self.name, "has", self.score, "points")
        
    def ThrowScore(self, high_score):
        self.score = high_score

    def getName(self):
        print(self.name)
        
    def getScore(self):
        print(self.score)

    def changeName(self, name):
        self.name = name