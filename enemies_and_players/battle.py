import random
from enemies_and_players import enemy as e
from enemies_and_players import player as p

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


# a function where the player can use their items, items for now will only include health potions that offer
# different amounts of healing
def items():
    # variable for checking if the player has no potion of that type
    no_potion = 0
    # boolean variable that will be True if the player is in the item menu and false when they leave it
    in_menu = True

    # attempt at a linked list, lists the potion options and amount they have
    potion_options = ["Small Potion", "Medium Potion", "EX Potion"]
    potion_amount = [p.small_potion, p.medium_potion, p.EX_potion]

    # will loop through the potion_amount list to check if the player has a potion
    # if so, print the potion name and amount they have
    # otherwise, print something that tells the player they don't have any potions
    # FIXME: want the index of the potion that holds the item amount of potions the user has but it instead returns
    #  the amount of potions, ruining the system
    for i in range(len(potion_amount)):
        if i > 0:
            print("{}: {}".format(potion_options[i], potion_amount[i]))

        else:
            no_potion += 0


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
                       "> RUN\n")

        while choice.upper() not in options:
            choice = input("Please enter a valid choice\n> FIGHT\n> RUN\n")

        # screw it, I'll use if/else statements for now
        if choice.upper() == "FIGHT":
            fight()
        # print(options.get(choice.upper()))


def experience():
    global next_lvl
    # the player's experience will be determined from the enemy's level * 3
    # will start to accumulate as the player defeats more enemies
    p.player.experience += e.enemy.stats[0] * 3

    # while the experience the has is greater than what is needed to level up, execute the loop
    while p.player.experience >= next_lvl:
        # increase the player's level by 1 and subtract the exp from the exp needed to level up
        p.player.level += 1
        p.player.experience -= next_lvl

        # will increase the exp needed to level up as the player levels up
        next_lvl = round(next_lvl * 1.5)

        # increases all of the player's stats when they level up
        p.player.health += 5
        p.player.attack += 3
        p.player.defense += 3
        p.player.speed += 3

        print("You leveled up! ALL stats are increased!")
        print("HP: {} ATK: {} DEF: {} SPD: {}\n".format(p.player.health, p.player.attack, p.player.defense,
                                                        p.player.speed))

    # if the player doesn't level up after a battle will print the experience gained in the battle
    print('You gained {} experience!\n'.format(p.player.experience))
    # prints the level of the player, their progress bar of their experience and the experience needed to level up
    print('LVL: {}\n'
          'PROGRESS BAR: {}%\n'
          'EXP NEEDED UNTIL YOU REACH THE NEXT LVL: {}'.format(p.player.level,
                                                               int((p.player.experience / next_lvl) * 100),
                                                               next_lvl - p.player.experience))


p.EX_potion = 4
p.medium_potion = 4
p.small_potion = 4

items()
