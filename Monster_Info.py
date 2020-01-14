from random import randint


class Monster:
    def __init__(self, hp, defense, speed, attacks=None):
        self.hp = hp
        self.defense = defense
        self.speed = speed
        self.attacks = attacks


class Slime(Monster):
    def __init__(self, hp, defense, speed):
        super().__init__(hp, defense, speed)
        if self.attacks is None:
            self.attacks = {"Slap": randint(5, 10), "Gurgle": None, "Split": None}




class Wyvern(Monster):
    def __init__(self, hp, defense, speed):
        super().__init__(hp, defense, speed)
        if self.attacks is None:
            self.attacks = {"Spit": None, "Claw": 10}

class Golem(Monster):
    def __init__(self, hp, defense, speed):
        super().__init__(hp, defense, speed)
        if self.attacks is None:
            self.attacks = ["Smash", "Harden", "Laser"]
# Different types of monsters.
