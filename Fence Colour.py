import random, os
os.system("cls")

print("     FENCE  COLOUR PROBLEM    ".center(70,"-"))
print("   (No Two Consecutive Fence will have Same Colour )   ".center(70,"-"))
fencenum = int(input("\nEnter Number of Fences:\t\t\t"))
colnum = int(input("Enter Max. No. of Colour(s) to use:\t"))
print("")

while(colnum>fencenum):
    print("Colur No. Cannot be More than Fence No.".center(70,"-"))
    colnum = int(input("Enter Colour No. Less than Fence Number:\t"))
while(colnum<2):
    print("Choose Atleat 2 Color(s).".center(70,"-"))
    colnum = int(input("Enter Colour No. More than 2:\t"))
if(colnum>4):
    while(colnum>4):
        print("Maximum 4 Colours can be Use.")
        colnum = int(input("Enter Upto 4 Number of Colour(s) to use:\t"))
else:
    color = colnum

color = colnum
fencecolorlist = []
colorlist = [None]*color
clist=[]
remlist = []
precolor = {"r":"Red","b":"Blue","g":"Green","y":"Yellow","s":"Silver"}
print("\nColor Code are:\n1.Red (R).\n2.Blue (B).\n3.Green (G).\n4.Yellow (Y).\n5.Silver (S).\n")

j=color
for i in range(color):
    while(j):
        userip = input("Enter Color Code:\t").lower()
        while(userip[0] in colorlist):
                print("Cannot Choose two same Color.Try Again.\n")
                userip = input("Enter Different Colour Code:\t").lower()
        if(userip[0] in precolor):  
            colorlist[i]=userip
            j -= 1
            i += 1
        else:
            print("Choose color from the given List Only.".center(50,"-"))
for i in range(len(colorlist)):
    clist.append(precolor[colorlist[i]])

print("")
print("You Choose Color: ({}) to colour your {} Fence".format(", ".join(clist),fencenum))
print("")

randcolor = []
for i in range(fencenum):
    randcolor.append(random.choice(clist))

for i in range(fencenum):
    if(len(fencecolorlist)==0):
        fencecolorlist.append(randcolor[i])
    else:
        if(randcolor[i] not in fencecolorlist):
            fencecolorlist.append(randcolor[i])  
        else:
            remlist.append(randcolor[i])
            fencecolorlist.append(None)

print(" Your Random Fence Colour Such that no two Consecutive Colours are:  ".center(100,"*"))
print("")
for i in range(fencenum):
    if(fencecolorlist[i]==None):
        fencecolorlist.append("999")
        choice =" ".join(random.choices(remlist))
        while(choice==fencecolorlist[i-1] or choice==fencecolorlist[i+1]):
            choice =" ".join(random.choices(remlist))
        fencecolorlist[i]=choice
        print("{} Fence Color will be:  {}".format(i+1,fencecolorlist[i]))
        fencecolorlist.remove("999")
    else:
        print("{} Fence Color will be:  {}".format(i+1,fencecolorlist[i]))
print("")
