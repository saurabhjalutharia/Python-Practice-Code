import  os
os.system("cls")
#--------------------------------------------------------- NODE STRUCTURE CLASS CODE ----------------------------------------------------------------
class dllNode():
    def __init__(self, data):
        self.nodeData = data                 #FOR NODE DATA PART
        self.nextLink = None                 #FOR NODE NEXT LINK PART
        self.previousLink = None             #FOR NODE PREVIOUS LINK PART
#------------------------------------------------------------ DOUBLY LINK LIST CODE ---------------------------------------------------------------------
class doublyLinkList():
    def __init__(self):
        self.start = None                    #CONSTRUCTOR FOR STARTING POINT
    
    def __str__(self):
        list =[]                             #LIST TO CONTAIN NODE DATA PART FOR PRINTING
        if self.start is None:               #CHECK LIST EMPTY
            print("  Doubly Link List is Empty   ".center(50,"-"))
            return
        else:
            pointer = self.start                #SET POINTER TO START POINT
            while pointer is not None:
                list.append(pointer.nodeData)   #ADD NODE DATA INTO LIST
                pointer=pointer.nextLink        #UPDATE POINTER FOR TRAVERSING NEXT NODE
            return "Total Node in the List are: " + str(len(list)) + " and List is: " + str(list)      #RETURN LIST CONTAINING ALL NODE DATA PART

    def dllcreate(self, num):                   #CREATE A NEW DOUBLY LINK LIST
        if num == 0:
            print("  An Empty Doubly Link List Created  ".center(50,"-"))
            print("")
            return
        elif num == 1:                          
            nodeData = int(input(f"Enter 1 Node Data:\t"))
            dllObject.dllinsertion(1, nodeData)                     #FOR FIRST NODE ONLY
        else:
            nodeData = int(input(f"Enter 1 Node Data:\t"))          #FOR MORE THAN 1 NODE
            dllObject.dllinsertion(1, nodeData)                     #FOR FIRST NODE ONLY
            for i in range(num-1):                                  #FOR REMAINING N-1 NODES
                nodeData = int(input(f"Enter {i+2} Node Data:\t"))
                dllObject.dllinsertion(3, nodeData)                 #FOR ADDING AT THE LAST PART OF THE LIST
            
    def dllinsertion(self, choice, data = None):
        if choice == 1:                                 #FOR INSERTION IN AN EMPTY LIST
            tempNode = dllNode(data)                    #CREATE A NEW NODE
            self.start = tempNode                       #START POINTS TO NEW NODE
        
        elif choice == 2:                               #FOR INSERTION AT THE FRONT OF THE LIST 
            tempNode = dllNode(data)
            tempNode.nextLink = self.start              #NEW NODE NEXT LINK POINTS TO STARING POINT
            self.start.previousLink = tempNode          #START PREVIOUS LINK POINTS TO NEW NODE
            self.start = tempNode                       #START POINTS TO NEW NODE
        
        elif choice == 3:                               #FOR INSERTION AT THE END OF THE LIST
            tempNode = dllNode(data)
            pointer = self.start                        #POINTER POINTS TO THE START OF THE LIST
            while pointer.nextLink is not None:
                  pointer = pointer.nextLink            #FOR TRAVERSING THE LIST
            pointer.nextLink = tempNode                 #POINTER NEXT LINK POINTS TO THE NEW NODE
            tempNode.previousLink = pointer             #NEW NODE PREVIOUS LINK POINTS TO THE POINTER

        elif choice == 4:                               #FOR INSERTION BEFORE A SPECIFIC NODE
            position = int(input("\tEnter Node Data Before which New Node will Insert:\t"))
            if self.start is None:
                print("List is Empty")
                return
            if self.start.nodeData == position:         #IF FIRST DATA ITEM IS THE SEARCHED ITEM
                tempNode = dllNode(data) 
                tempNode.nextLink = self.start
                self.start.previousLink = tempNode
                self.start = tempNode
                return
            pointer = self.start
            while pointer is not None:                  #FOR TRAVERSING THE LIST
                if pointer.nodeData == position:        #IF POINTER POINTING NODE CONTAIN THE SEARCHED DATA ITEM
                    break
                pointer = pointer.nextLink
            
            if pointer is None:                         #IF SEARCH ELEMENT NOT FOUND IN THE LIST
                print(f" Node {position} is Not Found in the List ")
                print("")
            else:                                       #ELEMENT FOUND AND NOW INSERT THE NEW NODE
                tempNode = dllNode(data) 
                tempNode.previousLink = pointer.previousLink
                tempNode.nextLink = pointer
                pointer.previousLink.nextLink = tempNode
                pointer.previousLink = tempNode

        elif choice == 5:                               #FOR INSERTION AFTER A SPECIFIC NODE
            position = int(input("\tEnter Node Data After which New Node will Insert:\t"))
            tempNode = dllNode(data)                    #NEW NODE CREATE
            pointer = self.start                        #POINTER POINTS TO THE STARTING POINT OF THE LIST
            while pointer is not None:
                if pointer.nodeData == position:
                    break
                pointer = pointer.nextLink
            if pointer is None:
                print(f" Node {position} is Not Found in the List ")
                print("")
            else:
                tempNode.previousLink = pointer
                tempNode.nextLink = pointer.nextLink
                if pointer.nextLink is not None: 
                    pointer.nextLink.previousLink = tempNode
                pointer.nextLink=tempNode
        else:
            print("  Invalid Input  ".center(50,"-"))
    
    def dlldeletion(self, choice, data = None):
        if choice == 1:                                 #FOR DELETING FROM FRONT
            if self.start is None:                      #IF LIST IS EMPTY
                print("  No Node is Present in the List  ".center(50,"-"))
                return
            if self.start.nextLink is None:             #ONLY ONE NODE PRESENT IN THE LIST
                print("  Node Deleted. Now List is Empty  ".center(50,"-"))
                self.start = None                       #SET START TO NONE
                return
            self.start = self.start.nextLink            #START POINTS TO THE SECOND NODE IN THE LIST
            self.start.previousLink = None              #START SET ITS PREVIOUS LINK TO NULL SO THAT NO REFERENCE FOR FIRST LINK

        elif choice == 2:                               #FOR DELETING FROM END
            if self.start is None:                      #IF LIST IS EMPTY
                print("  No Node is Present in the List  ".center(50,"-"))
                return
            if self.start.nextLink is None:             #ONLY ONE NODE PRESENT IN THE LIST
                print("  Node Deleted. Now List is Empty  ".center(50,"-"))
                self.start = None                       #SET START TO NONE
                return
            pointer = self.start                        #POINTER POINTS TO THE STARTING POINT OF THE LIST
            while pointer.nextLink.nextLink is not None:
                pointer = pointer.nextLink              #TRAVERSE LIST UPTO SECOND LAST NODE
            pointer.nextLink = None                     #SET SECOND LAST NODE NEXT LINK TO NONE, NO REFERENCE TO LAST NODE
        
        elif choice == 3:                               #FOR DELETING A SPECIFIC NODE
            if self.start is None:                      #IF LIST IS EMPTY
                print("  No Node is Present in the List  ".center(50,"-"))
                return
            if self.start.nextLink is None:             #FIRST NODE IS THE NODE TO DELETE
                if self.start.nodeData == data:
                    self.start = None                   #SET START TO NONE
                    print("  Node Deleted. Now List is Empty  ".center(50,"-"))
                    return
                else:
                    print(f" Node {data} is not Present in the List")
                    print("")
                    return
            if self.start.nodeData == data:             #IN THE LIST IF FIRST NODE IS THE DELETE NODE
                self.start = self.start.nextLink        #START POINT TO THE NEXT OF THE FIRST POINT
                self.start.previousLink = None          #START PREVIOUS SET TO NULL
                print(f"  Node {data} Deleted Successfully  ".center(50,"-"))
                return

            pointer = self.start.nextLink                        #POINTER POINTS TO THE STARTING POINT OF THE LIST
            while pointer.nextLink is not None:
                if pointer.nodeData == data:
                    break
                pointer = pointer.nextLink
            if pointer.nextLink is not None:                      #WHEN NODE PRESNT IN BETWEEN NODES
                pointer.previousLink.nextLink = pointer.nextLink
                pointer.nextLink.previousLink = pointer.previousLink
            else:                                                 #NODE PRESENT AT THE LAST
                if pointer.nodeData == data:
                    pointer.previousLink.nextLink = None
                    print(f"  Node {data} Deleted from the List  ".center(50,"-"))
                    print("")
                    return
                else:
                    print(f"  Node {data} Deleted Successfully  ".center(50,"-"))
                    return
        else:
            print("  Invalid Input  ".center(50,"-"))

    def dllsearch(self, data):
        nodeCounter = 0                                 #TO COUNT NUMBER OF NODE PRESENT IN THE LIST
        if self.start is None:
            print("  List is Empty  ".center(50,"-"))
            return
        pointer = self.start                             #POINTS TO THE STARTING POINT OF THE LIST
        while pointer.nextLink is not None:
            nodeCounter += 1                             #NODE COUNTER INCREMENT BY 1 EACH TIME
            if pointer.nodeData == data:
                break
            pointer = pointer.nextLink                    #NODE TRAVERSING
        if pointer.nodeData == data:
            print(f"\tNode: {data} is present at Index: {nodeCounter}")
            return
        else:
            print(f"\tNode: {data} is Not Present in the List")
            print("")
            return
    
    def dllreverse(self):
        if self.start is None:                             #IF LIST IS EMPTY
            print("  List is Empty  ".center(50,"-"))
            return
        print("")
        print("List Before Reverse is: ", dllObject.__str__())
        pointer1 = self.start                           #POINTER 1 POINT TO THE STARTING POINT OF THE LIST
        pointer2 = pointer1.nextLink                    #POINTER 2 POINTS TO THE NEXT LINK OF THE POINTER 1 NODE
        pointer1.nextLink = None                        #POINTER 1 NEXT LINK PART SET TO NULL AS AN END FOR REVERSE LINK
        pointer1.previousLink = pointer2                #POINTER 1 PREVIOUS LINK POINTS TO POINTER 2 NODE I.E 2 NODE
        while pointer2 is not None:
            pointer2.previousLink = pointer2.nextLink
            pointer2.nextLink = pointer1
            pointer1 = pointer2
            pointer2 = pointer2.previousLink
        self.start = pointer1                           #STRAT POINT TO POINTER 1 WHICH IS THE LAST NODE NOW AFTER TRAVERSING
        print("List After Reverse is:  ", dllObject.__str__())
        print("")
#--------------------------------------------------------------- MAIN CODE ---------------------------------------------------------------------
if __name__ == "__main__":
    def creater():
       print("The Creater of this Code is: "+chr(83)+chr(65)+chr(85)+chr(82)+chr(65)+chr(66)+chr(72)+" "+chr(74)+chr(65)+chr(76)+chr(85)+chr(84)+chr(72)+chr(82)+chr(73)+chr(65))
    dllObject = doublyLinkList()

    print("   WELCOME In Doubly Link List Data Structure  ".center(60,"*"))
    print("")
    nodenum = int(input("Enter number of Nodes:\t"))
    print("")
    dllObject.dllcreate(nodenum)

    while(True):
        print('''
    What would you like to do?
        1. Display the Current List         2. Insert a New Item in the List           
        3. Delete an Item from the List     4. Search Element in the List
        5. Reverse List                     6. Exit\n''')

        userinput = int(input("Enter Your Choice:\t"))
        
        if (userinput == 1010):
            creater()
        elif (userinput == 1):
            print(dllObject)                                          #DISPLAY THE CURRENT LIST
        elif (userinput == 2):
            print("")
            print("  Doubly Link List Insertion Operations  ".center(50,"-"))
            print('''
            1. Insert at the First Position of the List
            2. Insert at the Last Position of the List
            3. Insert Before a Specificy Node
            4. Insert After a Specificy Node\n''')
            userchoice = int(input("\tEnter Your Choice:\t"))
            if userchoice == 1:                                     
                newnodedata = int(input("\tEnter New Node Data:\t"))
                dllObject.dllinsertion(2, newnodedata)                  #FOR INSERTION OF NEW NODE AT THE FRONT OF THE LIST
            elif userchoice == 2:
                newnodedata = int(input("\tEnter New Node Data:\t"))
                dllObject.dllinsertion(3, newnodedata)                  #FOR INSERTION OF NEW NODE AT THE LAST OF THE LIST    
            elif userchoice == 3:
                newnodedata = int(input("\tEnter New Node Data:\t"))
                dllObject.dllinsertion(4, newnodedata)                  #FOR INSERTION OF NEW NODE BEFORE A SPECIFIC NODE   
            elif userchoice == 4:
                newnodedata = int(input("\tEnter New Node Data:\t"))
                dllObject.dllinsertion(5, newnodedata)                  #FOR INSERTION OF NEW NODE AFTER A SPECIFIC NODE
            else:
                print("  Invalid Input  ".center(50,"-"))    
       
        elif (userinput == 3):
            print("")
            print("  Doubly Link List Deletion Operations  ".center(50,"-"))
            print('''
            1. Delete From the First Position of the List
            2. Delete From the Last Position of the List
            3. Delete a Specificy Node\n''')
            userchoice = int(input("\tEnter Your Choice:\t"))
            if userchoice == 1:
                dllObject.dlldeletion(1)                    #DELETE FROM FRONT
            elif userchoice == 2:
                dllObject.dlldeletion(2)                    #DELETE FROM REAR
            elif userchoice == 3:
                deletnodedata = int(input("\tEnter Delelte Node:\t"))
                dllObject.dlldeletion(3, deletnodedata)     #DELETE SPECIFIC NODE
            else:
                print("  Invalid Input  ".center(50,"-"))    
        
        elif (userinput == 4):
            userchoice = int(input("\tEnter Node Data for Searching:\t"))
            print("")
            dllObject.dllsearch(userchoice)                 #FOR SEARCHING A SPECIFIC NODE IN THE LIST
        elif (userinput == 5):
            dllObject.dllreverse()                          #TO REVERSE THE LIST
        elif (userinput == 6):
            print("")
            print("\t\tThanks For using Doubly Link List Data Structure\n\n")
            exit()
        else:
            print("")
            print("   Invalid Input. Try Again.   ".center(60,"-"))
#-------------------------------------------------------------------- CODE END ----------------------------------------------------------