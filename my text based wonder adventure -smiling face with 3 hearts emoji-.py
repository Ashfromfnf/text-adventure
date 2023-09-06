import time

hp = 100
atkdmg = 10

def start():
    print("HP: " + str(hp))
    print("You enter a very dark dungeon, there are two doors, one on the left and one on the right.")
    answer = input('Which one do you go through?: ')

    if answer == "left" or answer == "l":
        print("you went left!!")
        print(answer)
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
    if answer == "y" or "yes":
        print("You pull out the sword! (+50 atk)")
        atkdmg += 50
        room_3()
    elif answer == "n" or "no":
        print("You don't pull out the sword and keep going")

def room_3():
    global hp
    print("You continue walking until you see a huge rubber duck! Do you attack?")
    answer = input("y/n: ")
    if answer == "y":
        print("You hit the duck once!")
        print("The duck hits you! ( " + str(100) + "-" + "40" + "=" + str(hp-40))
        print("Do you hit the duck again?")
        answer = input("y/n: ")
        if answer == "y" or answer == "yes":
            HP = 100
            ATK += 60
            print("You killed the duck! (+" + str(100-hp) + " HP, +60 ATK")
        elif answer == "n" or answer == "no":
            print("You died!")
            time.sleep(10)
            exit()


start()