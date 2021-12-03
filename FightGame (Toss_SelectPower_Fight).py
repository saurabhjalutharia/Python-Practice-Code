import random
import os
os.system("cls")

#----------------------------------------------DEFAULT VALUES-----------------------------------------------------------
Player1win=False
Player2win=False
power1=power2=100               #DEFAULT POWER OF BOTH THE PLAYERS
pp1list=[]
pp2list=[]
powerchoice = []                #POWER LIST CHOOSE BY THE PLAYER WHO WON THE TOSS
powerlist=["Fly","Invisible","Laser","Speed","Healing","Power Punch","ThunderBolt","Fire","Magnatic","Fire Claws"]
powerlistdict={"Fly":10,"Invisible":8,"Laser":12,"Speed":4,"Healing":13,"Power Punch":18,"ThunderBolt":19,"Fire":23,"Magnatic":5,"Fire Claws":19}
                        # POWER DICTIONARY ASSOCIATED WITH THEIR DEFAULT POWER

#--------------------------------------------------- GAME CODE START --------------------------------------------------------
print("   LETs START THE GAME  ".center(100,"-"))
print("")
player1=input("Enter 1st Player Name:\t")           #USER ENTER NAME
player2=input("Enter 2nd Player Name:\t")           #USER ENTER NAME

#--------------------------------------------- TOSS CODE -----------------------------------------------------------------
toss=random.choice(["h","t"])
answer=input(f"\nPlayer {player1} Choose Either Head(H) or Tail(T)\t").lower()
while(answer not in ["h","t"]):                     #USER VALID INPUT CHECK
    print(" Enter Either H or T ".center(40,"-"))
    print("")
    answer=input(f" Player {player1} Choose Either Head(H) or Tail(T)\t").lower()
if(answer==toss):
    print("")
    print("     {} You Win Toss. Choose Your Power First.   ".format(player1).center(50,"-"))
    Player1win=True                                 #PLAYER 1 WON THE TOSS
else:
    print("")
    print("     {} Win Toss. Choose Your Power First.   ".format(player2).center(50,"-"))
    Player2win=True                                 #PLAYER 2 WON THE TOSS

#------------------------------------------- PLAYER CHOOSE POWER ---------------------------------------------------------
print("   Choose Any 5 Power   ".center(50,"-"))
print("\t\t1. Fly\n\t\t2. Invisible\n\t\t3. Laser\n\t\t4. Speed\n\t\t5. Healing\n\t\t6. Power Punch\n\t\t7. ThunderBolt\n\t\t8. Fire\n\t\t9. Magnatic\n\t\t10. Fire Claws\n")
print("Enter Number in the Range 1-10 Only.")
for i in range(1,6):   
    num = input(f"Enter Your {i} Power:  ")
    while((num.isalpha()==True) or (int(num) not in range(1,11))):      #USER VALID INPUT CHECK
        print("Please Enter Numbers in the Range 1-10 Only.\n")
        num = input(f"Enter Your {i} Power:  ")
    numb = int(num)
    powerchoice.append(numb-1)                                          #PLAYER POWER NUMBER ADD IN THE POWERCHOICE LIST

#--------------------------- ASSIGN POWERS TO THEIR RESPECTED PLAYERS --------------------------------------------------
if(Player1win):
    for i in range(len(powerchoice)):
        pp1list.append(powerlist[powerchoice[i]])       #ADD WINNER PLAYER POWER IN THE PP1LIST IN LANGUAGE FORM
    for i in range(len(pp1list)):
        powerlist.remove(pp1list[i])                    #REMOVE POWER(s) THAT HAS BEEN SELECTED BY THE TOSS WINNER PLAYER
    pp2list=powerlist                                   #ASSIGN REMAINING POWER TO THE OTHER PLAYER
else:
    for i in range(len(powerchoice)):                   
        pp2list.append(powerlist[powerchoice[i]])       #SAME FROM ABOVE COMMENT
    for i in range(len(pp2list)):
        powerlist.remove(pp2list[i])                    #SAME FROM ABOVE COMMENT
    pp1list=powerlist                                   #SAME FROM ABOVE COMMENT
    
#-------------------------------- DISPLAY THE ASSIGN POWER And START THE GAME -------------------------------------------
print("")
print("{} Powers are: \t".format(player1), pp1list)
print("{} Powers are: \t".format(player2), pp2list)
print("")
print("   GAME BEGINS   ".center(100,"*"))
print("")

#---------------------------- PLAYER 1 AND PLAYER 2 FIGHTING And ANNOUNCING THE WINNER OF THE GAME ------------------------
while(power1>0 or power2>0):
    rand = random.randint(1,51)                     #FOR EITHER PLAYER START THE GAME
    randtime=random.randint(1,3)                    #FOR HOW MANY TIMES (CONSECUTIVELY) A PLAYER ATTACK OTHER ONE IN ONE GO 
    if((rand%2)==0):                                #PLAYER 1 START FIGHTING
        for i in range(randtime):                   #NUMBER OF TIMES PLAYER 1 ATTACK CONTINEOUSLY
            randppower=random.randint(0,4)          #PLAYER 1 CAN CHOOSE ANY POWER FROM HIS/HER POWER LIST
            p1=powerlistdict[pp1list[randppower]]   #PLAYER 1 POWER STRENGTH ALLOTED
            print("\n{} choose Power {} of strength ({}) and attack on {}.".format(player1,pp1list[randppower],p1,player2))

            power2 -= p1                             #PLAYER 2 POWER DECREASE BY NUMBER OF PLAYER 1 POWER STRENGTH
            if(power2<0):                            #TO CHECK WHEATHER PLAYER 2 LOSE OR NOT
                print("{} Energy left: {} And {}: 0.".format(player1,power1,player2))   
                print("")
                print("     {} WIN     ".center(50,"*").format(player1.upper()))                       #ANNOUNCE PLAYER 1 WIN
                print("")
                exit()
            else:
                print("{} Energy left: {} And {} Energy: {}.".format(player1,power1,player2,power2))   #DISPLAY RESPECTED REMAINING STRENGTH

    else:                                               #PLAYER 2 START FIGHTING
        for i in range(randtime):                       #SAME AS ABOVE COMMENT BUT IN CONTEXT TO PLAYER 2
            randppower=random.randint(0,4)              #SAME AS ABOVE COMMENT BUT IN CONTEXT TO PLAYER 2
            p2=powerlistdict[pp2list[randppower]]       #SAME AS ABOVE COMMENT BUT IN CONTEXT TO PLAYER 2
            print("\n{} choose Power {} of strength ({}) and attack on {}.".format(player2,pp2list[randppower],p2,player1))
            power1 -= p2
            if(power1<0):
                print("{} Energy left: {} And {}: 0.".format(player2,power2,player1))
                print("")
                print("     {} WIN     ".center(50,"*").format(player2.upper()))                       #SAME AS ABOVE COMMENT BUT IN CONTEXT OF PLAYER 2
                print("")
                exit()
            else:
                print("{} Energy left: {} And {} Energy: {}.".format(player1,power1,player2,power2))   #SAME AS ABOVE COMMENT BUT IN CONTEXT OF PLAYER 2

#---------------------------------------------- PROGRAM CODE END ---------------------------------------------------------------------