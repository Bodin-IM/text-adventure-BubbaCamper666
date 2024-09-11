from time import sleep
from random import randint

def angryVova1(vovaRespectlocal):
    print("unplug Vova's screen from power? y/n")
    choice = input(">").lower()
    if choice == "n":
        print("you go away from the room")
    elif choice == "y":
        print("you unpluged Vova's screen with his Minecraft.")
        vovaRespectlocal -=100
        print("he is extremely mad now.")
        return vovaRespectlocal
    
def checkres(vovaRespect):
    if vovaRespect <= 0:
        print("game over, too low respect Vova doesnt want to talk to you anymore.")
        sleep(3)
        quit()


def gopnikFight():
    global vovaRespect
    def playerDeathCheck(playerHP):
        if playerHP < 1:
            print("The gopnik won the fight.")
            return True

    def gopnikDeathCheck(gopnikHP):
        if gopnikHP < 1:
            print("You've beated the gopnik. He yells at you and runs away.")
            return True

        

    playerHP = 30
    gopnikHP = 30
    hitChance = 60
    MinDMG = 10
    MaxDMG = 40

    print(f"So you have {playerHP}, and the gopnik has {gopnikHP}, you have entered a fight")


    while True:
        sleep(2)
        print("You try to hit gopnik...")
        if randint(0,100) <= hitChance:
            DMG = randint(MinDMG,MaxDMG)
            gopnikHP -= DMG
            print(f"You dealed {DMG} damage.")
        else:
            print("...and ****** up :(")
        if playerDeathCheck(playerHP) == True:
            playerWin = 1
            break
        if gopnikDeathCheck(gopnikHP) == True:
            playerWin = 0
            break
        sleep(1)
        print(f"The gopnik now has {gopnikHP}, while you health is {playerHP}")
        sleep(2)
        print("Gopnik also wants to hit you.")
        if randint(0,100) <= hitChance:
            DMG = randint(MinDMG,MaxDMG)
            playerHP -= DMG
            print(f"Gopnik has dealed {DMG} damage to you.")
        else:
            print("But he didn't manage to hit you.")
        sleep(1)
        print(f"The gopnik now has {gopnikHP}, while you health is {playerHP}")
        if playerDeathCheck(playerHP) == True:
            playerWin = 1
            break
        if gopnikDeathCheck(gopnikHP) == True:
            playerWin = 0
            break

    return playerWin

print("You see Vova playing Minecraft all pause.")
vovaRespect = 100
print("are you gonna disturb him, or keep looking?")
print("A = disturb")
print("B = keep loking")
choice = input(">").lower()
if choice == "a":
    vovaRespect -= 5
    print("you tried to get him of Minecraft, but he still sits")
    vovaRespect = angryVova1(vovaRespect)
elif choice == "b":
    print ("nothing happens")

print("few minutes later you see that 2 people try to grief Vova's base in Minecraft")
print("you wanna join and help him in defense? y/n")
choice = input(">").lower()
if choice == "y":
    print("Vova is thankful to you")
    vovaRespect += 40
elif choice == "n":
    print("Vova's rage can be heard in near classses. his emerald house got TNTed.")
    print("He looks towards you and you both realize that if you help him this would not have happened.")
    vovaRespect -=10

print(f"The day is over, your Vova respect value is {vovaRespect} for now...")
checkres(vovaRespect)
input("press any key to continue")

print("next day have been late to school but see Vova playing again at Lunch.")
print("he asks you calmly to look at visma and see when school ends today.")
print("A = do what he wants")
print("B = say him to leave Minecraft and watch by himself")
choice = input(">").lower()
if choice == "a":
    print("you help Vova with time and show him visma")
    vovaRespect += 10
elif choice == "b":
    print("Vova has to leave Minecraft for few seconds and gets blown up by a creeper.")
    print("he's angry npw and blames you, but you think it's unfair. You wanna take revenge")
    vovaRespect -=20
    angryVova1(vovaRespect)

print("you see Vova planning to grief back guys from yesterday.")
print("A = join him")
print("B = warn the dudes")
choice = input(">").lower()
if choice == "a":
    print("you joned him and you griefed base of almoust all your classmates at night, it would be hard without you.")
    vovaRespect += 70
elif choice == "b":
    print("You have warned your classmates about Vova's dirty plan and at night, when Vova came griefing all base members was waiting for him...")
    vovaRespect -= 60

print(f"The day is over, your Vova respect value is {vovaRespect} for now...")
checkres(vovaRespect)
input("press any key to continue")

print("you've got nice cheats to Minecraft such as spawning items or monsters. What about Vova?")
print("A = spawn diamonds and netherite and give Vova")
print("B = spawn 10 wither bosses in Vovas base")
choice = input(">").lower()
if choice == "a":
    print("you made Vova happy, because he doenst need to steal items from others anymore")
    print("the admin saw this and banned him from server.")
    vovaRespect -= 100
elif choice == "b":
    print("wither bossses destroyed Vova's base, he was so mad he ragequitet Minecraft.")
    print("but suddenly he saw a crypto site behind Minecraft and the exchange rate of his pepecoins were extremmely high")
    print("He selled it and earned 20$, he is really happy now")
    vovaRespect += 80

print(f"The day is over, your Vova respect value is {vovaRespect} for now...")
checkres(vovaRespect)
input("press any key to continue")

print("next day you see a gopnik try to take Vova's mobile phone.")
print("You wanna fight the gopnik? Y or N")
choice = input(">").lower()
if choice == "y":
    if gopnikFight() == 1:
        print("Vova is very glad he kept his phone for now")
        vovaRespect += 80
    elif gopnikFight() == 0:
        print("Gopnik beat the shit out of you both and took Vova's phone.")
        vovaRespect += 20
elif choice == "n":
    print("Gopnik beat the shit out of Vova and takes his phone. Vova is angry that you never came to help.")
    vovaRespect -= 40

print(f"The day is over, your Vova respect value is {vovaRespect} for now...")
checkres(vovaRespect)
input("press any key to continue")

print("next day ")


input("press any key to see your results")

print(f"you've completed the game. Final Vova respect value: {vovaRespect}")
if vovaRespect >= 100:
    print("good ending, you were a good friend to Vova")
elif vovaRespect < 100:
    print("bad ending, you were a bad friend to Vova, but there is still some respect between you")
elif vovaRespect < 0:
    print("very bad ending, you were an absolute coward to Vova. He doesnt want to talk to you anymore.")