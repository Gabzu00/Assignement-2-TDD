"""Visa rekordlista genom en List"""

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

   with open('HighScore.txt', 'r') as file:
    
    for line in file:
        fields = line.strip('}').split(":")
        fileScore = fields[-1]
    
    if int(fileScore) >= newSore:
        toFile(player)
    else :
        exit()






