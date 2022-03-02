"""Detta motsvarar vår main -> vår meny"""


from Player import Player_class


player_1 = Player_class("Samuel", 0)


player_1.show_score()
player_1.change_score(5)
player_1.show_score()

