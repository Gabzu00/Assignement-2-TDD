"""Visa rekordlista genom en List"""
import Player

def toFile(player):
    
    with open ('HighScore.txt', 'w') as add:
        new = Player.Player_class
        first = str(new.getName(player))
        second = str(new.getScore(player))
        add.write(first)
        add.write(second)
        
def read():
    with open('HighScore.txt', 'r') as show:
        print(show.readlines())
        
def addHighScore(newSore, player):
   with open('HighScore.txt', 'r') as ass:
    for line in ass:
        fields = line.strip().split()
        fileScore = int(fields[1])
    
    if fileScore > newSore:
        toFile(player)
    else :
        exit()






