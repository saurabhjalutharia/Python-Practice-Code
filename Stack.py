class stack():
    def __init__(self, maxstacksize = 10):
        self.maxstacksize = maxstacksize
        self.itemList = [None] * self.maxstacksize
        self.itemcounter = 0
    
    def isfull(self):
        if self.itemcounter == self.maxstacksize:
            print("")
            print("\t\tStack Is Full")
            return True
            
    def isempty(self):
        if self.itemcounter == 0:
            print("")
            print("\t\tStack Is Empty")
            return True
    
    def add(self, item):
        if self.isfull():
            pass
        else:
            #self.newitem = item
            #self.itemList.append(item)
            self.itemList[self.itemcounter] = item
            self.itemcounter += 1
            print("\tItem Added Successfully in the Stack")
        
    def remove(self):
        if self.isempty():
            pass
        else:
            temp = self.itemList[self.itemcounter-1]
            self.itemList[self.itemcounter-1] = None
            self.itemcounter -= 1
            print(f"\tRemoved item from the Stack. Item was: {temp}")
    
    def peek(self):
        if self.isempty():
            pass
        else:
            print(f"\tCurrently Top most item in the Stack is: {self.itemList[self.itemcounter-1]}")
    
    def displaystack(self):
        a = []
        self.stacksize()
        print("   All Stack items   ".center(50,"-"))
        for i in range(len(self.itemList)):
            a.append(str(self.itemList[i]))
        print(" --> ".join(a))
    
    def stacksize(self):
        print(f"\tCurrently size of the Stack is: {self.itemcounter}\n")

if __name__ == "__main__":
    stackObject = stack()
    while(True):
        print('''
        --------Welcom in Stack Data Stracture--------
            1. Display Stack
            2. Add New Item
            3. Remove Item
            4. Peek Item
            5. Quit\n''')
        userans =int(input("Enter Your Choice:\t"))
        
        if (userans == 1):
            stackObject.displaystack()
        elif (userans == 2):
            usernewitem = int(input("\tEnter New Item:\t"))
            stackObject.add(usernewitem)
        elif (userans == 3):
            stackObject.remove()
        elif (userans == 4):
            stackObject.peek()
        elif (userans == 5):
            print("Quiting Stack Data Structure\n")
            exit()
        else:
            print("   Invalid Input. Try Again.   ".center(60,"-"))
            print("")