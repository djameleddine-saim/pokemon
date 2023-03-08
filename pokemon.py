import random
import json


class Pokemon:
    def __init__(self, name: str, health: int, mana: int, level: int, speed: int, is_player: bool):
        self.name = name
        self.health = health
        self.current_health = health
        self.mana = mana
        self.current_mana = mana
        self.level = level
        self.speed = speed
        self.current_speed = speed
        self.is_player = is_player
        self._exp = 0
        self.move_list = []
        self._level_up_base = 25

    def change_health(self, amount: int):
        self.current_health += amount
        if self.current_health < 0:
            self.current_health = 0
            return self.current_health
        elif self.current_health > self.health:
            self.current_health = self.health
            return self.current_health
        else:
            return self.current_health

    def change_mana(self, amount: int):
        self.current_mana += amount
        if self.current_mana < 0:
            self.mana = 0
            return self.current_mana
        elif self.current_mana > self.mana:
            self.current_mana = self.mana
            return self.current_mana
        else:
            return self.current_mana

    def change_speed(self, amount: int):
        self.current_speed += amount
        if self.current_speed < 0:
            self.current_speed = 0
            return self.current_speed
        else:
            return self.current_speed

    def _level_up(self):
        if self._exp > (self.level * self._level_up_base):
            self.level += 1
            self.change_health(int(self.health * 1.25))
            self.change_mana(int(self.mana * 1.25))
            self.change_speed(int(self.speed * 1.5))
            self._level_up()

    def add_exp(self, amount: int):
        self._exp += amount
        self._level_up()

    def add_move(self, move: object) -> bool:
        if len(self.move_list) < 4:
            self.move_list.append(move)
            return True
        else:
            print("Le pokemon connaît déjà 4 coups !")
            return False
