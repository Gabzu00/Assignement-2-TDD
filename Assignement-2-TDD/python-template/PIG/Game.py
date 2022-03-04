"""Vad spelaren har i handen och vad som händer därefter"""
import Dice
import Player
import random
import time
import HighScore

class Start():
    
    """Spelarens och bottens poäng"""
    player1Throws = 0
    player1Score = 0
    player1Total = 0

    BOTThrows = 0
    BOTScore = 0
    BOTTotal = 0
    
    """Ber spelaren om namn"""
    print("Hello!\nWelcome to our game!")
    player1 = input(f"Enter your name: ")
    
    """Skapar spelar objekt"""
    player = Player.Player_class(player1, 0)
    
    """Visa vem som har highscore"""
    print("Current highscore: ")
    HighScore.read()
    time.sleep(3)

    def startPlayer():
        if Start.player1Total >= 100:
            Start.Win()
        
        """Printar ut spelarens poäng och kast"""
        print(f"Score {Start.player1Score}")
        print(f"Throws {Start.player1Throws}")
        print(f"Total {Start.player1Total}\n")
        
        """Frågar spelaren om hen vill fortsätta kasta eller inte"""
        print("Enter 'Y' if you want to throw the dice")
        print("Enter 'N' if you want to end the round")
        print("Enter 'C' if you want to cheat")
        answer = input()
        
        """Vad som ska hända beroende på svaret från spelaren"""
        if answer == 'Y':
            Start.PlayerThrow()
        elif answer == 'C':
            Start.player1Total = 100
            Start.Win()
        else: 
            print("You chose to stop\n")
            Start.player1Total += Start.player1Score
            Start.player1Score = 0
            Start.BotThrow()
 
    def Win():
        """Kolla om spelare har vunnit"""
        if Start.player1Total >= 100:
            print("You win!!!")
            print(f"You threw {Start.player1Throws} times!")
            Start.player.ThrowScore(Start.player1Throws)
            
            """Om någon vinner kollar man om det är ett highscore eller inte """
            HighScore.addHighScore(Start.player1Throws, Start.player)
            print("New highscore!!!")
            exit()
    
    def PlayerThrow():    
        """Add throws"""
        Start.player1Throws += 1
        
        """Instanciera ett object från Dice klassen"""
        die = Dice.dice
        
        """Använd objectet för att kastat tärningen"""
        roll = die.throwDice()
        
        """Printa värdet som tärningen visade"""
        print("You rolled the dice!")
        Start.printValue(roll)
        
        """Vad som ska hända om man slår en etta eller annan siffra"""
        if roll == 1:
            time.sleep(3)
            Start.player1Total -= Start.player1Score
            Start.player1Score = 0
            Start.BotThrow()
        else:
            Start.player1Score += roll
            Start.player1Total += roll
            Start.startPlayer()
        
    def BotThrow():
        """Instanciera ett object från Dice klassen"""
        die = Dice.dice
        
        """Använd objectet för att kastat tärningen och printa värdet"""
        roll = die.throwDice()
        
        """Lägger till poäng och kast"""
        Start.BOTThrows += 1
        Start.BOTScore += roll
        
        """Printar ut vad BOTen fick"""
        print("\nBOT rolled the dice!")
        Start.printValue(roll)
        
        """Programmet ska vänta 2 sekunder så man hänger med i spelet"""
        time.sleep(3)
        
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
                print(f"Score {Start.BOTScore}")
                print(f"Throws {Start.BOTThrows}")
                print(f"Total {Start.BOTTotal}\n")
                Start.BotThrow()
            else: 
                keepGoing = False
                
                Start.BOTTotal += Start.BOTScore
                Start.BOTScore = 0
                print("The BOT chose to stop")
                time.sleep(3)
                
                name = Start.player1
                print(f"\nNow its {name}")
                Start.startPlayer()
                
    def printValue(roll):
        """Instanciera ett object från Dice klassen"""
        die = Dice.dice
        """Printar symbolen som tärningen visar"""
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
                
                
                
        
   
        
        
            
        
    