"""Lägga till ny spelare -> Spara spelare 1."""


class Player_class:
    """Meoder för vår klass."""

    def __init__(self, name, score):
        """Konstruktor."""
        self.name = name
        self.score = score

    def ThrowScore(self, high_score):
        """Sätter score till highscore."""
        self.score = high_score

    def changeName(self, name):
        """Byta namn på objektet."""
        self.name = name
