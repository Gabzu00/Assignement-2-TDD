"""Visa rekordlista genom en List"""
class checkHighScore():
    
    def toFile(player):
        """Skriver in det nya rekordet till text fil"""
        with open ('HighScore.txt', 'w') as add:
            add.write(str(player.__dict__))
        
    def read():
        """Printar det nuvarande rekordet"""
        with open('HighScore.txt', 'r') as show:
            data = show.read().rstrip().replace('}', '').replace('{', '').replace("'", "")
            print(data)

    def addHighScore(newSore, player):
        """Läser från filen och tar ut det senaste rekordet"""
        with open('HighScore.txt', 'r') as file:

            for line in file:
                fields = line.strip('}').split(":")
                fileScore = fields[-1]
                
            """Jämför gammalt rekord med det nya"""
            if int(fileScore) >= newSore:
                checkHighScore.toFile(player)
            else :
                exit()
