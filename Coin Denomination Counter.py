import os
os.system("cls")

cc=[100,50,20,10,5,2,1]                                         #CURRENCY DENOMINATION
count=[0]*7                                                     #LIST OF NUMBER OF DENOMINATION
print("   To Exit Press (0)   ".center(50,"-"))
amount=input("\nEnter Amount: \t")                              #USER ENTER AMOUNT

while(amount.isdigit()==False):                                 #CHECK WHEATHER INPUT IS VALID NUMBER OR NOT
    print("  Enter Number(s) Only  ".center(50,"-"))
    amount=input("\nEnter Amount: \t")                          #ASK AGAIN FOR USER INPUT UNTILL INPUT IS VALID
amount = int(amount)                                            #IF INPUT IS ALREADY VALID, PROGRAM CONTINUE

while(amount>0):
    for i in range(len(cc)):                                    #LIST OF VALID COIN CURRENCY
        rem = amount//cc[i]                                     #FLOOR VALUE OF THE REMAINDER
        while(rem!=0):
            count[i] += rem                                     #INCREAMENT COIN COUNT BY 1
            amount -= (rem*cc[i])                               #REDUCE THE AMOUNT BY THE DENOMINATION THAT ALREADY HAS TAKEN CARE OF
            rem = amount//cc[i]
    print("Total 100 rupee Denomition Need are:\t",count[0])
    print("Total  50 rupee Denomition Need are:\t",count[1])
    print("Total  20 rupee Denomition Need are:\t",count[2])
    print("Total  10 rupee Denomition Need are:\t",count[3])
    print("Total   5 rupee Denomition Need are:\t",count[4])
    print("Total   2 rupee Denomition Need are:\t",count[5])
    print("Total   1 rupee Denomition Need are:\t",count[6])
    count=[0]*7                                                   #RESET THE COUNT LIST FOR NEXT RUN
    amount=int(input("\nEnter Amount: \t"))                       #FOR NEXT RUN USER ENTER AMOUNT AGAIN. IF (0) PROGRAM EXIT
print("   THANKS   ".center(50,"-"))
print("\n")
exit()
