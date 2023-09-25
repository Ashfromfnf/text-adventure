import time
import random

name = ""
maxhp = 100
hp = 100
atkdmg = 10
inventory = []

firsttime = True
swordtime = 0


def start():
    global firsttime, name
    if firsttime == True:
        name = input("What is your name? -> ").lower()
        print("HP: " + str(hp))
        print("You enter a very dark dungeon, there are two doors, one on the left and one on the right.")
        firsttime = False
    answer = input('Which one do you go through?: ').lower()

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
    global atkdmg, swordtime
    print("There's a sword stuck in a rock on the floor. Do you pull it out?")
    answer = input("y/n: ").lower()
    if answer == "y" or answer == "yes":
        print("You pull out the sword! (+50 atk)")
        atkdmg += 50
        room_3()
    elif answer == "n" or answer == "no":
        swordtime += 1
        room_sword()
    else:
        print("Invalid input!")
        room_2()

def room_3():
    print("You've been walking for a while, without seeing anything of interest. \n Then you stumble upon a room with nothing but a mushroom in the middle of the room. \n You ponder if you should eat the mushroom or keep going \n The mushroom might be dangerous, but it might also aid you in battle")
    answer = input("Do you eat the mushroom? y/n: ").lower()
    if answer == "y" or answer == "yes":
        print("You lean down to pick the mushroom and hear it whisper in a language you do not understand.")
        time.sleep(1)
        print("You feel a sudden urge to eat the mushroom...")
        time.sleep(1)
        print("You feel like the mushroom is dangerous, but you can't look away from it...")
        time.sleep(1)
        print("You start to salvate while you notice yourself inching closer and closer towards the mushroom...")
        time.sleep(1)
        print("You take a big bite of the mushroom, you feel stronger than ever, it tastes amazing!")
        time.sleep(0.5)
        print("You take another bite, then another bite, and another bite, until the mushroom is eaten up. \n (+60 HP, +10 ATK)")
        maxhp += 60
        hp = maxhp
        atkdmg += 10
        time.sleep(0.75)
        print("You stand up and feel very dizzy, you pass out.")
        room_shroom()
    if answer == "n" or answer == "no":
        print("You walk past the mushroom, probably for the better. It might have been poisonous.")
        room_4()
    else:
        print("Invalid input! :/")
        room_3()


def room_shroom():
    # haha, room and shroom rhymes! :D
    print("""You wake up to 6 shroom-people dragging you along the cold dungeon floor. \n They're no taller than 50cm and they have a comically large shroomcap that almost looks like a hat \n They're chanting "Today's feast will be unmatched, we got a big, tall human, with a lot of flesh" \n They're singing and dancing, while dragging you to their camp. \n Once you arrive at their camp, their leader is sitting on his throne, with an even larger shroomcap than the others. \n He commands the other shrooms to hang you over the flame. \n You try to convince the shroomfolk that you don't taste as good as you look, they're kinda skeptical, so they carve out a decent-sized chunk of your thigh, while you're screaming and crying for help. \n One of the shroomfolk take a bite out of the chunk of thigh they cut out. \n "Oh wow, he tastes like shit" \n Another funguy takes a bite and says: "Oh yeah, you're right, here king, take a bite" \n The king takes a bite and lets you go free!""")

    print("You're still mad after they cut a big chunk out of your thigh, so when they untie you, you grab the sword you got from the stone earlier and go rampage and kill every funguy in your sight!")
    print("You've killed all the shrooms except for one... the king. You're standing face-to-face with him, he looks you deep in your eyes and cracks his knuckles,")

def duck_attack():
    global firsttime, hp, atkdmg, maxhp, duckhp



    if firsttime == True:
        duckhp = 200
        print("Do you attack the duck?")
        answer = input("y/n: ").lower()
        if answer == "y" or answer == "yes":
            duckhp -= atkdmg
            hp -= 40
            print("You hit the duck! (Duck's HP: " + str(duckhp+atkdmg), "-", str(atkdmg) + ")")
            print("The duck hits you! (HP: " + str(hp+40) + "-" + "40" + "=" + str(hp))
            firsttime = False"
        elif answer == "n" or answer == "no":
            print("The duck killed you! Oh noes")
            time.sleep(10)
    
        
    if duckhp <= 0:
        maxhp += 20
        hp = maxhp
        atkdmg += 60
        print("You killed the duck and ate it's meat! (+20 max HP, You healed fully, +60 ATK")
        
    if hp <= 0:
        print("The duck killed you! :c")
        time.sleep(10)
        

    else:
        print("Do you hit the duck again?")
        answer = input("y/n: ").lower()
        if answer == "yes" or "y":
            duckhp -= atkdmg
            hp -= 40
            print("You hit the duck! (Duck's HP: " + str(duckhp+atkdmg), "-", str(atkdmg) + ")")
            print("The duck hits you! (HP: " + str(hp+40) + "-" + "40" + "=" + str(hp))
            duck_attack()
        elif answer == "n" or answer == "no":
            print("The duck killed you! Oh noes")
            time.sleep(10)


def room_4():
    global firsttime
    global hp
    global atkdmg
    print("You continue walking until you see a huge rubber duck!")
    firsttime = True
    duck_attack()

def room_sword():
    global swordtime
    if swordtime <= 1:
        print("This is a plothole, you were supposed to pull out the sword")
        room_2()
    elif swordtime == 2:
        print("Seriously, again?")
        room_2()
    elif swordtime == 3:
        print("I'm tired of this...")
        print("The narrator stabs you with the sword.")
        time.sleep(10)



print("inv:", inventory)
start()
firsttime = True


