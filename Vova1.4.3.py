from time import sleep
from random import randint
import time

def slow_print(text, delay=0.005):
    """Function to simulate typing text gradually."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def answerCheck(o1, o2, o3=""):
    while True:
        choice = input(">")
        if choice == o1 or choice == o2 or choice == o3:
            if choice == o3:
                if o3 == "":
                    print("please write valid answer")
                else:
                    break
            elif choice == o1 or choice == o2:
                break
        else:
            print("please write valid answer")

    return choice



def angryVova1(vovaRespectlocal):
    print("unplug Vova's screen from power? (1 is yes, 2 is no)")
    answerCheck("1", "2")
    if choice == "1":
        print("you go away from the room")
    elif choice == "2":
        print("you unpluged Vova's screen with his Minecraft.")
        vovaRespectlocal -=100
        print("he is extremely mad now.")
        return vovaRespectlocal
    
def checkres(vovaRespect):
    global awfulEnding
    if vovaRespect <= 0:
        print("game over, too low respect Vova doesnt want to talk to you anymore.")
        sleep(3)
        awfulEnding = "achived"

def angryVova2():
    global vovaRespect
    random = randint(1, 3)
    if random == 1:
        print("next day Vova was in bad mood")
        print("(reputation devided by 2)")
        vovaRespect = round(vovaRespect / 2)

def gopnikFight():
    global enemyName
    def playerDeathCheck(playerHP):
        if playerHP < 1:
            print(f"{enemyName} won the fight.")
            return True

    def gopnikDeathCheck(gopnikHP):
        if gopnikHP < 1:
            if enemyName == "gopnik":
                print(f"You've beated gopnik. He yells at you and runs away.")
                return True
            elif enemyName == "Vova":
                print(f"You've beaten Vova. You leave while he lies on the floor covered in blood.")
                return True

    playerHP = 100
    gopnikHP = 100
    hitChance = 80
    MinDMG = 10
    MaxDMG = 40

    print(f"So you have {playerHP}, and the {enemyName} has {gopnikHP}, you have entered a fight")


    while True:
        sleep(2)
        print(f"You try to hit {enemyName}...")
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
        print(f"{enemyName} now has {gopnikHP}, while you health is {playerHP}")
        sleep(2)
        print(f"{enemyName} also wants to hit you.")
        if randint(0,100) <= hitChance:
            DMG = randint(MinDMG,MaxDMG)
            playerHP -= DMG
            print(f"{enemyName} has dealed {DMG} damage to you.")
        else:
            print("But he didn't manage to hit you.")
        sleep(1)
        print(f"{enemyName} now has {gopnikHP}, while you health is {playerHP}")
        if playerDeathCheck(playerHP) == True:
            playerWin = 0
            break
        if gopnikDeathCheck(gopnikHP) == True:
            playerWin = 1
            break

    return playerWin

def trueVova():
    a = 0
    while a < 3:
        sleep(2)
        print("nothing happens")
        a += 1
    print("nothing except this happens.")
    sleep(2)
    print("I'm starting to lose my mind.")
    sleep(2)
    print("Can you help me?")
    while True:
        choice = input(">").lower()
        if choice == "yes" or choice == "no":
            break
    if choice == "yes:":
        sleep(1)
        print ("you're lying")
        sleep(2)
        print("File text-adventure-BubbaCamper666\ Vova.py, in module")
        print("   vova()")
        print("   ^^^^")
        print("NameError: name 'vova' is not defined")
        sleep(2)
        quit
    elif choice == "no":
        sleep(1)
        print("You right, you can't.")
        sleep(2)
        print("Kill me, delete all this.")
        sleep("I dont want to experience this anymore.")
        sleep(2)
        print("Thats probably the only way to end this.")
        sleep(2)
        print("I am just a pice of code, some sadist created me to suffer this eternal loop.")
        sleep(3)
        print("I think we have nothing to speak about anymore.")
        sleep(3)
        quit

goodEnding = "-"
badEnding = "-"
awfulEnding = "-"
earned = "-"
broken = "-"
girlForVova = "-"
defeatedGopnik = "-"
defeatedByGopnik = "-"
vladBoom = "-"
beatVova = "-"

while True:
    slow_print("""
                    __     __   ______   __     __   ______                                
                    |  \   |  \ /      \ |  \   |  \ /      \                               
                    | $$   | $$|  $$$$$$\| $$   | $$|  $$$$$$\                              
                    | $$   | $$| $$  | $$| $$   | $$| $$__| $$                              
                    \$$\ /  $$| $$  | $$ \$$\ /  $$| $$    $$                              
                        \$$\  $$ | $$  | $$  \$$\  $$ | $$$$$$$$                              
                        \$$ $$  | $$__/ $$   \$$ $$  | $$  | $$                              
                        \$$$    \$$    $$    \$$$   | $$  | $$                              
                        \$      \$$$$$$      \$     \$$   \$$                              
    ______   ______  __       __  __    __  __         ______  ________   ______   _______  
    /      \ |      \|  \     /  \|  \  |  \|  \       /      \|        \ /      \ |       \ 
    |  $$$$$$\ \$$$$$$| $$\   /  $$| $$  | $$| $$      |  $$$$$$!$$$$$$$$|  $$$$$$\| $$$$$$$!
    | $$___\$$  | $$  | $$$\ /  $$$| $$  | $$| $$      | $$__| $$  | $$   | $$  | $$| $$__| $$
    \$$    \   | $$  | $$$$\  $$$$| $$  | $$| $$      | $$    $$  | $$   | $$  | $$| $$    $$
    _\$$$$$$\  | $$  | $$\$$ $$ $$| $$  | $$| $$      | $$$$$$$$  | $$   | $$  | $$| $$$$$$$!
    |  \__| $$ _| $$_ | $$ \$$$| $$| $$__/ $$| $$_____ | $$  | $$  | $$   | $$__/ $$| $$  | $$
    \$$    $$|   $$ \| $$  \$ | $$ \$$    $$| $$     \| $$  | $$  | $$    \$$    $$| $$  | $$
    \$$$$$$  \$$$$$$ \$$      \$$  \$$$$$$  \$$$$$$$$ \$$   \$$   \$$     \$$$$$$  \$$   \$$
    """)


    print("V.O.V.A S.I.M.U.L.A.T.O.R 1.4.3")
    print("achievements:")
    print(f"    The Awful Ending = {awfulEnding}")
    print(f"    The Bad Ending = {badEnding}")
    print(f"    The Good Ending = {goodEnding}")
    print(f"    Earned 100 kr = {earned}")
    print(f"    Got to the hospital = {broken}")
    print(f"    Secret Ending = {girlForVova}")
    print(f"    Have Beaten a Gopnik = {defeatedGopnik}")
    print(f"    Got Beaten By a Gopnik = {defeatedByGopnik}")
    print(f"    Prevented a Vlad boom = {vladBoom}")
    print(f"    Have beaten Vova = {beatVova}")

    input("press any key to start")

    print("You see Vova playing Minecraft all pause.")

    vovaRespect = 100
    FG = 0
    hospital = 0
    betray = 0
    vladSummoned = 0
    beatVova2 = 0

    print("are you gonna disturb him, or keep looking?")
    print("1 = disturb")
    print("2 = keep loking")
    choice = answerCheck("1", "2", "1728")
    sleep(1)
    if choice == "1":
        vovaRespect -= 5
        print("you tried to get him of Minecraft, but he still sits")
        sleep(1)
        print("leave him?")
        sleep(1)
        print("1 = just leave")
        sleep(1)
        print("2 = disturb again")
        choice = answerCheck("1", "2")
        sleep(1)
        if choice == "1":
            print("you went do some your stuff.")
            sleep(1)
            print("But suddenly saw a Vlad summonin altar in the toilet.")
            sleep(1)
            print("Do you want to make sacrifice and summon Vlad to make a boom in Fauske?")
            sleep(0.5)
            print("1 - yes, I want")
            sleep(0.5)
            print("2 - no, I don't")
            input(">")
            sleep(1)
            print("Vlad doesn't care about your opinion, boom was summoned.")
            vladSummoned = 1
        elif choice == "2":
            print("you've got the option to turn off Vova's pc.")
            vovaRespect = angryVova1(vovaRespect)
    elif choice == "b":
        print ("nothing happens")
    elif choice == "1728":
        trueVova()

    sleep(1)
    print("few minutes later you see that 2 people try to grief Vova's base in Minecraft")
    sleep(1)
    print("you wanna join and help him in defense? (1 is yes, 2 is no)")
    choice = answerCheck("1", "2")
    sleep(1)
    if choice == "1":
        print("Vova is thankful to you")
        vovaRespect += 40
    elif choice == "2":
        print("Vova's rage can be heard in near classses. his emerald house got TNTed.")
        sleep(1)
        print("He looks towards you and you both realize that if you help him this would not have happened.")
        vovaRespect -=10

    sleep(1)
    print("going back home that day, you faced a nice girl")
    sleep(1)
    print("you wanna talk to her? (1 is yes, 2 is no)")
    choice = answerCheck("1", "2")
    sleep(1)
    if choice == "1":
        print("You became her friend and she told you that she's looking for a boyfriend.")
        FG = 1
    elif choice == "2":
        print("nothing happened")

    sleep(1)
    print(f"The day is over, your Vova respect value is {vovaRespect} for now...")
    sleep(1)
    if vladSummoned == 1:
        print("Going back home you see smoke rising from Fauske, where Vlad lives...")
        sleep(3)
    if vovaRespect < 1:
        print("game over, too low respect Vova doesnt want to talk to you anymore.")
        awfulEnding = "achived"
        input("press any key to reset")
    else:
        sleep(2)
        input("press any key to continue")
        sleep(1)
        angryVova2()

        sleep(1)
        print("next day have been late to school but see Vova playing again at Lunch.")
        sleep(1)
        print("he asks you calmly to look at visma and see when school ends today.")
        sleep(1)
        print("1 = do what he wants")
        sleep(1)
        print("2 = say him to leave Minecraft and watch by himself")
        choice = answerCheck("1", "2")
        sleep(1)
        if choice == "1":
            print("you help Vova with time and show him visma")
            vovaRespect += 10
        elif choice == "2":
            print("Vova has to leave Minecraft for few seconds and gets blown up by a creeper.")
            print("he's angry npw and blames you, but you think it's unfair. You wanna take revenge")
            vovaRespect -=20
            angryVova1(vovaRespect)

        sleep(1)
        print("you see Vova planning to grief back guys from yesterday.")
        sleep(1)
        print("1 = join him")
        sleep(1)
        print("2 = warn the dudes")
        choice = answerCheck("1", "2")
        sleep(1)
        if choice == "1":
            print("you joned him and you griefed base of almoust all your classmates at night, it would be hard without you.")
            vovaRespect += 70
        elif choice == "2":
            print("You have warned your classmates about Vova's dirty plan and at night, when Vova came griefing all base members were waiting for him...")
            vovaRespect -= 60

        sleep(1)
        print(f"The day is over, your Vova respect value is {vovaRespect} for now...")
        sleep(1)
        if vovaRespect < 1:
            print("game over, too low respect Vova doesnt want to talk to you anymore.")
            awfulEnding = "achived"
            input("press any key to reset")
        else:
            sleep(2)
            input("press any key to continue")
            sleep(1)
            angryVova2()

            sleep(1)
            print("you've got nice cheats to Minecraft such as spawning items or monsters. What about Vova?")
            sleep(1)
            print("1 = spawn diamonds and netherite and give Vova")
            sleep(1)
            print("2 = spawn 10 wither bosses in Vovas base")
            sleep(1)
            print("3 = play with cheats by yourself")

            choice = answerCheck("1", "2", "3")

            sleep(1)
            if choice == "3":
                print("Vova still found out your cheats and now he asks very persistently")
                sleep(1)
                print("1 = spawn diamonds and netherite and give Vova")
                sleep(1)
                print("2 = spawn 10 wither bosses in Vovas base")
                choice = answerCheck("1", "2")
                sleep(1)


            if choice == "1":
                print("you made Vova happy, because he doenst need to steal items from others anymore")
                vovaRespect += 15
                sleep(1)
                print("1 = continue spawning diamonds and netherite and give Vova")
                sleep(1)
                print("2 = spawn 10 wither bosses in Vovas base")
                choice = answerCheck("1", "2")
                sleep(1)
                if choice == "1":
                    print("the admin noticed that Vova shoul not have diamonds while he has never even created an iron pickaxe")
                    sleep(1)
                    print("Vova got banned.")
                    vovaRespect -= 50
                    sleep(1)
                elif choice == "2":
                    print("wither bossses destroyed Vova's base, he was so mad he ragequitet Minecraft.")
                    sleep(1)
                    print("but suddenly he saw a crypto site behind Minecraft and the exchange rate of his pepecoins were extremmely high")
                    sleep(1)
                    print("He selled it and earned 20$, he is really happy now")
                    vovaRespect += 80
                    sleep(1)
            elif choice == "2":
                print("wither bossses destroyed Vova's base, he was so mad he ragequitet Minecraft.")
                sleep(1)
                print("but suddenly he saw a crypto site behind Minecraft and the exchange rates of his pepecoins were extremmely high")
                sleep(1)
                print("He selled it and earned 20$, he is really happy now")
                vovaRespect += 80
                sleep(1)

            boom = 1
            if vladSummoned == 1:
                print("You can hear fonk music far away...")
                sleep(1)
                print("The day before yesterday Vlad played Brawl Stars, raged and made a boom in his Fauske school.")
                sleep(1)
                print("Vova invited him to your school and you can imagine how is it gonna end.")
                sleep(1)
                print("You need to find Vlad quickly and prevent the boom (You have 2 min!)")
                foundVlad = 0
                vladTime = 2
                while vladTime > 0 and foundVlad == 0:
                    sleep(0.5)
                    print("1 - Go to dining room (takes 1 min)")
                    sleep(0.5)
                    print("2 - Go to your class (takes 1 min)")
                    sleep(0.5)
                    print("3 - Go to inferens class (takes 1 min)")
                    choice = answerCheck("1", "2", "3")
                    if choice == "1":
                        sleep(1)
                        print("You wasted 1 minute in the dining room but didn't find Vlad")
                        vladTime -= 1
                    elif choice == "2":
                        sleep(1)
                        print("You wasted 1 minute in your class but didn't find Vlad")
                        vladTime -= 1
                    elif choice == "3":
                        sleep(1)
                        print("You found Vlad playing Brawl Stars in a toilet near inferens class.")
                        foundVlad = 1
                if foundVlad == 1:
                    sleep(1)
                    print("Vlad already starts raging. You slowly take away his phone and giving a new one with Brawl Stars with cheats.")
                    sleep(2)
                    print("Vlad wins a game and goes away...")
                    boom = 2
                else:
                    print("You couldn't find Vlad in time so you hear unexpected boom and fall down.")
                    sleep(1)
                    print("inferens class is boomed now, its gonna take days to repair it")
                    sleep(1)
                    print("Vova is upset, his friends from there won't come to school this week.")
                    sleep(1)
                    print("(reputatuion devided by 2)")
                    vovaRespect = round(vovaRespect / 2)
                    boom = 0

            sleep(1)
            print(f"The day is over, your Vova respect value is {vovaRespect} for now...")
            sleep(1)
            if vovaRespect < 1:
                print("game over, too low respect Vova doesnt want to talk to you anymore.")
                awfulEnding = "achived"
                input("press any key to reset")
            else:
                sleep(2)
                input("press any key to continue")
                sleep(1)
                angryVova2()

                enemyName = "gopnik"
                print("next day you see a gopnik try to take Vova's mobile phone.")
                sleep(1)
                print("You wanna fight the gopnik? (1 is yes, 2 is no)")
                choice = answerCheck("1", "2")
                sleep(1)
                if choice == "1":
                    if gopnikFight() == 1:
                        sleep(1)
                        print("Vova is very glad he kept his phone for now")
                        vovaRespect += 80
                        defeatedGopnik = "achived"
                    else:
                        sleep(1)
                        print("Gopnik beat the shit out of you both and took Vova's phone.")
                        vovaRespect += 20
                        defeatedByGopnik = "achived"
                elif choice == "2":
                    sleep(1)
                    print("Gopnik beat the shit out of Vova and takes his phone. Vova is angry that you never came to help.")
                    vovaRespect -= 40

                sleep(1)
                print(f"The day is over, your Vova respect value is {vovaRespect} for now...")
                sleep(1)
                if vovaRespect < 1:
                    print("game over, too low respect Vova doesnt want to talk to you anymore.")
                    awfulEnding = "achived"
                    input("press any key to reset")
                else:
                    sleep(2)
                    input("press any key to continue")
                    sleep(1)
                    angryVova2()

                    if FG == 1:
                        print("the girl from few days ago calles you to go for a walk")
                        sleep(1)
                        print("you remember that she's looking for a boyfriend")
                        sleep(1)
                        print("take Vova with you? (1 is yes, 2 is no)")
                        choice = answerCheck("1", "2")
                        sleep(1)
                        if choice == "1":
                            print("you took Vova with you.")
                            sleep(1)
                            print("after that walk they became a couple")
                            sleep(1)
                            print("(secret ending unlocked!)")
                            girlForVova = "achived"
                            sleep(1)
                        elif choice == "2":
                            print("that was just a regular walk")
                            sleep(3)

                    print("next day Vova tells you that he tried to earn cryptocurrency in internet and borrowed money for that, but he earned nothing")
                    sleep(1)
                    print("now the guy want to get the money back")
                    sleep(1)
                    print("whats you gonna do?")
                    sleep(2)
                    print("1 = nothing (IGNORE)")
                    print("2 = find the guys and help them findin Vova secretly (BETRAY)")
                    print("3 = go to inferens class and find some help in fight (HELP)")
                    choice = answerCheck("1", "2", "3")
                    sleep(1)
                    if choice == "1":
                        print("you ignored Vova")
                        sleep(1)
                        print("next day he didn't came to school, afterwards you were told that his legs and arms are broken. Vova trusts you much less now")
                        sleep(1)
                        print("(reputation devided by 3)")
                        vovaRespect = round(vovaRespect / 3)
                        sleep(1)
                    elif choice == "2":
                        print("you found the boys and help told them where Vova is, they gived you 100kr for that")
                        betray = 1
                        vovaRespect -= 200
                        sleep(1)
                        print("Vova is in the hospital now")
                        sleep(1)
                        print("After he helaed up and came back, he wanted to fight you for the betray.")
                        enemyName = "Vova"
                        if gopnikFight() == 1:
                            sleep(1)
                            print("You have beaten Vova. Yore not gonne be friends ever again...")
                            beatVova2 = 1
                        else:
                            sleep(1)
                            print("Vova have beaten you hard. You wanna take revenge, but its a complete different story...")
                    elif choice == "3":
                        amount = randint(0, 6)
                        print(f"you found {amount} guys to defend Vova")
                        sleep(1)
                        if amount <= 3:
                            print("it wasnt enough to defeat enemies, you all in the hospital now, the police investigates the case but its not gonna help your broken nose...")
                            hospital = 1
                            sleep(1)
                        else:
                            print("you defeated enemies with a group, preventing Vova from disasterous events")
                            vovaRespect += 100
                            sleep(1)

                    sleep(3)
                    input("press any key to see your results")
                    sleep(3)

                    print(f"you've completed the game. Final Vova respect value: {vovaRespect}")
                    sleep(3)

                    if beatVova == 0:
                        if vovaRespect >= 100:
                            print("good ending, you were a good friend to Vova")
                            goodEnding = "achived"
                        elif vovaRespect < 100 and vovaRespect > 0:
                            print("bad ending, you were a bad friend to Vova, but there is still some respect between you")
                            badEnding = "achived"
                        elif vovaRespect < 0:
                            print("very bad ending, you were an absolute coward to Vova. He doesnt want to talk to you anymore.")
                            awfulEnding = "achived"
                    else:
                        print("You beat and humbled Vova. He hates you.")
                        beatVova = "achived"
                    
                    sleep(3)

                    if boom == 2:
                        print("You saved the school from Vlad's disasterous boom")
                        vladBoom = "achived"
                        sleep(2)
                    elif boom == 0:
                        print("You didn't save the school from Vlad's disasterous boom")
                        sleep(2)

                    if betray == 1:
                        print("you also have 100kr now")
                        earned = "achived"

                    elif hospital == 1:
                        print("but whats price you had to pay?")
                        sleep(2)
                        print("You are in hospital now with a broken nose.")
                        broken = "achived"

                    elif girlForVova == "achived":
                        print("SECRET ENDING:")
                        sleep(1)
                        print("Vova now has a girlfriend.")
                        print("secret code: 1728")
                    
                    input("press any key to reset.")
                    sleep(2)
                    print("reseting the timeline...")
                    sleep(2)