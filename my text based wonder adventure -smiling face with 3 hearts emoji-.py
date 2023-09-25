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
        firsttime == True
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
    shroom_fight()

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

def shroom_victory():
    global inventory, hp, maxhp
    inventory.append("King Shroom's Head")
    print("Item acquired! \n King Shroom's Head \n")
    time.sleep(1.5)
    print("\n You put it on your head and look so much cooler! (+200 Swag, +60 Max HP)")
    maxhp += 60
    hp = maxhp
    time.sleep(0.25)
    print("HP:", hp)
    room_4()

def shroom_fight():
    global inventoryz, hp, maxhp
    print("""You've killed all the shrooms except for one... the king. You're standing face-to-face with him, he looks you deep in your eyes and cracks his knuckles; "This will be an easy fight" """)
    time.sleep(0.5)
    print("""You pull out your trusty sword and stare him into the eyes and say "Your head will be mine" """)
    answer = input("Do you: \n A: Run towards him with your sword pointed towards his heart \n B: Try to slice off his head clean. \n C: Run away, he's scary \n D: Stab yourself \n E: Insult him until he forfeits \n").lower()

    if answer == "a":
        print("""You charge towards him will all your speed, impaling his heart with your sword. He's gagging up purple blood(?). With his last breath, he says "Well done, kid" """)
        shroom_victory()
    
    elif answer == "b":
        print("""You run towards him, with your sword positioned to your right, in both hands. Once you're close enough, you try to slice off his head. You only give him a little cut on on the neck. \n You can see his purple blood-like substance go down his neck and onto his torso. \n But to your surprise, the wound healed itself \n He says; "Is that all you got, huh" and tries to eat your face""")
        time.sleep(2.5)
        print("He's on your face and nibbling on your nose, what do you do?")
        answer = input("Do you: \n A: Scream like a child \n B: Bite him back \n").lower()
        if answer == "a":
            print("You scream in the shroom's face, he covers his ears and runs off.")
            time.sleep(0.5)
            print("Well, that was easy")
            room_4()
        elif answer == "b":
            print("You bite the shroom, he screams in pain and lies down on the fungus-infested floor.")
            time.sleep(0.45)
            print("You then take your sword and thrust it through his evil heart.")
            shroom_victory()
    elif answer == "c":
        print("You run as fast as you can away from him, until you see another room...")
        room_4()
    elif answer == "d":
        print("You stab yourself. You died.")
        time.sleep(5)
    elif answer == "e":
        print("You say that his nose looks wonky")
        time.sleep(3.5)
        print("He starts crying and runs away!")
        room_4()



def room_5():
    global inventory
    print("You're still exhaused by the fight with the duck, but you keep going \n You see three doors, which one do you go through?")
    answer = input("1/2/3:  ").lower
    if answer == "!":
        print("You see Magne, your programming teacher, he gives you a generous 6/6 on your programming task. \n You say thanks, and he vanishes, just as suddenly as he appeared")
        inventory.append("Certificate of Getting The Best Grade")
        print("Item aquired! \n Certificate of Getting The Best Grade \n \n")
        print("this is it.")
        time.sleep(5)
    if answer == "2":
        print("""You see complete nothingness. Darkness. A voice that sounds like it comes from everywhere says: \n "You've escaped the simulation, the goal of many, but reality of only a select few. You have won." \n You see a lot of green ones and zeros scroll down fast, \n then you feel at peace, as if you've been stressed your whole life and finally sat down on the couch. \n You feel happy for once, you feel content with your life. You don't regret anything""")
        time.sleep(5)
    if answer == "3":
        print("You somehow teleport into the realms of Minecraft. Everything turns blocky, even yourself. You get a sudden urge to mine diamonds, and do so.")
        print("Item aquired! \n A Minecraft Diamond! \n \n")
        inventory.append("Minecraft Diamond")
        time.sleep(5)
    




print("inv:", inventory)
start()
firsttime = True
print("This is the end. Here's some stats:")
print(hp + "/" + maxhp, "HP")
print(atkdmg, "ATK")

print("inv:", inventory)


# I would have done more with like keys and stuff, but I didn't really find anywhere where it would be suitable, sorry! :c