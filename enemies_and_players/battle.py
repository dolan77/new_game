import random
from enemies_and_players import enemy as e
from enemies_and_players import player as p

player = p.player
enemy = e.enemy


# try to find a way to use a switch case in Python
def battle_sys(player, enemy):
    while e.enemy.stat[0] > 0:

        e.enemy_hud()
        print()
        p.player_hud()
        print()

        # implement a fight option (more options to come) and allow the player and enemy to damage each other.
        # make sure to not change the player and enemy's health permanently but rather temporarily for the battle
        # after battle ends player will go back to full HP and could have a chance of leveling up
        options = {"FIGHT": 1, "RUN": 2}
        choice = input("> FIGHT\n"
                       "> RUN\n")

        while choice.upper() not in options:
            choice = input("Please enter a valid choice\n> Fight\n> Run\n")

        print(options.get(choice.upper()))


battle_sys(player, enemy)
