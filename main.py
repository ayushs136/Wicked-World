from CLASSES.game import Person, Bgcolors
import random
# import  time
from CLASSES.magic import Spell
from CLASSES.inventory import Items

# CREATE BLACK MAGIC
fire = Spell("FIRE", 10, 100, "BLACK MAGIC")
thunder = Spell("Thunder", 10, 124, "BLACK MAGIC")
blizzard = Spell("Blizzard", 10, 100, "BLACK MAGIC")
meteor = Spell("Meteor", 20, 200, "BLACK MAGIC")
quake = Spell("Quake", 12, 120, "BLACK MAGIC")

# CREATE WHITE MAGIC
cure = Spell("Cure", 12, 120, "WHITE MAGIC")
cura = Spell("Cura", 10, 200, "WHITE MAGIC")
curaga = Spell("Curaga", 30, 400, "WHITE MAGIC")

# CREATE SOME ITEMS
potion = Items("Potion", "potion", "Heals 50 HP", 50)
hipotion = Items("Hi-potion", "potion", "Heals 100 HP", 100)
superpotion = Items("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Items("Elixer", "elixer", "Fully restore HP/MP of one party member", 9999)
hielixer = Items("MEGA-Elixer", "elixer", "Fully restore HP/MP", 9999)

granade = Items("Granade", "attack", "Deals 500 Damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
enemy_spells = [fire, meteor, curaga]
player_items = [{"item": potion, "quantity": 15},
                {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5},
                {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 5},
                {"item": granade, "quantity": 5}]

player1 = Person("KRONO", 500, 65, 60, 34, player_spells, player_items)
player2 = Person("BILLA", 500, 65, 60, 34, player_spells, player_items)
player3 = Person("AYUSH", 500, 65, 60, 34, player_spells, player_items)

enemy1 = Person("Vector   ", 1000, 65, 45, 25, enemy_spells, [])
enemy2 = Person("Voldemort", 1000, 65, 45, 25, enemy_spells, [])
enemy3 = Person("Vimp     ", 1000, 65, 45, 25, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

enemy1.intro()

# time.sleep(1)
print(Bgcolors.FAIL + Bgcolors.HEADER + "An Enemy Attacks!" + Bgcolors.ENDC)

i = 0
running = True

while running:

    print("\n\n")
    print(
        Bgcolors.BLUE + "////////////////////////////////////////////////////////////////////////////////" + Bgcolors.ENDC)
    print("NAME                  HP: HIT-POINTS                          MP: MAGIC-POINTS")
    for player in players:
        # time.sleep(0.6)
        player.get_stats()
    print("\n")
    for enemy in enemies:
        enemy.get_enemy_stats()
    for player in players:

        # time.sleep(0.5)
        print(Bgcolors.FAIL, "=========================================================", Bgcolors.ENDC)
        # time.sleep(0.5)
        print(player.choose_action())
        # time.sleep(0.5)
        choice = input("    Choose Action: ")

        index = int(choice) - 1
        # ATTACK SECTION
        if index == 0:

            dmg = player.generate_damage()

            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace(" ", "") + " has died.")
                del enemies[enemy]

            # time.sleep(0.5)
            print(Bgcolors.BLUE, "You Attack for " + enemies[enemy].name.replace(" ", "") + " for ", dmg,
                  " points of Damage. ",
                  Bgcolors.ENDC)

        # MAGIC SECTION
        elif index == 1:
            # time.sleep(0.5)
            player.choose_magic()
            # time.sleep(0.5)
            magic_choice = int(input("    Choose magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_gamage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                # time.sleep(0.5)
                print(Bgcolors.FAIL, "\n NOT ENOUGH MP\n", Bgcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "WHITE MAGIC":
                player.heal(magic_dmg)
                print(Bgcolors.OKBLUE, "\n", spell.name, " Heals for ", str(magic_dmg), " HP. ", Bgcolors.ENDC)

            elif spell.type == "BLACK MAGIC":
                # time.sleep(0.5)
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(Bgcolors.OKBLUE, "\n", spell.name, "Deals", str(magic_dmg),
                      "points of damage to " + enemies[enemy].name.replace(" ", "") + Bgcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    del enemies[enemy]
        # ITEMS SECTION
        elif index == 2:
            # time.sleep(0.5)
            player.choose_items()
            # time.sleep(0.5)
            item_choice = int(input("    Choose Item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(Bgcolors.FAIL, "\nNone Left...", Bgcolors.ENDC)

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(Bgcolors.OKGREEN, "\n", item.name, " heals for ", str(item.prop), "HP", Bgcolors.ENDC)

            elif item.type == "elixer":

                if item.name == "MEGA-Elixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(Bgcolors.OKGREEN, "\n", item.name, " Fully restores HP/MP ", Bgcolors.ENDC)

            elif item.type == "granade":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print(Bgcolors.WARNING, "\n", item.name, " deals ", str(item.prop), " points of damage to ",
                      enemies[enemy].name, Bgcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    del enemies[enemy]

    defeated_e = 0
    defeated_p = 0
    # check if battle is over
    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_e += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_p += 1

    # check if enemy defeated
    if defeated_e == 2:
        print(Bgcolors.OKGREEN, "\n\n\tYou Win!!!", Bgcolors.ENDC)
        running = False

    # check if players defeated
    elif defeated_p == 2:
        # time.sleep(0.5)
        print(Bgcolors.FAIL, "You just Lost", Bgcolors.ENDC)
        running = False

    # enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)

        if enemy_choice == 0:
            target = random.randrange(0, 3)
            enemy_dmg = enemy.generate_damage()
            players[target].take_damage(enemy_dmg)
            print(Bgcolors.FAIL, enemy.name.replace(" ", ""),
                  " attacks " + players[target].name.replace(" ", "") + " for = ", enemy_dmg, Bgcolors.ENDC)
            # time.sleep(1)

        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)
            if spell.type == "WHITE MAGIC":
                enemy.heal(magic_dmg)
                print(Bgcolors.OKBLUE, "\n", spell.name, " Heals" + enemy.name + " for ", str(magic_dmg), " HP. ",
                      Bgcolors.ENDC)

            elif spell.type == "BLACK MAGIC":
                # time.sleep(0.5)
                target = random.randrange(0, 3)
                players[target].take_damage(magic_dmg)

                print(Bgcolors.OKBLUE, "\n", enemy.name.replace(" ", ""), "'s ", spell.name, "Deals", str(magic_dmg),
                      "points of damage to " + players[target].name.replace(" ", "") + Bgcolors.ENDC)

                if players[target].get_hp() == 0:
                    print(players[target].name.replace(" ", "") + " has died.")
                    del players[player]
                    # print("Enemy chooses " + spell + " damage is " + magic_dmg)
