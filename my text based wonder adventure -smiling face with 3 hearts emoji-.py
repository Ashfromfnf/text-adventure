import time
import random

hp = 100
atkdmg = 10
firsttime = True
swordtime = 0


def start():
    global firsttime
    if firsttime == True:
        print("HP: " + str(hp))
        print("You enter a very dark dungeon, there are two doors, one on the left and one on the right.")
        firsttime = False
    answer = input('Which one do you go through?: ')

    if answer == "left" or answer == "l":
        print("you went left!!")
        room_1()

    elif answer == "right" or answer == "r":
        print("you went right!")
        room_2()

    else:
        print("invalid input")
        start()


def room_1():
    global hp
    print("You see your mother. She kills you. You're dead lmfao")
    hp -= hp
    print("HP: " + str(hp))
    time.sleep(10)
    exit()

def room_2():
    global atkdmg
    print("There's a sword stuck in a rock on the floor. Do you pull it out?")
    answer = input("y/n: ")
    if answer == "y" or answer == "yes":
        print("You pull out the sword! (+50 atk)")
        atkdmg += 50
        room_3()
    elif answer == "n" or answer == "no":
        print("You don't pull out the sword and keep going")
        swordtime += 1
        room_4()
    else:
        print("Invalid input!")
        room_2()

def room_3():
    global hp, atkdmg
    print("You continue walking until you see a huge rubber duck! Do you attack?")
    answer = input("y/n: ")
    if answer == "y":
        print("You hit the duck once!")
        print("The duck hits you! ( " + str(100) + "-" + "40" + "=" + str(hp-40))
        print("Do you hit the duck again?")
        answer = input("y/n: ")
        if answer == "y" or answer == "yes":
            hp = 100
            atkdmg += 60
            print("You killed the duck! (+" + str(100-hp) + " HP, +60 ATK")
        elif answer == "n" or answer == "no":
            print("You died!")
def duck_attack():
    global firsttime
    global hp
    global atkdmg
    global duckhp
    if firsttime == True:
        duckhp = 100
        print("Do you attack the duck?")
        answer = input("y/n: ")
    if firsttime == False or answer == "y" or answer == "yes":
        print("You hit the duck! (Duck's HP: " + str(duckhp+atkdmg), "-", str(duckhp) + ")")
        print("The duck hits you! (HP: " + str(hp) + "-" + "40" + "=" + str(hp-40))
        firsttime = False
    
        
        if duckhp <= 0:
            hp = 100
            atkdmg += 60
            print("You killed the duck and ate it's meat! (+" + str(100-hp) + " HP, +60 ATK")
        
        if hp <= 0:
            print("The duck killed you! :c")
            time.sleep(10)
            exit()

        else:
            print("Do you hit the duck again?")
            answer = input("y/n: ")
            if answer == "yes" or "y":
                duck_attack()

    elif answer == "n" or answer == "no":
        print("The duck killed you! Oh noes")
        time.sleep(10)
        exit()

def room_3():
    global firsttime
    global hp
    global atkdmg
    print("You continue walking until you see a huge rubber duck!")
    firsttime = True
    duck_attack()

def room_4():
    global swordtime
    if swordtime >= 0:
        print("This is a plothole, you were supposed to pull out the sword")
        room_2()
    if swordtime == 1:
        print("Seriously, again?")
        room_2()
    if swordtime == 2:
        print("I'm tired of this...")
        print("The narrator stabs you with the sword.")
        time.sleep(10)
        firsttime == True
        start()



start()


