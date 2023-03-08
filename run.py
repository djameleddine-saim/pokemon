from combat import *

Pokemon = load_monsters_from_config()

""" choisire ton pokemon et le pokemon qui tu veux affronte """
""" tout les pokemon son dans le ficher pokedex """
""" Chaque Pokémon a un nom, des points de santé, 
des points de mana, un niveau et un attribut de vitesse"""
menu(Pokemon[5], Pokemon[6])

"""Pikachu[0], Rattata[1], Bulbasaur[2], Charmander[3], Squirtle[4],
Mewtwo[5], Snorlax[6], Dragonite[7], Gyarados[8], Alakazam[9]."""