import random
from enemies_and_players import enemy as e
from enemies_and_players import player as p
from enemies_and_players import items as item
player = p.player
enemy = e.enemy

# initializing the experience the player has and the experience needed to move onto the next level
next_lvl = 25


def fight():
    # calculates the player's damage against the enemy, if the player deals less than or equal to 0 damage
    # sets the damage to 1
    damage_dealt = e.enemy.stats[2] - player.attack
    if damage_dealt <= 0:
        damage_dealt = 1

    # calculates the enemy's damage against the player, if the enemy deals less than or equal to 0 damage
    # sets the damage to 1
    damage_received = player.defense - e.enemy.stats[2]
    if damage_received <= 0:
        damage_received = 1

    # prints the damage received and dealt
    print("\nYou dealt {} damage to the enemy!".format(damage_dealt))
    print("The enemy dealt {} damage to you!\n".format(damage_received))

    # changes the enemy's and player's health after the damage is dealt / received
    e.enemy.stats[0] -= damage_dealt
    p.player.health -= damage_received


# try to find a way to use a switch case in Python
def battle_sys():
    while e.enemy.stats[0] > 0:

        e.enemy_hud()
        print()
        p.player_hud()
        print()

        # implement a fight option (more options to come) and allow the player and enemy to damage each other.
        # make sure to not change the player and enemy's health permanently but rather temporarily for the battle
        # after battle ends player will go back to full HP and could have a chance of leveling up
        options = {"FIGHT": 1, "RUN": 2}
        choice = input("> FIGHT\n"
                       "> RUN\n"
                       "> ITEMS\n")

        while choice.upper() not in options:
            choice = input("Please enter a valid choice\n> FIGHT\n> RUN\n")

        # screw it, I'll use if/else statements for now
        if choice.upper() == "FIGHT":
            fight()
        # print(options.get(choice.upper()))

        elif choice.upper() == "RUN":
            item.items()


def experience():
    global next_lvl
    # the player's experience will be determined from the enemy's level * 3
    # will start to accumulate as the player defeats more enemies
    p.player.experience += e.enemy.stats[0] * 3

    # while the experience the has is greater than what is needed to level up, execute the loop
    while p.player.experience >= next_lvl:
        # increase the player's level by 1 and subtract the exp from the exp needed to level up
        p.player.experience -= next_lvl

        # will increase the exp needed to level up as the player levels up
        next_lvl = round(next_lvl * 1.5)

        # will call the level_up function and increase the player's level by 1 and all their stats from 1-3
        p.player.level_up()

        print("You leveled up! ALL stats are increased!")

    # if the player doesn't level up after a battle will print the experience gained in the battle
    print('You gained {} experience!\n'.format(p.player.experience))

    # prints the level of the player, their progress bar of their experience and the experience needed to level up
    print('LVL: {}\n'
          'PROGRESS BAR: {}%\n'
          'EXP NEEDED UNTIL YOU REACH THE NEXT LVL: {}'.format(p.player.level,
                                                               int((p.player.experience / next_lvl) * 100),
                                                               next_lvl - p.player.experience))

    print("HP: {} ATK: {} DEF: {} SPD: {}\n".format(p.player.max_health, p.player.attack, p.player.defense,
                                                    p.player.speed))


battle_sys()