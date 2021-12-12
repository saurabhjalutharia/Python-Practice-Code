import os
os.system("cls")

#------------------------------------------------------------- NEW NODE CODE ---------------------------------------------------------------------
class NewNode():
    def __init__(self, data):
        self.nodeData = data         #CONTAIN NODE DATA WHEN EVERY TIME A NEW NODE CREATE
        self.link = None             #CONTAIN LINK OF NEXT THE NODE WHEN EVERY TIME A NEW NODE CREATE

#--------------------------------------------------------- NODE OPERATIONS CODE ----------------------------------------------------------------------
class LinkList():
    def __init__(self):                                         #EVERY LIST CONTAIN A STARTING POINT
        self.start = None

    def __str__(self):                                          #DISPLAY THE COMPLETE LIST
        if self.start is None:                                  #IF LIST IS EMPTY
            return '[]'
        pointer = self.start
        result = ''.join(['[', str(pointer.nodeData)])          #ADD [, AT STARTING BEFORE RETURNING TO USER. ONLY FOR GOOD REPRESENTATION 
        pointer = pointer.link                                  #HOP POINTER TO THE NEXT POINTER OF THE LIST
        while pointer is not None:
            result = ', '.join([result, str(pointer.nodeData)]) #ADD EVERY NODE DATA IN THE RETURN LIST
            pointer = pointer.link
        result = ''.join([result, ']'])                          #AT LAST ADD ] FOR CLOSING THE LIST ONLY FOR REPESENTAION

        return result

    def __len__(self):                                            #DISPLAY THE TOTAL NUMBER OF NODES IN THE LIST
        pointer = self.start                                      #MARK/POINT THE POINTER TO THE STARTING POINT OF THE LIST
        nodecounter = 0                                           #COUNT NUMBER OF NODES WHILE TRAVERSING
        while pointer is not None:
            nodecounter += 1
            pointer = pointer.link
        return f"Total Node(s) in the List are: {nodecounter}"     #RETURN TOTAL NUMBER OF NODES
    
    def createNewList():                                           #IT WILL CREATE A NEW LIST
        nodeNum = int(input('Enter the Number of Nodes:\t'))
        if nodeNum == 0:
            print("Blank Link List Is Created")
            return linkListObject                                   #RETURN NULL LINK LIST
        for i in range(nodeNum):
            data = int(input(f"Enter the {i+1} Element For Insertion: "))
            linkListObject.listInsertion(2, data)
        return linkListObject
    
    def listInsertion(self, choice, data):
        if choice == 1:                                     #FOR INSERTION OF NEW NODE AT THE BIGINING OF THE LIST
            tempNode = NewNode(data)
            tempNode.link = self.start
            self.start = tempNode
            return
        
        elif choice == 2:                                   #FOR INSERTION OF NEW NODE AT THE ENDING OF THE LIST
            if self.start is None:                          #IF START IS NONE MEANS THERE IS NO NODE IN THE LIST 
                linkListObject.listInsertion(1, data)       #ADD FIRST ELEMENT IN THE LIST
                return
            else:
                pointer = self.start
                tempNode = NewNode(data)            #CREATE TEMPORARY NODE OF NEW NODE
                while pointer.link is not None:
                    pointer = pointer.link          #HOP POINTER TILL WE REACH AT THE LAST NODE OF THE LIST
                pointer.link = tempNode             #POINT THE LAST NODE LINK TO THE NEW NODE AND NEW NODE LINK WILL BE NONE BY DEFAULT
                return
        
        elif choice == 3:                           #FOR INSERTION OF NEW NODE AT BEAFORE A SPECIFIC NODE
            prefix = int(input("\tEnter Node Data Where New Node Will be Add as Prefix:\t"))                                 
            if self.start is None:                   #CASE FOR EMPTY LIST
                print('List is empty')
                return
            if self.start.nodeData == prefix:        #CASE FOR IF ONLY ONE ELEMENT IS PRESENT IN THE LIST
                linkListObject.listInsertion(1, data)
            pointer = self.start
            while pointer.link is not None:
                if pointer.link.nodeData == prefix:  #POINTER POINTS TO NEXT NODE DATA WHILE STANDING ONE STEP BACK TO THE POINTING NODE
                    break
                pointer = pointer.link
            if pointer is None:
                print(prefix, 'Node is Not Present in the List')    #SEARCHED NODE NOT IN THE LIST
            else:
                tempNode = NewNode(data)        
                tempNode.link = pointer.link
                pointer.link = tempNode
        
        elif choice == 4:                   #FOR INSERTION OF NEW NODE AT AFTER A SPECIFIC NODE
            surfix = int(input("\tEnter Node Data Where New Node Will be Add as Surfix:\t"))
            pointer = self.start
            while pointer is not None:
                if pointer.nodeData == surfix:
                    break
                pointer = pointer.link
            if pointer is None:
                print(surfix, 'Node is Not Present in the List')
            else:
                tempNode = NewNode(data)
                tempNode.link = pointer.link
                pointer.link = tempNode
        
        elif choice == 5:                   #FOR INSERTION OF NEW NODE AT A PARTICULAR POSITION
            index = int(input("\tEnter Position/Index for New Node:\t"))
            if self.start is None:
                print('List is Empty'.center(50,"-"))
                return
            elif index == 1:
                linkListObject.listInsertion(1, data)
            else:
                pointer = self.start
                i = 1
                while i <= index-1 and pointer is not None:
                    if i == index-1:
                        break
                    i += 1
                    pointer = pointer.link
                if pointer is not None:
                    tempNode = NewNode(data)
                    tempNode.link = pointer.link
                    pointer.link = tempNode
                else:
                    print('List does not Contain ', index, 'Elements')
        else:
            print("Invalid Input")
    
    def reverseList(self):
        previous = None
        pointer = self.start
        while pointer is not None:
            link = pointer.link
            pointer.link = previous
            previous = pointer
            pointer = link
        self.start = previous
        print("")
        print("   List reverse Successfully   ".center(50,"-"))
        print("")
    
    def listDeletion(self, choice, data=None):
        self.choice = choice
        if self.choice == 1:
            if self.start is None:
                return
            self.start = self.start.link
            print("")
            print("  First Node Deleted Successfully of the List  ".center(60,"-"))
        
        if self.choice == 2:
            if self.start is None:
                return
            if self.start.link is None:
                self.start = None
            pointer = self.start
            while pointer.link.link is not None:            #TO HOP UPTO SECOND LAST NODE
                pointer = pointer.link
            pointer.link = None
            print("")
            print("  Last Node Deleted Successfully of the List  ".center(60,"-"))

        if self.choice == 3:
            if self.start is None:
                print('List is Empty')
            if self.start.link == data:
                self.start = self.start.link
                return
            pointer = self.start
            while pointer.link is not None:
                if pointer.link.nodeData == data:
                    pointer.link = pointer.link.link
                    print("")
                    print(f"  Node {data} Deleted Successfully from the List  ".center(60,"-"))
                    return
                pointer = pointer.link    
            print(data, 'Not Found in the List')
    
    def listSearch(self, data):
        pointer = self.start
        elementindex = 1
        while pointer is not None:
            if pointer.nodeData == data:
                print(f'\t\t{pointer.nodeData} is at Position: {elementindex}')
                return elementindex
            pointer = pointer.link
            elementindex += 1
        else:
            print(f'  {data} Not Found in the List  '.center(50,"-"))
            print("")
    
    def sortList(self, choice):
        self.choice = choice
        if self.choice == 1:
            pass

        if self.choice == 2:
            print("")
            print("Before Sorting Link List is: ", linkListObject)
            end = None
            while end != self.start.link:
                pointer = self.start
                while pointer.link != end:
                    temppointer = pointer.link
                    if pointer.nodeData > temppointer.nodeData:
                        pointer.nodeData, temppointer.nodeData = temppointer.nodeData, pointer.nodeData
                    pointer= pointer.link
                end = pointer
            print("After Sorting Link List is: ", linkListObject)
            print("")

        if self.choice == 3:
            print("")
            print("Before Sorting Link List is: ", linkListObject)
            end = None
            while end != self.start.link:
                r = pointer = self.start
                while pointer.link != end:
                    temppointer = pointer.link
                    if pointer.nodeData > q.nodeData:
                        pointer.link = q.link
                        temppointer.link = pointer
                        if pointer!= self.start:
                            r.link = temppointer
                        else:
                            self.start = temppointer
                        pointer, temppointer = temppointer, pointer
                    r = pointer
                    pointer= pointer.link
                end = pointer
            print("After Sorting Link List is: ", linkListObject)
            print("")

    def has_cycle(self):
        if linkListObject.cycleInList(3) is None:
            return False
        else:
            return True

    def cycleInList(self, choice, data = None):
        self.choice = choice
        if self.choice == 1:
            if self.start is None:
                return
            pointer = self.start
            px = None
            previous = None
            while pointer is not None:
                if pointer.link == data:
                    px = pointer
               previous = pointer
                pointer = pointer.link
            if px is not None:
                previous.link = px
            else:
                print(data, " Not Present in the List")
                
        if self.choice == 2:
            c = self.find_cycle()
            if c is None:
                return
            print("Node at Where the Cycle was Detected is: ", c.nodeData)
            pointer = c
            q = c
            len_cycle = 0
            while True:
                len_cycle += 1
                q = q.link
                if pointer == q:
                    break
            print("Length of the Cycle is: ", len_cycle)

            len_rem_list = 0
            pointer = self.start
            while pointer != q:
                len_rem_list += 1
                pointer = pointer.link
                q = q.link
            print("Number of nodes not included in the cycle are : ", len_rem_list)
            length_list = len_cycle + len_rem_list
            print("Length of the list is : ", length_list)
            pointer = self.start
            for i in range(length_list - 1):
                pointer = pointer.link
            pointer.link = None

        if self.choice == 3:                #HARE AND TORTOISE ALGORITHM
            if self.start is None or self.start.link is None:
                return None
            hare = self.start
            tortoise = self.start
            while tortoise is not None and tortoise.link is not None:
                hare = hare.link
                tortoise = tortoise.link.link
                if hare == tortoise:
                    return hare
            return None
#---------------------------------------------------------- MAIN LINK LIST CODE FOR USER --------------------------------------------------------------------------    
linkListObject = LinkList()     #LINK LIST CLASS OBJECT
def creater():
   print("The Creater of this Code is: "+chr(83)+chr(65)+chr(85)+chr(82)+chr(65)+chr(66)+chr(72)+" "+chr(74)+chr(65)+chr(76)+chr(85)+chr(84)+chr(72)+chr(82)+chr(73)+chr(65))

if __name__ == '__main__':
    linkListObject = LinkList()
    while(True):
        print('''
    What would you like to do?
        1. Display the Current List         2. Create a New List          
        3. Total Nodes in the List          4. Insert a New Item in the List
        5. Delete an Item from the List     6. Search Element in the List
        7. Sort List                        8. Cycle In List
        9. Reverse List                     10. Exit\n''')
        userinput = int(input("Enter Your Choice:\t"))
        
        if (userinput == 1010):
                creater()
        
        elif (userinput == 1):
            print(linkListObject)

        elif (userinput == 2):
            LinkList.createNewList()
        
        elif (userinput == 3):
            print(linkListObject.__len__())
        
        elif (userinput == 4):
            print("")
            print("   Insertion Operation on List   ".center(50,"-"))
            print("\t1. Insert a New Node at the Beginning of List\n\t2. Insert a New Node at the End of List\n\t3. Insert a New Node Before a Specific Node in the List\n\t4. Insert a New Node After a Specific Node in the List\n\t5. Insert a Node at a Given Position/Index\n")
            insertionChoice = int(input("\tEnter Your Choice:\t"))
            if insertionChoice == 1:
                inertionnodedata = int(input("\tEnter New Node Data:\t"))
                linkListObject.listInsertion(1, inertionnodedata)
            elif insertionChoice == 2:
                inertionnodedata = int(input("\tEnter New Node Data:\t"))
                linkListObject.listInsertion(2, inertionnodedata)
            elif insertionChoice == 3:
                inertionnodedata = int(input("\tEnter New Node Data:\t"))
                linkListObject.listInsertion(3, inertionnodedata)
            elif insertionChoice == 4:
                inertionnodedata = int(input("\tEnter New Node Data:\t"))
                linkListObject.listInsertion(4, inertionnodedata)
            elif insertionChoice == 5:
                inertionnodedata = int(input("\tEnter New Node Data:\t"))
                linkListObject.listInsertion(5, inertionnodedata)
            else:
                print("")
                print("  Invalid Input  ".center(50,"-"))
        
        elif (userinput == 5):
            print("")
            print("   Deletion Operation on List   ".center(50,"-"))
            print("\t\t1. Delete a Node from Beginning\n\t\t2. Delete a Node from End\n\t\t3. Delete a Specific Node\n")
            deletionchoice = int(input("\t\tEnter Your Choice:\t"))
            if deletionchoice == 1:
                linkListObject.listDeletion(1)       
            elif deletionchoice == 2:
                linkListObject.listDeletion(2)    
            elif deletionchoice == 3:
                deletionchoicedata = int(input("\tEnter Node Data To Delete:\t"))
                linkListObject.listDeletion(3, deletionchoicedata)
            else:
                print("")
                print("  Invalid Input  ".center(50,"-"))
                
        
        elif (userinput == 6):
            searchitem = int(input("\t\tEnter Node Data for Searching:\t"))
            linkListObject.listSearch(searchitem)
        
        elif (userinput == 7):
            print("")
            print("   Sorting Operation on List   ".center(50,"-"))
            print("\t\t1. Merge Sort\n\t\t2. Bubble Sort by Exchanging Node Data\n\t\t3. Bubble Sort by Exchanging Node Links\n")
            sortchoice = int(input("\t\tEnter Your Choice:\t"))
            if sortchoice == 1:
                linkListObject.sortList(1)
            elif sortchoice == 2:
                linkListObject.sortList(2)
            elif sortchoice == 3:
                linkListObject.sortList(3)
            else:
                print("")
                print("  Invalid Input  ".center(50,"-"))
        
        elif (userinput == 8):
            print("")
            print("   Cycle In List Operations   ".center(50,"-"))
            print("\t\t1. Insert a Cycle\n\t\t2. Remove Cycle from List\n\t\t3. Detect a Cycle In List\n")
            cyclechoice = int(input("\t\tEnter Your Choice:\t"))
            if cyclechoice == 1:
                linkListObject.cycleInList(1)
            elif cyclechoice == 2:
                linkListObject.cycleInList(2)
            elif cyclechoice == 3:
                linkListObject.cycleInList(3)
            else:
                print("")
                print("  Invalid Input  ".center(50,"-"))
        
        elif (userinput == 9):
            linkListObject.reverseList()
        
        elif (userinput == 10):
            print("\t\tThanks For using Single Link List Data Structure\n\n")
            exit()
        
        else:
            print("")
            print("   Invalid Input. Try Again.   ".center(60,"-"))

#---------------------------------------------------------------- CODE ENDED -----------------------------------------------------------------------