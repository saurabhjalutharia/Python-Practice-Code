import random, os
os.system("cls")
print("Press 0 for Exit".center(50,"*"))
roll=None
while(roll!=0):
    sum = 0
    roll=int(input("\nEnter the number of times Dice will roll:\t"))
    for i in range(roll):
        dig=random.randint(1,6)
        print("For {} time Dice Roll it Generated:   {}".format(i+1,dig))
        sum += dig
    print("\nTotal Sum of Dice Digit is:  ",sum)
