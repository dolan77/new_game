import random
# if i want to refer to anything in the player.py file, use p.(thing i'm referring to)
from enemies_and_players import player as p


class Enemy:
    # constructor: gives the variable these types of attributes (variable_name.attribute)
    def __init__(self, n, lvl, st):
        self.name = n
        self.level = lvl
        self.stat = st


# function that prints the enemy HUD
def enemy_hud():
    print("{}\nLVL: {}\nHP: {}".format(enemy.name.upper(), enemy.level, enemy_stats[0]))


# function that will grab a random name of an enemy from a list
def enemy_spawn():
    name_list = ["Slime", "Goblin", "Imp", "Snake", "Baboon"]

    return random.choice(name_list)


# enemy_numbers is a list of numbers that the enemy will use for their health, attack, defense and speed stat.
enemy_numbers = [5, 5, 5, 4, 3, 4, 5, 1, 2]

# will pull a random number in the enemy_numbers list for the enemy's health, attack, defense, speed
enemy_stats = [random.choice(enemy_numbers), random.choice(enemy_numbers), random.choice(enemy_numbers),
               random.choice(enemy_numbers)]

# variable that creates an enemy from the Enemy class
enemy = Enemy(enemy_spawn(), p.player.level + random.randint(-2, 2), enemy_stats)

# will keep rolling for a new level if the enemy's level is less than 0
while enemy.level <= 0:
    enemy.level = p.player.level + random.randint(-2, 2)
