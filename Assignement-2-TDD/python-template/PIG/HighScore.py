"""Visa rekordlista genom en List."""
import os

class checkHighScore():
    """Metoder för klassen."""

    def toFile(player):
        """Skriver in det nya rekordet till text fil."""
        with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/PIG/HighScore.txt', 'w') as add:
            add.write(str(player.__dict__))

    def read():
        """Printar det nuvarande rekordet."""
        with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/PIG/HighScore.txt', 'r') as show:
            data = show.read().rstrip().replace('}', '')
            data2 = data.replace('{', '').replace("'", "")
            print(data2)

    def addHighScore(newSore, player):
        """Läser från filen och tar ut det senaste rekordet."""
        with open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/PIG/HighScore.txt', 'r') as file:
            if os.stat(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/PIG/HighScore.txt').st_size == 0:
                checkHighScore.toFile(player)

            for line in file:
                fields = line.strip('}').split(":")
                fileScore = fields[-1]

            """Jämför gammalt rekord med det nya."""
            if int(fileScore) >= newSore:
                checkHighScore.toFile(player)
            else:
                print("End")
