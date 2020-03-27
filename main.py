from classes.game import Person, Bcolors
from classes.magic import Spell
from classes.inventory import Item
import random


# Create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 180, "white")

# create Type

potion = Item("Potion", "potion", "Heal 50 HP", 50)
hipotion = Item("HI-Potion", "potion", "Heal 100 HP", 100)
superpotion = Item("Super-Potion", "potion", "Heal 1000 HP", 1000)
elixer = Item("Elexir", "elixer", "Fully restore mp/hp of one party member", 9999)
hielixer = Item("Mega-Elexir", "elixer", "Fully restore party's mp/hp ", 9999)
granade = Item("Granade", "attack", "deals 500 damage", 500)

playerItems = [{"item": potion, "quantity": 1}, {"item": hipotion, "quantity": 5},
               {"item": superpotion, "quantity": 5},
               {"item": elixer, "quantity": 5},
               {"item": hielixer, "quantity": 5},
               {"item": granade, "quantity": 5}
               ]

player1 = Person("Shubh:", 3765, 65, 430, 34, [fire, blizzard, meteor, quake, cure, cura], playerItems)
player2 = Person("Gapua:", 2819, 65, 313, 34, [fire, blizzard, meteor, quake, cure, cura], playerItems)
player3 = Person("Alexa:", 2451, 65, 212, 34, [fire, blizzard, meteor, quake, cure, cura], playerItems)

players = [player1, player2, player3]

enemy1 = Person("Moris      ", 2012, 65, 530, 35, [], [])
enemy2 = Person("Cris-Cross  ", 18202, 65, 600, 35, [], [])
enemy3 = Person("Vlexer    ", 3430, 65, 343, 35, [], [])

enemies = [enemy1, enemy2, enemy3]
running = True
print(Bcolors.FAIL + Bcolors.BOLD + "An Enemy Attcks" + Bcolors.ENDC)
while running:
    print("============================")

    print("Name                       HP                                 MP")
    print("                           --------------------------           --------------")
    for player in players:
        player.set_stats()

    print("\n")

    print("Name                          --------------------------------------------------\n")
    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:

        player.choose_action()
        choice = input("    Choose Action:")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.chooseTarget(enemies)
            enemies[enemy].take_dmg(dmg)
            print("    You attacked for " + enemies[enemy].name, Bcolors.FAIL + Bcolors.BOLD + str(dmg) + Bcolors.ENDC)
            if enemies[enemy].get_hp() == 0:
                print(Bcolors.OKGREEN + "Enemy " + enemies[enemy].name + "has died" + Bcolors.ENDC)
                del enemies[enemy]
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose Magic:")) - 1
            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_spellDmg(magic_choice)
            current_mp = player.get_mp()
            if current_mp < spell.cost:
                print(Bcolors.FAIL + "\n     Not enough mp" + Bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)
            if spell.type == "white":
                player.heal(magic_dmg)
                print(Bcolors.OKBLUE + "\n    " + spell.name + " heals for", str(magic_dmg), "HP" + Bcolors.ENDC)
            elif spell.type == "black":
                enemy = player.chooseTarget(enemies)
                enemies[enemy].take_dmg(magic_dmg)
                print(Bcolors.OKBLUE + "\n    " + spell.name + " deals", str(magic_dmg), "points of damage to" + enemies[enemy].name + Bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(Bcolors.OKGREEN + "Enemy " + enemies[enemy].name + "has died" + Bcolors.ENDC)
                    del enemies[enemy]
        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose Item:")) - 1
            if item_choice > 5:
                continue
            item = player.items[item_choice]["item"]
            if not item:
                continue
            if player.items[item_choice]["quantity"] == 0:
                print(Bcolors.FAIL, "    Not Enough quantity", Bcolors.ENDC)
                continue
            if item.type == "potion":
                player.heal(item.prop)
                print(Bcolors.OKBLUE + "\n" + item.name + " heals for", str(item.prop), "HP" + Bcolors.ENDC)
            elif item.type == "elixer":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(Bcolors.OKBLUE + "\n" + item.name + " fully recovers MP/HP", Bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.chooseTarget(enemies)
                enemies[enemy].take_dmg(item.prop)
                print(Bcolors.OKBLUE + "\n" + item.name + " deals", str(item.prop), "points of damage to " +
                      enemies[enemy].name + Bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(Bcolors.OKGREEN + "Enemy " + enemies[enemy].name + "has died" + Bcolors.ENDC)
                    del enemies[enemy]
            else:
                continue

            player.items[item_choice]["quantity"] -= 1

        else:
            continue

    defeated_enemy = 0
    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemy += 1

    defeated_player = 0
    for player in players:
        if player.get_hp() == 0:
            defeated_player += 1

    if defeated_enemy == 2:
        print(Bcolors.OKGREEN + "You Win !" + Bcolors.ENDC)
        running = False
        break
    elif defeated_player == 2:
        print(Bcolors.FAIL + "Your Enemies defeated you!" + Bcolors.ENDC)
        running = False
        break
    for enemy in enemies:
        enemyDmg = enemy.generate_damage()
        target = random.randrange(0, 3)
        players[target].take_dmg(enemyDmg)
        print(Bcolors.OKGREEN + enemy.name + Bcolors.ENDC + "Enemy attacked for ", Bcolors.FAIL + Bcolors.BOLD + str(enemyDmg) + " to " + players[target].name +
              Bcolors.ENDC)
