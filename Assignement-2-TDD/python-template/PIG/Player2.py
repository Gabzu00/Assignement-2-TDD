"""Lägga till ny spelare -> Spara spelare 2"""

class Player_class:
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def ThrowScore(self, high_score):
        self.score = high_score

    def changeName(self, name):
        self.name = name
