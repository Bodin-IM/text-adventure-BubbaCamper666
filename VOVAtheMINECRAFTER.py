from time import sleep
from random import randint
def angryVova1(vovaRespectlocal):
    print("unplug Vova's screen from power? y/n")
    while True:
        choice = input(">").lower()
        if choice == "y" or choice == "n":
            break
        else:
            print("please write valid answer")
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

def angryVova2():
    global vovaRespect
    random = randint(1, 2)
    if random == 1:
        print("next day Vova was in bad mood")
        print("(reputation devided by 2)")
        vovaRespect = vovaRespect / 2

def gopnikFight():
    def playerDeathCheck(playerHP):
        if playerHP < 1:
            print("The gopnik won the fight.")
            return True

    def gopnikDeathCheck(gopnikHP):
        if gopnikHP < 1:
            print("You've beated the gopnik. He yells at you and runs away.")
            return True



    playerHP = 100
    gopnikHP = 100
    hitChance = 80
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
            playerWin = 0
            break
        if gopnikDeathCheck(gopnikHP) == True:
            playerWin = 1
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
            playerWin = 0
            break
        if gopnikDeathCheck(gopnikHP) == True:
            playerWin = 1
            break

    return playerWin

print("You see Vova playing Minecraft all pause.")
vovaRespect = 100
earned = 0
broken = 0
girlForVova = 0
print("are you gonna disturb him, or keep looking?")
print("A = disturb")
print("B = keep loking")
while True:
    choice = input(">").lower()
    if choice == "a" or choice == "b":
        break
    else:
        print("please write valid answer")
if choice == "a":
    vovaRespect -= 5
    print("you tried to get him of Minecraft, but he still sits")
    print("leave him?")
    print("A = just leave")
    print("B = disturb again")
    while True:
        choice = input(">").lower()
        if choice == "a" or choice == "b":
            break
        else:
            print("please write valid answer")        
    if choice == "a":
        print("you went do some your stuff.")
    elif choice == "b":
        print("you've got the option to turn off Vova's pc.")
        vovaRespect = angryVova1(vovaRespect)
elif choice == "b":
    print ("nothing happens")

print("few minutes later you see that 2 people try to grief Vova's base in Minecraft")
print("you wanna join and help him in defense? y/n")
while True:
    choice = input(">").lower()
    if choice == "y" or choice == "n":
        break
    else:
        print("please write valid answer")
if choice == "y":
    print("Vova is thankful to you")
    vovaRespect += 40
elif choice == "n":
    print("Vova's rage can be heard in near classses. his emerald house got TNTed.")
    print("He looks towards you and you both realize that if you help him this would not have happened.")
    vovaRespect -=10

print("going back home that day, you faced a nice girl")
print("you wanna talk to her? y/n")
while True:
    choice = input(">").lower()
    if choice == "y" or choice == "n":
        break
    else:
        print("please write valid answer")
if choice == "y":
    print("You became her friend and she told you that she's looking for a boyfriend.")
    girlForVova = 1
elif choice == "n":
    print("nothing happened")

print(f"The day is over, your Vova respect value is {vovaRespect} for now...")
checkres(vovaRespect)
input("press any key to continue")
angryVova2()

print("next day have been late to school but see Vova playing again at Lunch.")
print("he asks you calmly to look at visma and see when school ends today.")
print("A = do what he wants")
print("B = say him to leave Minecraft and watch by himself")
while True:
    choice = input(">").lower()
    if choice == "a" or choice == "b":
        break
    else:
        print("please write valid answer")
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
while True:
    choice = input(">").lower()
    if choice == "a" or choice == "b":
        break
    else:
        print("please write valid answer")
if choice == "a":
    print("you joned him and you griefed base of almoust all your classmates at night, it would be hard without you.")
    vovaRespect += 70
elif choice == "b":
    print("You have warned your classmates about Vova's dirty plan and at night, when Vova came griefing all base members was waiting for him...")
    vovaRespect -= 60

print(f"The day is over, your Vova respect value is {vovaRespect} for now...")
checkres(vovaRespect)
input("press any key to continue")
angryVova2()

print("you've got nice cheats to Minecraft such as spawning items or monsters. What about Vova?")
print("A = spawn diamonds and netherite and give Vova")
print("B = spawn 10 wither bosses in Vovas base")
print("C = play with cheats by yourself")
while True:
    choice = input(">").lower()
    if choice == "a" or choice == "b" or choice == "c":
        if choice == "c":
            print("Vova still found out your cheats and now he asks very persistently")
            print("A = spawn diamonds and netherite and give Vova")
            print("B = spawn 10 wither bosses in Vovas base")
        elif choice == "a":
            break
        elif choice == "b":
            break
    else:
        print("please write valid answer")
if choice == "a":
    print("you made Vova happy, because he doenst need to steal items from others anymore")
    vovaRespect += 15
    print("A = continue spawning diamonds and netherite and give Vova")
    print("B = spawn 10 wither bosses in Vovas base")
    while True:
        choice = input(">").lower()
        if choice == "a" or choice == "b":
            break
        else:
            print("please write valid answer")
    if choice == "a":
        print("the admin noticed that Vova shoul not have diamonds while he never even created an iron pickaxe")
        print("Vova got banned.")
        vovaRespect -= 50
    elif choice == "b":
        print("wither bossses destroyed Vova's base, he was so mad he ragequitet Minecraft.")
        print("but suddenly he saw a crypto site behind Minecraft and the exchange rate of his pepecoins were extremmely high")
        print("He selled it and earned 20$, he is really happy now")
        vovaRespect += 80
elif choice == "b":
    print("wither bossses destroyed Vova's base, he was so mad he ragequitet Minecraft.")
    print("but suddenly he saw a crypto site behind Minecraft and the exchange rate of his pepecoins were extremmely high")
    print("He selled it and earned 20$, he is really happy now")
    vovaRespect += 80

print(f"The day is over, your Vova respect value is {vovaRespect} for now...")
checkres(vovaRespect)
input("press any key to continue")
angryVova2()

print("next day you see a gopnik try to take Vova's mobile phone.")
print("You wanna fight the gopnik? Y or N")
while True:
    choice = input(">").lower()
    if choice == "y" or choice == "n":
        break
    else:
        print("please write valid answer")
if choice == "y":
    if gopnikFight() == 1:
        print("Vova is very glad he kept his phone for now")
        vovaRespect += 80
    else:
        print("Gopnik beat the shit out of you both and took Vova's phone.")
        vovaRespect += 20
elif choice == "n":
    print("Gopnik beat the shit out of Vova and takes his phone. Vova is angry that you never came to help.")
    vovaRespect -= 40

print(f"The day is over, your Vova respect value is {vovaRespect} for now...")
checkres(vovaRespect)
input("press any key to continue")
angryVova2()

if girlForVova == 1:
    print("the girl from few days ago calles you to go for a walk")
    print("you remember that she's looking for a boyfriend")
    print("take Vova with you? y/n?")
    while True:
        choice = input(">").lower()
        if choice == "y" or choice == "n":
            break
        else:
            print("please write valid answer")
    if choice == "y":
        print("you took Vova with you.")
        print("after that walk they became a couple")
        print("secret ending unlocked!")
        girlForVova = 2
    elif choice == "n":
        print("that was just a regular walk")

print("next day Vova tells you that he tried to earn cryptocurrency in internet and borrowed money for that, but he earned nothing")
print("now the guy want to get the money back")
print("whats you gonna do?")
print("A = nothing (IGNORE)")
print("B = find the guys and help them findin Vova secretly (BETRAY)")
print("C = go to inferens class and find some help in fight (HELP)")
while True:
    choice = input(">").lower()
    if choice == "a" or choice == "b" or choice == "c":
        choice == "a", "b", "c"
        break
    else:
        print("please write valid answer")
if choice == "a":
    print("you ignored Vova")
    print("next day he didn't came to school, afterward you were told that hes legs and arms are broken. Vova trusts you much less now")
    print("(reputation devided by 3)")
    vovaRespect = round(vovaRespect / 3)
elif choice == "b":
    print("you found the boys and help told them where Vova is, they gived you 100kr for that")
    earned = 1
    vovaRespect -= 200
    print("Vova is in the hospital now")
elif choice == "c":
    amount = randint(0, 6)
    print(f"you found {amount} guys to defend Vova")
    if amount <= 3:
        print("it wasnt enough to defeat enemies, you all in the hospital now, the police investigates the case but its not gonna help your broken nose...")
        broken = 1
    else:
        print("you defeated enemies with a group, preventing Vova from disasterous events")
        vovaRespect += 100

input("press any key to see your results")

print(f"you've completed the game. Final Vova respect value: {vovaRespect}")

if vovaRespect >= 100:
    print("good ending, you were a good friend to Vova")
    quit
elif vovaRespect < 100:
    print("bad ending, you were a bad friend to Vova, but there is still some respect between you")
    quit
elif vovaRespect < 0:
    print("very bad ending, you were an absolute coward to Vova. He doesnt want to talk to you anymore.")
    quit

if earned == 1:
    print("you also have 100kr now")
    quit

if broken == 1:
    print("but whats price you had to pay?")
    print("You are in hospital now with a broken nose.")
    quit

if girlForVova == 2:
    print("SECRET ENDING:")
    print("Vova now has a girlfriend.")