"""Detta motsvarar vår main -> vår meny."""
from . import PvP
from . import PvE


class startMain():
    """Här startar vår program."""
    def main():
        """Frågar om spelaren vill spela PvP eller PvE."""
        check = False
        while check == False:
            print("PvP --> press '1'")
            print("PvE --> press '2'")
            answer = input()
            if answer == '1' or answer =='2':
                check = True
            else:
                print("Invalid input")
        """Instruktioner."""
        print("\nInstructions: ")
        print("1. Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to hold:")
        print("2. If the player rolls a 1, they score nothing and it becomes the next player's turn")
        print("3. If the player rolls any other number, it is added to their turn total and the player's turn continues.")
        print("4. If a player chooses to hold, their turn total is added to their score, and it becomes the next player's turn.")
        print("5. The first player to score 100 or more points wins.")
        print("6. If you choose to cheat you will immediately get 100 point and win the game\n")

        """Om spelaren svarar 1 eller 2."""
        if answer == '1':
            PvP.Start.init()
            PvP.Start.startPlayer1()
        else:
            PvE.Start.init()
            PvE.Start.startPlayer()


if __name__ == "__main__":
    startMain.main()
