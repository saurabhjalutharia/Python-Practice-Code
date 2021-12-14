import  os
os.system("cls")
#--------------------------------------------------------- NODE STRUCTURE CLASS CODE ----------------------------------------------------------------
class scllNode():
    def __init__(self, data):
        self.nodeData = data                 #FOR NODE DATA PART
        self.link = None                 #FOR NODE NEXT LINK PART
#-------------------------------------------------------SINGULAR CIRCULAR LINK LIST CODE ---------------------------------------------------------------------
class SingularCircularLinkList():
    def __init__(self):
        self.last = None                    #CONSTRUCTOR FOR KNOWING LAST NODE IN THE CIRCULAR LIST
    
    def __str__(self):
        list = []                           #FOR DISPLAY LIST CONTAIN
        if self.last == None:
            return "----------------   Circular List is Empty  ----------------"
        pointer=self.last.link              #LAST NODE IS THE FIRST NODE IN CIRCULAR LINK LIST 
        while True:                         #LAST FROM THE LAST NODE AND GO TO FIRST NODE FROM ITS LINK
            list.append(pointer.nodeData)
            pointer = pointer.link
            if pointer == self.last.link:   #MEANS WE TRAVERSED THE WHOLE CIRCULAR LIST
                break  
        return "Number of Node in Circular Links are: "+ str(len(list)) + " and Nodes are: " + str(list)
    
    def scllcreate(self, scllsize):
        if scllsize == 0:                           #IF CIRCULAR LIST IS EMPTY
            print("  Empty Singular Circular Link List Created  ".center(60,"-"))
            return
        if scllsize == 1:
            nodeData = int(input(f"Enter 1 Node Data:\t"))              #IF CIRCULAR LIST CONTAIN ONLY ONE NODE
            scllObject.scllinsert(1, nodeData)                          #INSERT FIRST NODE IN EMPTY CIRCULAR LINK LIST
            return
        else:
            nodeData = int(input(f"Enter 1 Node Data:\t"))              #FOR MORE THAN 1 NODE
            scllObject.scllinsert(1, nodeData)                          #FOR FIRST NODE ONLY
            for i in range(scllsize-1):                                 #FOR REMAINING N-1 NODES
                nodeData = int(input(f"Enter {i+2} Node Data:\t"))
                scllObject.scllinsert(2, nodeData)
        
    def scllinsert(self, choice, data = None):
        if choice == 1:                         #FOR EMPTY CIRCULAR LINK LIST
            tempNode = scllNode(data)           #NEW NODE CREATED BY NAME TEMPNODE
            self.last = tempNode                #ITS THE LAST NODE AND THE ONLY NODE 
            self.last.link = self.last          #REFER TO ITSELF
        
        elif choice == 2:                         #INSERTION IN FRONT OF THE CIRCULAR LINK LIST
            tempNode = scllNode(data)           #NEW NODE CREATED BY NAME TEMPNODE
            tempNode.link = self.last.link
            self.last.link = tempNode
        
        elif choice == 3:                         #INSERTION AT THE END PART OF THE CIRCULAR LINK LIST
            tempNode = scllNode(data)           #NEW NODE CREATED BY NAME TEMPNODE
            tempNode.link = self.last.link
            self.last.link = tempNode
            self.last = tempNode
        
        elif choice == 4:                         #INSERTION BEFORE A SPECIFIC NODE
            position = int(input("\tEnter Node Data Before which New Node will Insert:\t"))
            prepointer = self.last
            pointer = self.last.link
                                                    #IN CIRCULAR LINK LIST IF EXIT FROM THE WHILE LOOP ONLY 
            while True:                             #IF EITHER WE FOUND THE SEARCHED DATA OR NOT THERE IS NO NONE CONCEPT
                if pointer.nodeData == position:    #IF POINTER FOUND THE SEARCH NODE DATA
                    break
                prepointer = pointer
                pointer = pointer.link
                if pointer == self.last.link:       #IF POINTER CIRCLE THROUGHOUT THE WHOLE LIST AND MEET ITS OWN LINK
                    break
            if pointer == self.last.link and pointer.nodeData != position: #EXHAUST THE LIST AND CANNOT FIND THE NODE
                print("")
                print(f"  Node {position} is not Present in the List  ".center(60,"-"))
                print("")
            else:                                   #IF SEARCH NODE DATA FOUND 
                tempNode = scllNode(data)
                tempNode.link = prepointer.link
                prepointer.link = tempNode
                if prepointer == self.last:            #IF POINTER IS THE LAST NODE,  DATA WILL BE LAST NODE SO REPLACE POINTER
                    self.last = tempNode
        
        elif choice == 5:                         #INSERTION AFTER A SPECIFIC NODE
            position = int(input("\tEnter Node Data After which New Node will Insert:\t"))
            pointer = self.last.link
                                                    #IN CIRCULAR LINK LIST IF EXIT FROM THE WHILE LOOP ONLY 
            while True:                             #IF EITHER WE FOUND THE SEARCHED DATA OR NOT THERE IS NO NONE CONCEPT
                if pointer.nodeData == position:    #IF POINTER FOUND THE SEARCH NODE DATA
                    break
                pointer = pointer.link
                if pointer == self.last.link:       #IF POINTER CIRCLE THROUGHOUT THE WHOLE LIST AND MEET ITS OWN LINK
                    break
            if pointer == self.last.link and pointer.nodeData != position: #EXHAUST THE LIST AND CANNOT FIND THE NODE
                print("")
                print(f"  Node {position} is not Present in the List  ".center(60,"-"))
                print("")
            else:                                   #IF SEARCH NODE DATA FOUND 
                tempNode = scllNode(data)
                tempNode.link = pointer.link
                pointer.link = tempNode
                if pointer == self.last:            #IF POINTER IS THE LAST NODE,  DATA WILL BE LAST NODE SO REPLACE POINTER
                    self.last = tempNode
        else:
            print("  Invalid Input  ".center(50,"-"))
            print("")

    def sclldelete(self, choice, data = None):
        if choice == 1:
            if self.last is None:                     #LIST IS EMPTY
                return
            if self.last.link == self.last:           #ONLY ONE ELEMENT IN THE LIST 
                self.last = None                      #SET SELF REFERENCE TO NULL, NO REERENCE, NODE DELETE 
                return
            self.last.link = self.last.link.link      #SET Nth NODE LINK TO 1st NODE LINK IINK i.e 2nd NODE

        elif choice == 2:
            if self.last is None:                     #LIST IS EMPTY
                return
            if self.last.link == self.last:           #ONLY ONE ELEMENT IN THE LIST 
                self.last = None                      #SET SELF REFERENCE TO NULL, NO REERENCE, NODE DELETE
                return
            pointer = self.last.link                  #POINTER POINTS TO THE FIRST NODE
            while pointer.link != self.last:          #POINTER REFERS TO THE PREVIOUS NODE
                pointer = pointer.link                #TRAVERSE
            pointer.link = self.last.link
            self.last = pointer
        
        elif choice == 3:
            if self.last is None:                     #LIST IS EMPTY
                return
            if self.last.link == self.last and self.last.nodeData == data: 
                self.last = None                      #ONLY ONE NODE
                return
            if self.last.link.nodeData == data:       #DELETE FIRST NODE
                self.last.link = self.last.link.link
                return

            pointer = self.last.link
            while pointer.link != self.last.link:      #POINTER INITIALIZE FIRST NODE THE TRAVERSE THE LIST
                if pointer.link.nodeData == data:
                    break
                pointer = pointer.link
            if pointer.link == self.last.link:
                print(data,"not found in the list")
            else:                                      #POINTER REFERS TO THE PREVIOUS NODE
                pointer.link = pointer.link.link
                if self.last.nodeData == data:
                    self.last = pointer
        else:
            print("  Invalid Input  ".center(50,"-"))
            print("")

#--------------------------------------------------------------- MAIN CODE ---------------------------------------------------------------------
if __name__ == "__main__":
    def creater():
       print("The Creater of this Code is: "+chr(83)+chr(65)+chr(85)+chr(82)+chr(65)+chr(66)+chr(72)+" "+chr(74)+chr(65)+chr(76)+chr(85)+chr(84)+chr(72)+chr(82)+chr(73)+chr(65))
    scllObject = SingularCircularLinkList()

    print("   WELCOME In Singular Circlular Link List Data Structure  ".center(70,"*"))
    print("")
    sizenum = int(input("Enter Size For Circular Link List:\t"))
    print("")
    scllObject.scllcreate(sizenum)

    while(True):
        print('''
    What would you like to do?
        1. Display the Current List         2. Insert a New Item in the List           
        3. Delete an Item from the List     4. Exit\n''')

        userinput = int(input("Enter Your Choice:\t"))
        
        if (userinput == 1010):
            creater()
        elif (userinput == 1):
            print(scllObject) 
        elif (userinput == 2):
            print("")
            print("  Circular Link List Insertion Operations  ".center(50,"-"))
            print('''
            1. Insert at the FRONT of the List
            2. Insert at the END of the List
            3. Insert Before a Specificy Node
            4. Insert After a Specificy Node\n''')
            userchoice = int(input("\tEnter Your Choice:\t"))
            if userchoice == 1:                                     
                newnodedata = int(input("\tEnter New Node Data:\t"))
                scllObject.scllinsert(2, newnodedata)
            if userchoice == 2:                                     
                newnodedata = int(input("\tEnter New Node Data:\t"))
                scllObject.scllinsert(3, newnodedata)
            if userchoice == 3:                                     
                newnodedata = int(input("\tEnter New Node Data:\t"))
                scllObject.scllinsert(4, newnodedata)
            if userchoice == 4:                                     
                newnodedata = int(input("\tEnter New Node Data:\t"))
                scllObject.scllinsert(5, newnodedata)
        
        elif (userinput == 3):
            print("")
            print("  Singular Circular Link List Deletion Operations  ".center(70,"-"))
            print('''
            1. Delete From the First Position of the List
            2. Delete From the Last Position of the List
            3. Delete a Specificy Node\n''')
            userchoice = int(input("\tEnter Your Choice:\t"))
            if userchoice == 1:
                scllObject.sclldelete(1)                    #DELETE FROM FRONT
            elif userchoice == 2:
                scllObject.sclldelete(2)                    #DELETE FROM REAR
            elif userchoice == 3:
                deletnodedata = int(input("\tEnter Delelte Node Data:\t"))
                scllObject.sclldelete(3, deletnodedata)     #DELETE SPECIFIC A NODE
            else:
                print("  Invalid Input  ".center(50,"-")) 

        elif (userinput == 4):
            print("")
            print("\t\tThanks For using Singular Circlular Link List Data Structure\n\n")
            exit()
        else:
            print("")
            print("   Invalid Input. Try Again.   ".center(60,"-"))
#-------------------------------------------------------------------- CODE END ----------------------------------------------------------