"""imports."""
from . import HighScore
from . import Player1
from . import Player2
from . import Dice
import time


class Start():
    
    """Spelarnas poäng."""
    player1Throws = 0
    player1Score = 0
    player1Total = 0

    player2Throws = 0
    player2Score = 0
    player2Total = 0

    """Variablel för spelare 1 namn."""
    Player1Name = "test1"

    """Variablel för spelare 2 namn."""
    Player2Name = "test2"

    """Skapar spelar objekt."""
    player1 = Player1.Player_class
    player2 = Player2.Player_class

    def init():
        """Ber spelar 1 och 2 om namn."""
        print("Hello!\nWelcome to our game!")
        Start.Player1Name = input("Enter name for player 1: ")
        Start.Player2Name = input("Enter name for player 2: ")

        """Visa vem som har highscore."""
        print("\nCurrent highscore: ")
        HighScore.checkHighScore.read()
        print(f"\nNow its {Start.Player1Name} to start")

        """Sätter namn och poäng till spelar objekt."""        
        Start.player1 = Player1.Player_class(Start.Player1Name, 0)
        Start.player2 = Player2.Player_class(Start.Player2Name, 0)

    def startPlayer1():
        """Kolla om spelate 1 har vunnit."""
        if Start.player1Total >= 100:
            Start.Win1()
        else:
            """Printar ut spelarens poäng och kast."""
            print(f"\nTemporary Score: {Start.player1Score}")
            print(f"Throws: {Start.player1Throws}")
            print(f"Total Score: {Start.player1Total}\n")

            """Frågar spelaren om hen vill fortsätta kasta eller inte."""
            check = False
            while check == False:
                print("Enter 'Y' if you want to throw the dice")
                print("Enter 'N' if you want to end the round")
                print("Enter 'C' if you want to cheat")
                print("Enter 'Q' if you want to quit")
                print("Enter 'W' if you want to change name")
                answer = input("")
                if answer == 'Y' or answer == 'N':
                    check = True
                elif answer == 'C' or answer == 'Q' or answer == 'W':
                    check = True
                else:
                    print("Invalid input\n")

            """Vad som ska hända beroende på svaret från spelaren."""
            if answer == 'Y':
                Start.Player1Throw()
            elif answer == 'C':
                Start.player1Total = 100
                Start.Win1()
            elif answer == 'N':
                print("\nYou chose to stop")
                print(f"Now its {Start.Player2Name} to play")
                Start.player1Total += Start.player1Score
                Start.player1Score = 0
                Start.startPlayer2()
            elif answer == 'W':
                print("Who wants to change name?")
                print(f"{Start.Player1Name} --> Enter 1")
                print(f"{Start.Player2Name} --> Enter 2")
                whoChanges = input()
                newName = input("Enter new name: ")
                if whoChanges == "1":
                    Start.player1.changeName(newName)
                elif whoChanges == "2":
                    Start.player2.changeName(newName)
                Start.startPlayer1()
            else:
                exit()

    def Player1Throw():
        """Add throws."""
        Start.player1Throws += 1

        """Instanciera ett object från Dice klassen."""
        die = Dice.dice

        """Använd objectet för att kastat tärningen."""
        roll = die.throwDice()

        """Printa värdet som tärningen visade."""
        print(f"{Start.Player1Name} rolled the dice!")
        Start.printValue(roll)

        """Vad som ska hända om man slår en etta eller annan siffra."""
        if roll == 1:
            time.sleep(3)
            Start.player1Total -= Start.player1Score
            Start.player1Score = 0
            print(f"\nNow its {Start.Player2Name} to play")
            Start.startPlayer2()
        else:
            Start.player1Score += roll
            Start.player1Total += roll
            Start.startPlayer1()

    def startPlayer2():
        """Kolla om spelare 2 har vunnit."""
        if Start.player2Total >= 100:
            Start.Win2()
        else:
            """Printar ut spelarens poäng och kast."""
            print(f"\nTemporary Score: {Start.player2Score}")
            print(f"Throws: {Start.player2Throws}")
            print(f"Total Score: {Start.player2Total}\n")

            """Frågar spelaren om hen vill fortsätta kasta eller inte."""
            check = False
            while check == False:
                print("Enter 'Y' if you want to throw the dice")
                print("Enter 'N' if you want to end the round")
                print("Enter 'C' if you want to cheat")
                print("Enter 'Q' if you want to quit")
                print("Enter 'W' if you want to change name")
                answer = input("")
                if answer == 'Y' or answer == 'N':
                    check = True
                elif answer == 'C' or answer == 'Q' or answer == 'W':
                    check = True
                else:
                    print("Invalid input\n")

            """Vad som ska hända beroende på svaret från spelaren."""
            if answer == 'Y':
                Start.Player2Throw()
            elif answer == 'C':
                Start.player1Total = 100
                Start.Win2()
            elif answer == 'N':
                print("\nYou chose to stop")
                print(f"Now its {Start.Player1Name} to play")
                Start.player1Total += Start.player1Score
                Start.player1Score = 0
                Start.Player1Throw()
            elif answer == 'W':
                print("Who wants to change name?")
                print(f"{Start.Player1Name}? --> Enter 1")
                print(f"{Start.Player2Name}? --> Enter 2")
                whoChanges = input()
                newName = input("Enter new name: ")
                if whoChanges == "1":
                    Start.player1.changeName(newName)
                elif whoChanges == "2":
                    Start.player2.changeName(newName)
                Start.startPlayer2()
            else:
                exit()

    def Player2Throw():
        """Add throws."""
        Start.player2Throws += 1

        """Instanciera ett object från Dice klassen."""
        die = Dice.dice

        """Använd objectet för att kastat tärningen."""
        roll = die.throwDice()

        """Printa värdet som tärningen visade."""
        print(f"{Start.Player2Name} rolled the dice!")
        Start.printValue(roll)

        """Vad som ska hända om man slår en etta eller annan siffra."""
        if roll == 1:
            time.sleep(3)
            Start.player2Total -= Start.player2Score
            Start.player2Score = 0
            print(f"\nNow its {Start.Player1Name} to play")
            Start.startPlayer1()
        else:
            Start.player1Score += roll
            Start.player1Total += roll
            Start.startPlayer2()

    def Win1():
        """Kolla om spelare har vunnit."""
        print(f"{Start.Player1Name} wins!!!")
        print(f"You threw {Start.player1Throws} times!")

        """Skicka in antalet kast till spelar objectet."""
        Start.player1.ThrowScore(Start.player1Throws)

        """Om någon vinner kollar man om det är ett highscore eller inte."""
        call = HighScore.checkHighScore
        call.addHighScore(Start.player1Throws, Start.player1)
        print("New highscore!!!")
        exit()

    def Win2():
        """Kolla om spelare har vunnit."""
        print(f"{Start.Player2Name} wins!!!")
        print(f"You threw {Start.player2Throws} times!")

        """Skicka in antalet kast till spelar objectet."""
        Start.player2.ThrowScore(Start.player2Throws)

        """Om någon vinner kollar man om det är ett highscore eller inte."""
        call = HighScore.checkHighScore
        call.addHighScore(Start.player2Throws, Start.player2)
        print("New highscore!!!")
        exit()

    def printValue(roll):
        """Instanciera ett object från Dice klassen."""
        die = Dice.dice
        """Printar symbolen som tärningen visar."""
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
        else:
            print(die.diceSix())
