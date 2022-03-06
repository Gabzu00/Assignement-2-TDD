"""Detta motsvarar vår main -> vår meny"""

def main():
    print("Pvp --> press '1'")
    print("PvE --> press '2'")
    answer = input()
    
    print("\nInstructions: ")
    print("1. Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to hold:")
    print("2. If the player rolls a 1, they score nothing and it becomes the next player's turn")
    print("3. If the player rolls any other number, it is added to their turn total and the player's turn continues.")
    print("4. If a player chooses to hold, their turn total is added to their score, and it becomes the next player's turn.")
    print("5. The first player to score 100 or more points wins.\n")

    if answer == '1':
        import PvP
    else:
        import PvE
        PvE.Start()
        PvE.Start.startPlayer()

if __name__ == "__main__":
    main()