import os
os.system("cls")

print("Simple Calculator".center(50,"-"))
print("\nWhat would you like to do : ")
print("\t1. Addition \n\t2. Substraction \n\t3. Multiplication \n\t4. Division \n\t5. Exit")

while(True):
    choice = int(input("\nEnter Your Choice:\t"))
    print("")
    while(choice>5 or choice==0):
        print("  Enter in the Range Only(1-5)  ".center(50,'-'))
        choice = int(input("\nEnter Your Choice:\t"))
        print("")
    if(choice == 5):
        exit()
    num1 = int(input("Enter Your First Number :\t"))
    num2 = int(input("Enter Your Second Number :\t"))
    
    if(choice == 1):
        result = num1 + num2
        print("The SUM of these two numbers are:\t {} + {} = {}.".format(num1,num2,result))
    elif(choice == 2):
        result = num1 - num2
        print("The DIFFERENCE of these two numbers are:\t{} - {} = {}.".format(num1,num2,result))
    elif(choice == 3):
        result = num1 * num2
        print("The MULTIPLICATION of these two numbers are:\t{} * {} = {}.".format(num1,num2,result))
    elif(choice == 4):
        result = num1 / num2
        print("The DIVISION of these two numbers are:\t{} / {} = {:.2f}.".format(num1,num2,result))
    else:
        print("   Invalid Input.Try Again   ".center(50,"-"))

    
    

