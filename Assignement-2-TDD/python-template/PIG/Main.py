"""Detta motsvarar vår main -> vår meny"""


def main():
    check = False
    while check == False:
        print("Pvp --> press '1'")
        print("PvE --> press '2'")
        answer = input()
        if answer == '1' or answer =='2':
            check = True
        else:
            print("Invalid input")

   
    print("\nInstructions: ")
    print("1. Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to hold:")
    print("2. If the player rolls a 1, they score nothing and it becomes the next player's turn")
    print("3. If the player rolls any other number, it is added to their turn total and the player's turn continues.")
    print("4. If a player chooses to hold, their turn total is added to their score, and it becomes the next player's turn.")
    print("5. The first player to score 100 or more points wins.")
    print("6. If you choose to cheat you will immediately get 100 point and win the game\n")

    if answer == '1':
        import PvP
        PvP.Start.startPlayer1()
    else:
        import PvE
        PvE.Start.startPlayer()

if __name__ == "__main__":
    main()