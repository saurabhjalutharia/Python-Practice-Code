import random
import os
os.system("cls")

print("Enter the Guessed Number in the Range 1 to 50:".center(100,"-"))
print("You will get 5 Chance and 3 Hint. Press ""0"" for Hint".center(100,"-"))
ans = random.randint(1,51)
half=ans//2
count=0
chance=5
hint = 3
hintreq=None
multiple=[]
while(chance!=0):
    num = int(input(""))
    if(num==0):
        if(hint!=0):
            hint -= 1
            if(hint==2):
                if(ans%2==0):
                    print("Your 1st Hint.".center(50,"*"))
                    print("Random Number is an Even number.")
                    print("{} Hint Left.".format(hint))
                else:
                    print("Your 1st Hint.".center(50,"*"))
                    print("Random Number is an Odd number.")
                    print("{} Hint Left.".format(hint))
            if(hint==1):
                if(ans<=half):
                    print("Your 2nd Hint.".center(50,"*"))
                    print("Random Number is Less than {}.".format(half))
                    print("{} Hint Left.".format(hint))
                else:
                    print("Your 2nd Hint.".center(50,"*"))
                    print("Random Number is Greater than {}.".format(half))
                    print("{} Hint Left.".format(hint))
            if(hint==0):
                for i in range(1,11):
                    if((ans%i)==0):
                        multiple.append(i)
                if(multiple.__len__()==1):
                    print("Your 3rd Hint.".center(50,"*"))
                    print("Random Number is a Prime Number\t")
                    print("{} Hint Left.".format(hint))
                else:
                    print("Your 3rd Hint.".center(50,"*"))
                    print("Random Number is Multiple of\t", multiple)
                    print("{} Hint Left.".format(hint))
        else:
            print("No Hint Left.")
    else:
        if(num<51 and num>=1):
            if(num!=ans):
                chance -= 1
                count +=1
                print("You Gussed Wrong Number. Chance Left: {}".format(chance))
                print("Press ""0"" for Hint. Hint's Left:    {}\n".format(hint))
            else:
                print("You Guessed Correct. The Random Number was:\t",ans)
                if(hint==3):
                    print("     You did an Excellent job       ".center(50,"#"))
                if(hint==2):
                    print("     You did Good job    ".center(50,"#"))
                if(hint==1):
                    print("     You Need Little Practice    ".center(50,"#"))
                if(hint==0):
                    print("     Poor Perfomance     ".center(50,"#"))
                exit()
        else:
            print("Enter Number in the Range 1 to 50 Only.")
print("You Lose. The Random Number was: {}".center(50,"-").format(ans))
exit()
