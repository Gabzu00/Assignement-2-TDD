"""Detta motsvarar vår main -> vår meny"""

from Player import Player_class

def main():
    print("Hello welcome to the PIG game")
    print("")




player_1 = Player_class("Samuel", 0)


player_1.show_score()
player_1.change_score(5)
player_1.show_score()

if __name__ == "__main__":
    main()