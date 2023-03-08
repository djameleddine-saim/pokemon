
from Attaque import *
def get_int_input():
    while True:
        try:
            user_input = int(input(">>> "))
        except ValueError:
            print("Sélection invalide, veuillez réessayer.")
            continue
        else:
            return user_input


def load_monsters_from_config() -> list:
    monster_list = []
    with open("pokedex.json", "r") as config:
        monsters_config = json.load(config)
    for monster in monsters_config["Pokemon"]:
        monster_list.append(
            Pokemon(
                monster["name"],
                monster["health"],
                monster["mana"],
                monster["level"],
                monster["speed"],
                False
            ))
    for move in monsters_config["move"]:
        for monster in monster_list:
            monster.move_list.append(
                Attaque(
                    move["name"],
                    move["lower"],
                    move["upper"],
                    move["target"],
                    move["cost"]
                ))
    return monster_list


def menu(player: Pokemon, npc: Pokemon):
    player.is_player = True
    print("L'ennemi {} a {} points de vie. Votre pokemon {} a {} points de vie".format(
        npc.name,
        npc.current_health,
        player.name,
        player.current_health))
    print("Choisissez une Attaque à utiliser parmi les suivants: ")
    i = 1
    for move in player.move_list:
        print("{}. {}".format(i, move.name))
        i += 1
    while True:
        move_key = get_int_input() - 1
        if move_key < 0 or move_key > 5:
            print("Coup non valide, réessayez.")
            continue
        else:
            break
    player_move_choice = player.move_list[move_key]
    if player.speed > npc.speed:
        print("Le joueur attaque en premier.")
        first = player
        second = npc
        combat(first, player_move_choice, second, second.move_list[0])
    elif npc.speed > player.speed:
        print("Les NCP attaquent en premier.")
        first = npc
        second = player
        combat(first, first.move_list[0], second, player_move_choice)
    else:
        print("Vitesse égale, le premier attaquant sera aléatoire.")
        if random.randint(0, 1) == 0:
            first = player
            second = npc
            combat(first, player_move_choice, second, second.move_list[0])
        else:
            first = npc
            second = player
            combat(first, first.move_list[0], second, player_move_choice)


def combat(attacker: Pokemon, attacker_move: Attaque, defender: Pokemon, defender_move: Attaque):
    if attacker_move.target_other:
        attacker_damage = random.randint(attacker_move.lower, attacker_move.upper)
        defender.change_health(attacker_damage*-1)
        print("{} a fait {}dégâts! {} a encore {} PV!".format(
            attacker.name,
            attacker_damage,
            defender.name,
            defender.current_health))
    else:
        attacker_damage = random.randint(attacker_move.lower, attacker_move.upper)
        attacker.change_health(attacker_damage)
        attacker.change_mana(attacker_move.cost*-1)
        print("{} a guéri pour {}!".format(
            attacker.name,
            attacker_damage,
        ))

    if defender.current_health > 0:
        if defender_move.target_other:
            attacker_damage = random.randint(attacker_move.lower, attacker_move.upper)
            attacker.change_health(attacker_damage*-1)
            print("{} a fait {}dégâts! {} a encore {} PV!".format(
                defender.name,
                attacker_damage,
                attacker.name,
                attacker.current_health))
        else:
            attacker_damage = random.randint(attacker_move.lower, attacker_move.upper)
            defender.change_health(attacker_damage)
            defender.change_mana(defender_move.cost*-1)
            print("{} a guéri pour {}!".format(
                defender.name,
                attacker_damage,
            ))
    elif defender.current_health <= 0 and attacker.is_player:
        print("{} a gagné! Toutes nos félicitations!".format(attacker.name))
        quit()
    elif defender.current_health <= 0 and not attacker.is_player:
        print("{} a perdu! Plus de chance la prochaine fois!".format(attacker.name))
        quit()

    if attacker.current_health > 0 and attacker.is_player:
        menu(attacker, defender)
    elif attacker.current_health > 0 and not attacker.is_player:
        menu(defender, attacker)
    elif attacker.current_health <= 0 and attacker.is_player:
        print("{} a perdu! Plus de chance la prochaine fois!".format(attacker.name))
        quit()
    elif attacker.current_health <= 0 and not attacker.is_player:
        print("{} a perdu! Toutes nos félicitations!".format(attacker.name))
        quit()
