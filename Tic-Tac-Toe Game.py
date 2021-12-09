from itertools import permutations
import random, os
os.system("cls")

winList = []
winList1 = []
xList = []
extra = []
outermatrix=[]
userWin = False
compWin = False
row = 3
column = 3
totaluserchance=5
totalcompchance=4
totallist = [1,2,3,4,5,6,7,8,9]     # TOTAL BOARD NUMBER
userlist=[]
complist=[]
positionfill = []
symbollist = []
positiondict={}                     #DICTIONARY FOR SYMBOL
symlist = ["x","o"]

#-------USER AND COMPUTER CHOOSE THEIR RESPECTED SYMBOL And SETING MAX. CHANCE FOR USER----------
print("     Lets Play Tic-Tac-Toe  ".center(50,"*"))
print("     Choose Your Symbol 'X' or 'O'.   ".center(50,"*"))
usersymbol = input("").lower()
while(usersymbol[0] not in symlist):
    print(" Choose Either Symbol 'X' or 'O'. ".center(50,"-"))
    usersymbol = input("").lower()
if(usersymbol == "x"):
    compsymbol="o"
else:
    compsymbol = "x"
print("\nYour Symbol is ({}) and Computer Symbol is ({}).\n".format(usersymbol,compsymbol))
if(totaluserchance<totalcompchance):
    k=chance=totaluserchance
else:
    chance=k=totalcompchance
#-------ENTERING VALUEs BY USER AND COMPUTER And CHECKING IF POSITION IS ALREADY OCCUPIED OR NOT-----------
while(chance):
    for i in range(1):
        j=1
        while(j):
            a = int(input("Choose Your Position:\t"))
            if(a in positionfill):
                print("Position already Occupied. Try Again\n")
            else:
                if(a<1 or a>9):
                    print("Enter in the Range (1-9) Only.")
                else:
                    userlist.append(a)      #ADDING USER CHOSEN POSITION IN THE USER LIST
                    positionfill.append(a)  #TOTAL POSITION FILL OUT OF 9
                    totallist.remove(a)     #REMOVING ELEMENT THAT HAS BEEN CHOSSEN BY USER
                    j -= 1

#-------COMPUTER CHOOSE ITS SYMBOL POSITION RANDOMLY FROM THE REMAINING POSITION-------------------- 
    num=random.choice(totallist)
    while(num in positionfill):
        num=random.randint(1,9)
    print("Computer Choose Position: {}".format(num))
    complist.append(num)        #ADDING COMPUTER CHOSEN POSITION IN THE COMPUTER LIST
    positionfill.append(num)    #POSITION FILL BY COMPUTER
    totallist.remove(num)       #REMOVING ELEMENT THAT HAS BEEN CHOSSEN BY COMPUTER

#----------LISTING FINAL POSITION BY USER AND COMPUTER IN THROUGHOUT THE GAME-------------------------
    if(len(totallist)==1):
        a = totallist.pop()             #(a) CONTAIN THE LAST ELEMENT POSITION THATS NOT CHOSSEN BY EITHER
        if(k==totaluserchance):
            userlist.append(a)          #ADDING LAST ELEMENT POSITION IN THE USER LIST
            positionfill.append(a)      #ALL POSITION COMPLETELY FILL
        else:
            complist.append(a)          #ADDING LAST ELEMENT POSITION IN THE COMPUTER LIST
            positionfill.append(a)      #ALL POSITION COMPLETELY FILL
    else:
        print("\nRemaning Position are: ",totallist)    #DISPLAYING REMANING POSITION
    print("")
#----------SET SYMBOL IN THE DICTIONARY WITH KEY ACC. TO WHAT POSITION ARE FILL BY WHO-----------
    for i in range(len(positionfill)):
        if(positionfill[i] in userlist):
            positiondict[positionfill[i]]=usersymbol
        else:
            positiondict[positionfill[i]]=compsymbol
    print("")

#--------------------------------FOR DISPLAY RESPECTED SYMBOLS ON THE SCREEN---------------------------
    for i in range(row):
        print("\t\t\t", end="")
        for j in range(column):
            if(i==0):
                a = (2**i)+j          #FOR 1, 2, 3 POSITION ON THE BOARD
                if(a in positionfill):
                    if(j==(column-1)):
                        print(" {} ".format(positiondict[a]), end=" ")
                    else:
                        print(" {} |".format(positiondict[a]), end=" ")
                else:
                    if(j==(column-1)):
                        print(" {} ".format(" "), end=" ")
                    else:
                        print(" {} |".format(" "), end=" ")
                
            elif(i==1):
                b = (2**i)+(j+2)       #FOR 4, 5, 6 POSITION ON THE BOARD
                if(b in positionfill):
                    if(j==(column-1)):
                        print(" {} ".format(positiondict[b]), end=" ")
                    else:
                        print(" {} |".format(positiondict[b]), end=" ")
                else:
                    if(j==(column-1)):
                        print(" {} ".format(" "), end=" ")
                    else:
                        print(" {} |".format(" "), end=" ")
            
            else:
                c = (2**i)+(j+3)       #FOR 7, 8, 9 POSITION ON THE BOARD
                if(c in positionfill):
                    if(j==(column-1)):
                        print(" {} ".format(positiondict[c]), end=" ")
                    else:
                        print(" {} |".format(positiondict[c]), end=" ")
                else:
                    if(j==(column-1)):
                        print(" {} ".format(" "), end=" ")
                    else:
                        print(" {} |".format(" "), end=" ")
        print("")
    print("")
    chance -= 1     #FOR WHILE LOOP

#---------------------------------TO ANNOUNCE WINNER OF THE GAME------------------------------------

winList = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
for i in range(len(winList)):
    winList1.append(list(permutations(winList[i])))     #ALL POSSIBLE WINNING OUTCOME LIST OF LIST OF TUPLE[[()]]
for k in range(len(userlist)):
    x = userlist.pop(k)      #POP EACH ELEMENT FROM USER ONE BY ONE AND COMPARE THE REMANING LIST WITH THE WINNING POSSIBILITY
    for i in list(winList1):
        for j in i:
            a = list(j)
            extra.append(a)  #CONTAIN THE LIST OF ALL POSSIBLE WINNING OUTCOME
    if userlist in extra:    #COMPARE USER INPUT ELEMENT WITH THE WINNING OUTCOMES
        userWin=True
        userlist.insert(k, x)
        break
    else:
        None
    userlist.insert(k, x)
if(userWin):
    print("")
    print("     CONGRATULATION On Your Big Win     ".center(70,"*"))
    print("")
else:
    print("")
    print("     Computer Win. Try Again Looser.     ".center(70,"*"))
    print("")

# TIE CASE IS NOT HERE. I KNOW.
#--------------------------------------------------END----------------------------------------------------------------------------#