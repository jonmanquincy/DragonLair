from Character_Info import Fighter
from Monster_Info import Slime
from Monster_Info import Wyvern
from Monster_Info import Golem
from random import randint
import Choices
slime = Slime(50, 5, 5)
wyvern = Wyvern(75, 5, 20)
golem = Golem(100, 5, 5)
fighter = Fighter(50, 1, 1, 5, 5)
turn_num = 1
characters_turn = True
monsters_turn = False
# The goal will be to for it to only give new turns if both the Character and Monster are alive.


# Hopefully make a fool proof way of making sure if Characters speed is > than Monsters speed that they get the first
# Turn before switching back and forth.
player_turn = None
monsters_turn = None
if player_turn == False:
    monsters_turn = True
turn_count = 0
poison = False
poison_count = 0
rage = False
split = False
split_num = 0
player_wins = False
fighter.current_hp += fighter.max_hp
print("""
You are leaving home to find the riches stored in the fabled Dragon's lair.
Hopefully there isn't too many dangers on the way. - You think to yourself.
But as you leave into the fields right outside your village you are attacked!
It's a cute little slime...
Guess you have no choice but to fight?
""")

while (fighter.current_hp >= 1) and (slime.hp >= 1):
    import random
    slaps_ranint = randint(5, 10)
    attacks_ranint = randint(7, 15)
    is_alive = True
    print("-------------------------------------------------------------------------------------------------")

    turn_count += 1
    print("You are on turn number " + str(turn_count))
    if rage == True:
        print("You are enraged.")

    if split == True:
        print("Slime is split into " + str(split_num) + " extra body of slimes. ")




    if (turn_count == 1) and fighter.speed > slime.speed:
        characters_turn = True
    else:
        monsters_turn = True



    #Trying to set up player input for turns
    if characters_turn == True:
        print("Please insert: /n 1) For Attack /n 2) Defend /n 3) For Rage")
        player_input = input("> ").lower()
        if  player_input in ("1", "Attack"):
            player_input = fighter.moves["Attack"]
        elif player_input in ("2", "Defend"):
            player_input = fighter.moves["Defend"]
            print("You used Defend and will take no damage from the next attack.")
        elif player_input in ("3", "Rage"):
            player_input = fighter.moves["Rage"]
            print("You used Rage your next attack will deal triple damage.")
        else:
            print("This is not a valid option please enter either 1, 2, 3.")
            continue





    if player_input == fighter.moves["Attack"]:
        if rage == True:
            slime.hp -= (attacks_ranint * 3)
            rage = False
            print("You deal " + str(attacks_ranint) + " times THREE from rage for a total of: " + str(attacks_ranint * 3))
        else:
            slime.hp -= attacks_ranint
            print("You deal " + str(attacks_ranint) + " Damage to the slime.")
    elif player_input == fighter.moves["Rage"]:
        print("You scream in Rage, your blood boiling.")
        rage = True
    elif player_input == fighter.moves["Defend"]:
        print("You lift your shield in defense.")




    if slime.hp >= 0:
        monsters_turn = True
    else:
        print("Slime defeated, YOU WIN!")
        break


    if monsters_turn == True:
        monster_input = randint(1, 10)
        if monster_input >= 1 and monster_input <= 8:
            monsters_turn = slime.attacks["Slap"]
        elif monster_input in (9, "Gurgle"):
            monster_input = slime.attacks["Gurgle"]
            print("The slime looks very offended and makes some questionable noises.")
        else:
            if monster_input in (10, "Split"):
                monster_input = slime.attacks["Split"]
                split = True
                split_num += 1
                print("The Slime splits into an extra slime.")
    if player_input == fighter.moves["Defend"]:
        print("You block all incoming damage!")
        print("Your HP: " + str(fighter.current_hp) + " Monsters HP: " + str(slime.hp))
    elif monsters_turn == slime.attacks["Slap"]:
        if split == True:
            fighter.current_hp -= (slaps_ranint * (split_num + 1))
            print("Slime uses Slap! Deals: " + str(slaps_ranint) + " times " + str((split_num + 1)) + " for a total of " + str((slaps_ranint * (split_num + 1))) + " Damage!")
            print("Your HP: " + str(fighter.current_hp) + " Monsters HP: " + str(slime.hp))
        else:
            fighter.current_hp -= slaps_ranint
            print("Slime uses Slap! Deals: " + str(slaps_ranint) + " Damage!")
            print("Your HP: " + str(fighter.current_hp) + " Monsters HP: " + str(slime.hp))

    else:
        print("Your HP: " + str(fighter.current_hp) + " Monsters HP: " + str(slime.hp))


    if fighter.current_hp <= 0:
        print("You have died!")
        is_alive = False
        break

if is_alive == True:
    fighter.update_level(3)
    print("You are now player level!: " + str(fighter.lvl))
    fighter.update_stats()

Choices.current_fight.traverse()
fighter.current_hp = fighter.max_hp

if Choices.the_mountains:
    while (fighter.current_hp >= 1) and (wyvern.hp >= 1):
        import random

        if poison_count == 0:
            poison = False

        print("-------------------------------------------------------------------------------------------------")
        if poison == True:
            print("You are poisoned and take 5 damage.")
            fighter.current_hp -= 5
        print("Your HP: " + str(fighter.current_hp) + " Monsters HP: " + str(wyvern.hp))
        turn_count = 0
        turn_count += 1
        print("You are on turn number " + str(turn_count))
        if rage == True:
            print("You are enraged.")


        if characters_turn == True:
            print("Please insert: /n 1) For Attack /n 2) Defend /n 3) For Rage")
            player_input = input("> ").lower()
            if  player_input in ("1", "Attack"):
                player_input = fighter.moves["Attack"]
            elif player_input in ("2", "Defend"):
                player_input = fighter.moves["Defend"]
                print("You used Defend and will take no damage from the next attack.")
            elif player_input in ("3", "Rage"):
                player_input = fighter.moves["Rage"]
                print("You used Rage your next attack will deal triple damage.")
            else:
                print("This is not a valid option please enter either 1, 2, 3.")
                continue





        if player_input == fighter.moves["Attack"]:
            if rage == True:
                wyvern.hp -= (attacks_ranint * 3)
                rage = False
                print("You deal " + str(attacks_ranint) + " times THREE from rage for a total of: " + str(attacks_ranint * 3))
            else:
                wyvern.hp -= attacks_ranint
                print("You deal " + str(attacks_ranint) + " Damage to the Wyvern.")
        elif player_input == fighter.moves["Rage"]:
            print("You scream in Rage, your blood boiling.")
            rage = True
        elif player_input == fighter.moves["Defend"]:
            print("You lift your shield in defense.")

        if wyvern.hp >= 0:
            monsters_turn = True
        else:
            print("Wyvern defeated, YOU WIN!")
            break

        if monsters_turn == True:
            monster_input = randint(1, 3)
            if monster_input == 1:
                monsters_turn = wyvern.attacks["Spit"]
                print("With some really unsetlling throat noises the Wyvern spits venom at you, POISONING YOU!")
                poison = True
                poison_count += 3

            else:
                if player_input == fighter.moves["Defend"]:
                    print("The Wyvern claws down at you but you block it with your shield!")
                else:
                    monsters_turn = wyvern.attacks["Claw"]
                    fighter.current_hp -= 10
                    print("The Wyvern strikes you with it's claws doing 10 damage!")

        if fighter.current_hp <= 0:
            print("You have died!")
            is_alive = False
            break


elif Choices.the_caverns:
    while (fighter.current_hp >= 1) and (golem.hp >= 1):
        import random
        print("-------------------------------------------------------------------------------------------------")
        print("Your HP: " + str(fighter.current_hp) + " Monsters HP: " + str(wyvern.hp))
        turn_count = 0
        turn_count += 1
        print("You are on turn number " + str(turn_count))
        if rage == True:
            print("You are enraged.")


        if characters_turn == True:
            print("Please insert: /n 1) For Attack /n 2) Defend /n 3) For Rage")
            player_input = input("> ").lower()
            if  player_input in ("1", "Attack"):
                player_input = fighter.moves["Attack"]
            elif player_input in ("2", "Defend"):
                player_input = fighter.moves["Defend"]
                print("You used Defend and will take no damage from the next attack.")
            elif player_input in ("3", "Rage"):
                player_input = fighter.moves["Rage"]
                print("You used Rage your next attack will deal triple damage.")
            else:
                print("This is not a valid option please enter either 1, 2, 3.")
                continue





        if player_input == fighter.moves["Attack"]:
            if rage == True:
                wyvern.hp -= (attacks_ranint * 3)
                rage = False
                print("You deal " + str(attacks_ranint) + " times THREE from rage for a total of: " + str(attacks_ranint * 3))
            else:
                wyvern.hp -= attacks_ranint
                print("You deal " + str(attacks_ranint) + " Damage to the Golem.")
        elif player_input == fighter.moves["Rage"]:
            print("You scream in Rage, your blood boiling.")
            rage = True
        elif player_input == fighter.moves["Defend"]:
            print("You lift your shield in defense.")

        if wyvern.hp >= 0:
            monsters_turn = True
        else:
            print("Golem defeated, YOU WIN!")
            break


