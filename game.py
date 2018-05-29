import random

import time


class Bgcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLUE = '\033[96m'


class Person:
    def __init__(self, name, hp, mp, atck, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atckl = atck - 10  # 50
        self.atckh = atck + 10  # 70
        self.df = df
        self.items = items
        self.magic = magic
        self.Action = ["Attack", "MAGIC", "ITEMS"]
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atckl, self.atckh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
            return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n" + Bgcolors.BOLD + "    " + self.name + Bgcolors.ENDC)
        print("\n", Bgcolors.BOLD + Bgcolors.OKBLUE + "    Actions: " + Bgcolors.ENDC)
        for item in self.Action:
            print("    " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n", Bgcolors.BOLD + Bgcolors.OKBLUE + "    Magic: " + Bgcolors.ENDC)
        for spell in self.magic:
            print("    " + str(i) + ":", spell.name, "(cost: ", str(spell.cost) + ")")
            i += 1

    def choose_items(self):
        i = 1
        print("\n", Bgcolors.BOLD + Bgcolors.OKBLUE + "    Items: " + Bgcolors.ENDC)
        for items in self.items:
            print("    " + str(i) + ".", items["item"].name, ": ", items["item"].description, " (x",
                  str(items["quantity"]), ")")
            i += 1

    def choose_target(self, enemies):
        i = 1
        print("\n", Bgcolors.BOLD + Bgcolors.FAIL + "    Target: " + Bgcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("    " + str(i) + ".", enemy.name)
                i += 1
        choice = int(input("    Choose target: ")) - 1
        return choice

    def intro(self):
        time.sleep(1)
        print(Bgcolors.OKBLUE, "\n\t*****************************************************\n\t", Bgcolors.ENDC)
        time.sleep(1)
        print(Bgcolors.UNDERLINE+Bgcolors.BOLD+Bgcolors.BLUE+"\t\tINSTRUCTIONS"+Bgcolors.ENDC)
        time.sleep(1)
        print(
            Bgcolors.BOLD + Bgcolors.WARNING + "\n\t* HEY, MY NAME IS AYUSH SHARMA also known as KRONO$ " + Bgcolors.ENDC)
        time.sleep(1)
        print(Bgcolors.OKGREEN, "\n\t* I Welcome you to the Wicked World!", Bgcolors.ENDC)
        time.sleep(1)
        print(Bgcolors.OKGREEN,
              "\n\t* This is a game 3 player game", Bgcolors.ENDC)
        time.sleep(1)
        print(Bgcolors.OKGREEN,
              "\n\t* This game has 3 monsters" + Bgcolors.FAIL + " Voldemort, Vimp & Vector" + Bgcolors.ENDC)
        time.sleep(1)
        print(Bgcolors.OKGREEN,
              "\n\t\t* You can Attack your enemy by 3 methods" +
              "\n\t\t1. Attack them with your Hit points\n\t\t2. Using magic Spells",
              "\n\t\t3. Using of magic items(just 1 'Grenades')",
              "\n\n\t* Magic Items will Heal your Health..."
              , Bgcolors.ENDC)
        time.sleep(1)
        print(Bgcolors.OKGREEN, "\n\t* You have 500 HIT-POINTS\n\n\t* You got 65 MAGIC POINTS", Bgcolors.ENDC)
        time.sleep(1)
        print(Bgcolors.OKGREEN, "\n\t* You got 60 ATTACK POWER!\n\n\t* AND Also got 3 MAGIC Spells", Bgcolors.ENDC)
        time.sleep(1)
        print(Bgcolors.OKGREEN, "\n\t* EACH ATTACK COSTS RANDOM MAGIC POINTS", Bgcolors.ENDC)
        time.sleep(1)
        print(Bgcolors.OKGREEN,
              "\n\t* AND EACH MAGIC SPELL HAVE DIFFERENT COSTS\n\n\t* There is a healing spell and items in the List",
              Bgcolors.ENDC)
        time.sleep(1)
        print(Bgcolors.OKGREEN,
              "\n\t* The enemy will heal themselves automatically", Bgcolors.ENDC)
        time.sleep(0.5)
        print(Bgcolors.FAIL,
              "\n\t* Be careful with the numbers, use numbers which are in the list"+Bgcolors.ENDC)
        time.sleep(0.5)
        print(Bgcolors.OKBLUE, "********************************************************", Bgcolors.ENDC)
        time.sleep(1)
        print(Bgcolors.OKBLUE,
              "\n\t* Hope you'll like it...", Bgcolors.ENDC)
        time.sleep(1)

    def get_stats(self):

        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 25

        mp_bar = " "
        mp_ticks = (self.mp / self.maxmp) * 10

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar += " "

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        while len(hp_bar) < 25:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_hp = ""
        current_mp = ""
        if len(hp_string) < 7:
            decreased = 7 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        if len(mp_string) < 5:
            decreased = 5 - len(mp_string)

            while decreased > 0:
                current_mp += " "
                decreased -= 1

            current_mp += mp_string
        else:
            current_mp = mp_string

        print("                 _______________________________________           _________________")
        print(
            Bgcolors.BOLD + self.name + "    " +
            current_hp + "|" + Bgcolors.OKGREEN + hp_bar + Bgcolors.ENDC + "|    " +
            current_mp + " |" + Bgcolors.OKBLUE + mp_bar + Bgcolors.ENDC + "|")

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 50

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""
        if len(hp_string) < 10:
            decreased = 10 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                       _______________________________________________________________________________")
        print(
            Bgcolors.BOLD + self.name + "    " +
            current_hp + "|" + Bgcolors.FAIL + hp_bar + Bgcolors.ENDC + "|")

    def choose_enemy_spell(self):

        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_gamage()

        pct = (self.hp / self.maxhp) * 100
        if self.mp < spell.cost or spell.type == "WHITE MAGIC" and pct > 50:
            self.choose_enemy_spell()
        else:
            return spell, magic_dmg
