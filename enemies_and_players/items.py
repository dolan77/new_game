from enemies_and_players import player as p

# a function where the player can use their items, items for now will only include health potions that offer
# different amounts of healing

# NEW ITEMS IDEA: A TEMPORARY ATTACK UP ITEM. WILL CALCULATE DAMAGE NOW FROM player.damage + temp_damage.


def items():
    # variable for checking if the player has no potion of that type
    no_potion = 0
    # boolean variable that will be True if the player is in the item menu and false when they leave it
    in_menu = True

    # linked lists. based on the potion used, will use the healing[index] to heal the player by that amount
    potion_amount = [p.small_potion, p.medium_potion, p.EX_potion]
    healing = [10, 20, 35]

    while in_menu is True:
        # attempt at a linked list, lists the potion options and amount they have
        potion_options = ["SMALL POTION", "MEDIUM POTION", "EX POTION"]

        # will loop through the potion_amount list to check if the player has a potion
        # if so, print the potion name and amount they have
        # otherwise, print something that tells the player they don't have any potions
        for i in range(len(potion_amount)):
            if potion_amount[i] > 0:
                print("{}: {}".format(potion_options[i], potion_amount[i]))

            else:
                no_potion += 1

        # will check if the player has no potions at all, if so will print you have no potions and leave the item menu.
        # set to 3 because at the moment there are only 3 healing items.
        if no_potion == 3:
            print("You have no potions")
            in_menu = False

        # will get the user's input and check to see if it is one of the options
        choice = str(input("Please choose which item you want to use: "))
        while choice.upper() not in potion_options:
            choice = str(input("Please choose which item you want to use: "))

        # once the player has chosen the item, will check the potion_options list to find the potion the user wants to
        # use based on its index. will then subtract the potion by 1 and heal the player depending on the potion used.
        # FIXME: find a way to heal the player based on the potion used. Small = 10 HP MED = 20 HP EX = 35 HP
        for x in potion_options:
            if x == choice.upper():
                item = potion_options.index(x)
                potion_amount[item] -= 1
                break


p.small_potion = 5
p.medium_potion = 5
p.EX_potion = 5

items()
