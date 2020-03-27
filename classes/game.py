import random
from .magic import Spell
class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.hp = hp
        self.mp = mp
        self.name = name
        self.maxmp = mp
        self.maxhp = hp
        self.atkl = atk-10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0
        return  self.hp

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def get_maxhp(self):
        return self.maxhp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def heal(self,dmg):
        self.hp += dmg

    def choose_action(self):
        i = 1
        print("\n" + Bcolors.OKBLUE + Bcolors.BOLD + self.name + Bcolors.ENDC)
        print(Bcolors.OKBLUE + Bcolors.BOLD + "    ACTIONS" + Bcolors.ENDC)
        for item in self.actions:
            print("        " + str(i)+":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + Bcolors.OKBLUE + Bcolors.BOLD + "    MAGIC" + Bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i)+":", spell.name, "(cost:", str(spell.cost)+")")
            i += 1

    def choose_item(self):
        i = 1

        print("\n" + Bcolors.OKGREEN + Bcolors.BOLD + "    ITEMS" + Bcolors.ENDC)
        for item in self.items:
            print("        " + str(i)+":", item["item"].name, item["item"].description, "x", str(item["quantity"]))
            i += 1

    def chooseTarget(self,enemies):
        print("        " + Bcolors.FAIL + "Target:" + Bcolors.ENDC)
        i = 1
        for enemy in enemies:
            print("        " + Bcolors.FAIL + str(i) + ":" + enemy.name + Bcolors.ENDC)
            i += 1

        tar_enemy = int(input("    choose Target"))-1
        return tar_enemy

    def get_enemy_stats(self):
        hp_bar = ""
        hp_sticks = self.hp / self.maxhp * 100 / 2
        while hp_sticks > 0:
            hp_bar += "█"
            hp_sticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "
        print(Bcolors.BOLD + self.name + "           " +
              str(self.hp) + "/" + str(self.maxhp) + " |" + Bcolors.FAIL + hp_bar + Bcolors.ENDC + "|    " +
              Bcolors.BOLD + Bcolors.ENDC)

    def set_stats(self):
        hp_bar = ""
        hp_sticks = self.hp/self.maxhp * 100/4
        while hp_sticks > 0:
            hp_bar += "█"
            hp_sticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        mp_bar = ""
        mp_sticks = self.mp / self.maxmp * 100 / 10
        while mp_sticks > 0:
            mp_bar += "█"
            mp_sticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        print(Bcolors.BOLD + self.name + "           " +
              str(self.hp) + "/" + str(self.maxhp) + " |" + Bcolors.OKGREEN + hp_bar + Bcolors.ENDC + "|    " +
              Bcolors.BOLD + str(self.mp) + "/" + str(self.maxmp) + "|" + Bcolors.OKBLUE + mp_bar + Bcolors.ENDC + "|\n")
