"""Imports för klassen."""
from. import Dice
from. import Player1
import random
import time
from. import HighScore


class Start():
    """Variabel för väntetid."""

    waitTime = 3

    """Spelarens och bottens poäng."""

    player1Throws = 0
    player1Score = 0
    player1Total = 0

    BOTThrows = 0
    BOTScore = 0
    BOTTotal = 0

    difficulty = 0
    PlayerName = ""
    roll = 0
    botWon = False
    keepGoing = True
    """Skapar spelar objekt."""
    player = Player1.Player_class

    def init():
        """Välj en svårighetsgrad."""
        check = False
        while check == False:
            print("Choose difficulty: ")
            print("1 --> Hard")
            print("Hard = The BOT will get double point")
            print("2 --> Easy")
            Start.difficulty = input()
            if Start.difficulty == '1' or Start.difficulty == '2':
                check = True
            else:
                print("Invalid input\n")

        """Ber spelaren om namn."""
        print("Hello!\nWelcome to our game!")
        Start.PlayerName = input("Enter your name: ")

        """Lägget till namn och score i spelar object."""
        Start.player = Player1.Player_class(Start.PlayerName, 0)

        """Visa vem som har highscore."""
        print("\nCurrent highscore: ")
        HighScore.checkHighScore.read()

    def startPlayer():
        """Frågar spelaren om vad den vill göra."""
        keepGoing = True
        while keepGoing:
            """Printar ut spelarens poäng och kast."""
            print(f"\nTemporary Score: {Start.player1Score}")
            print(f"Throws: {Start.player1Throws}")
            print(f"Total Score: {Start.player1Total}\n")

            """Frågar spelaren om vad hen vill göra härnest."""
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
                Start.PlayerThrow()
                if Start.player1Total >= 100:
                    Start.Win()
                    keepGoing = False
            elif answer == 'C':
                Start.player1Total = 100
                Start.Win()
                keepGoing = False
            elif answer == 'N':
                print("\nYou chose to stop")
                Start.player1Score = 0
                Start.option()
            elif answer == 'W':
                newName = input("Enter new name: ")
                Start.PlayerName = newName
                Start.player.changeName(newName)
            elif answer == 'Q':
                keepGoing = False
                print("End")

    def Win():
        """Kolla om spelare har vunnit."""
        print("You win!!!")
        print(f"You threw {Start.player1Throws} times!")

        """Skicka in antalet kast till spelar objectet."""
        Start.player.ThrowScore(Start.player1Throws)

        """Om någon vinner kollar man om det är ett highscore eller inte."""
        check = HighScore.checkHighScore
        check.addHighScore(Start.player1Throws, Start.player)

        print("End")

    def PlayerThrow():
        """Add throws."""
        Start.player1Throws += 1

        """Instanciera ett object från Dice klassen."""
        die = Dice.dice

        """Använd objectet för att kastat tärningen."""
        Start.roll = die.throwDice()

        """Printa värdet som tärningen visade."""
        print("You rolled the dice!")
        Start.printValue(Start.roll)

        """Vad som ska hända om man slår en etta eller annan siffra."""
        if Start.roll == 1:
            Start.player1Total -= Start.player1Score
            Start.player1Score = 0
            Start.option()
        else:
            Start.player1Score += Start.roll
            Start.player1Total += Start.roll

    def BotThrow():
        """Instanciera ett object från Dice klassen."""
        die = Dice.dice

        """Använd objectet för att kastat tärningen och printa värdet."""
        Start.roll = die.throwDice()

        """Lägger till poäng och kast."""
        Start.BOTThrows += 1
        Start.BOTScore += Start.roll

        """Printar ut vad BOTen fick."""
        print("\nBOT rolled the dice!", flush=True)

        Start.printValue(Start.roll)
        print(flush=True)

        print(f"TemporarilyScore: {Start.BOTScore}")
        print(f"Throws: {Start.BOTThrows}")
        print(f"TotalScore: {Start.BOTTotal}\n")

        """Programmet ska vänta 2 sekunder så man hänger med i spelet."""
        time.sleep(Start.waitTime)

        """Vad som ska hända om BOTen får en etta eller annan siffra."""
        if Start.roll == 1:
            Start.BOTScore = 0
            Start.keepGoing = False

    def option():
        """Om botten ska kasta igen eller stanna."""
        Start.keepGoing = True
        while Start.keepGoing:
            """Generera en random siffra mellan 1 och 2."""
            odds = random.randint(1, 3)
            """Botten kastar igen."""
            if odds == 1 or 2:
                Start.BotThrow()
            else:
                Start.keepGoing = False
                """Svårighetsgrad appliceras beroende på tidigare val."""
                """Botten stannar."""
                if Start.difficulty == '1':
                    Start.BOTTotal += Start.BOTScore * 2
                    Start.BOTScore = 0
                    print("\nThe BOT chose to stop", flush=True)
                    print(f"TemporarilyScore: {Start.BOTScore}", flush=True)
                    print(f"Throws: {Start.BOTThrows}", flush=True)
                    print(f"TotalScore: {Start.BOTTotal}\n", flush=True)

                    Start.keepGoing = False

                    """Programmet väntar 3 sekunder."""
                    time.sleep(Start.waitTime)
                else:
                    Start.BOTTotal += Start.BOTScore
                    Start.BOTScore = 0
                    print("\nThe BOT chose to stop", flush=True)
                    print(f"TemporarilyScore: {Start.BOTScore}", flush=True)
                    print(f"Throws: {Start.BOTThrows}", flush=True)
                    print(f"TotalScore: {Start.BOTTotal}\n", flush=True)

                    Start.keepGoing = False

                    """Programmet väntar 3 sekunder."""
                    time.sleep(Start.waitTime)

                """Kollar om botten har vunnit"""
                if Start.BOTTotal >= 100:
                    print("The BOT won )=")
                    print(f"The BOT threw {Start.BOTThrows} times!!")
                    Start.keepGoing = False
                    Start.botWon = True
                    print("End")

        if not Start.botWon:
            print(f"Now its {Start.PlayerName} to play")

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
