import random


class Player:
    def __init__(self, n, t, lvl, hp, atk, spd, d, exp):
        self.name = n
        self.title = t
        self.level = lvl
        self.health = hp
        self.attack = atk
        self.speed = spd
        self.defense = d
        self.experience = exp

    def leveling(self):
        self.level = self.level + 1

        # rolls for adding random stats to health, attack, speed and defense respectively when the player levels up
        self.health = self.health + random.randint(2, 5)
        self.attack = self.attack + random.randint(1, 3)
        self.speed = self.speed + random.randint(1, 3)
        self.defense = self.defense + random.randint(1, 3)


def player_hud():
    print("{}\nLVL: {}\nHP: {}".format(player.name.upper(), player.level, player.health))


# from element 0 through 3: health, attack, speed, defense
initial_stat = [10, 5, 5, 5]

# creates a player from the player class with certain attributes starting from left moving to right:
# player name, player title, health, attack, speed, defense, experience
player = Player("Cheese", "Hero", 1, initial_stat[0], initial_stat[1], initial_stat[2], initial_stat[3], 0)

# print("HEALTH: {}\nATK: {}\nDEF: {}\nSPD: {}".format(player.health, player.attack, player.defense, player.speed))

# print(player.level)
