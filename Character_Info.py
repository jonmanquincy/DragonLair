from random import randint


class Character:
    experience = 1
    lvl = 1 + int(experience / 100)
    able_to_attack = True

    def __init__(self, max_hp, mp, lvl, attack, speed, moves=None):
        self.max_hp = max_hp
        self.mp = mp
        self.lvl = lvl
        self.attack = attack
        self.speed = speed
        self.moves = moves
        self.current_hp = 0

    def update_level(self, num):
        self.lvl += num

    def update_stats(self):
        self.max_hp += 3 * self.lvl
        self.attack += self.lvl
        self.speed += self.lvl
        print("Your HP is {0}, your attack is {1}, and your speed is {2}".format(self.max_hp, self.attack, self.speed))


# Different types of Characters.

class Fighter(Character):
    def __init__(self, max_hp, mp, lvl, attack, speed):
        super().__init__(max_hp, mp, lvl, attack, speed, moves=None)
        if self.moves is None:
            self.moves = {"Attack": randint(10, 20) + (self.attack * .5),
                          "Defend": "Take no damage one turn.",
                          "Rage": "Next turn triple damage"
                          }
