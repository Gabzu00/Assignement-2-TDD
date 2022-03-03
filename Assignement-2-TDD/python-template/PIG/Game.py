"""Vad spelaren har i handen och vad som händer därefter"""
import Dice
import Player
import random

class Start():
    
    """Tar spelarens namn och skapar object"""
    player1Throws = 0
    player1Score = 0
    player1Total = 0
    
    BOTThrows = 0
    BOTScore = 0
    BOTTotal = 0
    
    player1 = input("Enter your name: ")
    player = Player.Player_class(player1, 0)
    
    def startPlayer():
        """Loopar om användaren vill fortsätta kasta eller avsluta rundan"""
        print("Score " , Start.player1Score)
        print("Throws " , Start.player1Throws)
        print(f"Total {Start.player1Total}")
        print("Enter 'Y' if you want to throw the dice")
        print("Enter 'N' if you want to end the round")
        answer = input()
        if answer == 'Y':
            Start.PlayerThrow()
        else: 
            print("You chose to stop")
            Start.player1Total += Start.player1Score
            Start.player1Score = 0
            Start.BotThrow()
 
    
    def PlayerThrow():
        """Kolla om spelare har vunnit"""
        if Start.player1Total == 100:
            print("You win!!!")
            print(f"You threw {Start.player1Throws} times!")
        
        """Instanciera ett object från Dice klassen"""
        die = Dice.dice
        
        """Add throws"""
        Start.player1Throws += 1
        
        """Använd objectet för att kastat tärningen och printa värdet"""
        roll = die.throwDice()
        if roll == 1:
            print(die.diceOne())
        elif roll == 2:
            print(die.diceTwo())
        elif roll == 3:
            print(die.diceThree())
        elif roll == 4:
            print(die.diceFour())
        elif roll == 5:
            print(die.diceFive())
        else: print(die.diceSix())
        
        """Vad som ska hända om man slår en etta eller annan siffra"""
        if roll == 1:
            Start.player1Score = 0
            Start.BotThrow()
        else:
            Start.player1Score += roll
            Start.startPlayer()
        
    def BotThrow():
        die = Dice.dice
        roll = die.throwDice()
        
        Start.BOTThrows += 1
        Start.BOTScore += roll
        
        print("BOT rolled the dice!")
        print(f"It was a {roll}")
        
        if roll == 1:
            Start.BOTScore = 0
            name = Start.player1
            print(f"Now its {name}")
            Start.startPlayer()
        else : 
            Start.option(roll)
    
    def option(roll):
        keepGoing = True
        while keepGoing:
            
            if Start.BOTTotal == 100:
                    print("The BOT won )=")
                    print(f"The BOT threw {Start.BOTThrows} times!!")
                    keepGoing = False
            odds = random.randint(1,2)
            
            if odds == 1:
                print("Score " , Start.BOTScore)
                print("Throws " , Start.BOTThrows)
                print("Total " , Start.BOTTotal)
                Start.BotThrow()
            else: 
                keepGoing = False
                
                Start.BOTTotal += Start.BOTScore
                Start.BOTScore = 0
                print("The BOT chose to stop")
                
                name = Start.player1
                print(f"Now its {name}")
                
                
                
        
   
        
        
            
        
    