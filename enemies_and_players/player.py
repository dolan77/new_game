import random

# initializing how many potions the player will have, each one will give a different amount of healing
small_potion = 0
medium_potion = 0
EX_potion = 0


class Player:
    def __init__(self, n, t, lvl, hp, atk, spd, d, exp, max_hp):
        self.name = n
        self.title = t
        self.level = lvl
        self.health = hp
        self.attack = atk
        self.speed = spd
        self.defense = d
        self.experience = exp
        self.max_health = max_hp

    def level_up(self):
        self.level = self.level + 1

        # rolls for adding random stats to health, attack, speed and defense respectively when the player levels up
        self.max_health += random.randint(2, 5)
        self.attack += random.randint(1, 3)
        self.speed += random.randint(1, 3)
        self.defense += random.randint(1, 3)


def player_hud():
    print("{}\nLVL: {}\nHP: {}".format(player.name.upper(), player.level, player.health))


def max_health(new_health):
    if new_health >= player.max_health:
        player.health = player.max_health


# from element 0 through 3: health, attack, speed, defense
initial_stat = [10, 5, 5, 5]

# creates a player from the player class with certain attributes starting from left moving to right:
# player name, player title, health, attack, speed, defense, experience, max_hp
player = Player("Cheese", "Hero", 1, initial_stat[0], initial_stat[1], initial_stat[2], initial_stat[3], 0, 20)

# print("HEALTH: {}\nATK: {}\nDEF: {}\nSPD: {}".format(player.health, player.attack, player.defense, player.speed))

# print(player.level)
