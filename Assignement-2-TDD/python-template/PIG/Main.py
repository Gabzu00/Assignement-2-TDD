"""Detta motsvarar vår main -> vår meny"""

from Player import Player_class


def main():
    print("Instructions: ")
    print("1. Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to hold:")
    print("2. If the player rolls a 1, they score nothing and it becomes the next player's turn")
    print("3. If the player rolls any other number, it is added to their turn total and the player's turn continues.")
    print("4. If a player chooses to hold, their turn total is added to their score, and it becomes the next player's turn.")
    print("5. The first player to score 100 or more points wins.")
    print("")
    print("-------------------------------------------------------------------------------------------------------------")
    print("")
    print("Type cheat if you want to win faster")
    
    
player_1 = Player_class("Samuel", 0)


player_1.show_score()
player_1.change_score(5)
player_1.show_score()

if __name__ == "__main__":
    main()