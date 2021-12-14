import os
os.system("cls")
#------------------------------------------ GLOBAL VARIABLES ------------------------------------------------
currentBooksList = ["c", "python", "ds", "networking", "toc", "os", "maths"]
booksIssueList = []
studentObjectList = []

#----------------------------------------------- CLASS STUDENT -----------------------------------------------
class Student(object):
    def __init__(self):
        self.studentOwnBookLst=[]       #LIST FOR EACH STUDENT WHO OWN LIBRARY BOOKS
        self.issued = False             #BOOK ISSUED SUCESSUFULLY OR NOT. DEFAULT NOT.
        
    def newStudent(self, name):         #NEW STUDENT OBJECT CREATE BY STUDENT NAME
        i=0
        con = True
        self.name = name
        while(con):
            try:
                booknum = int(input(f"{self.name.capitalize()} how many Book(s) you want to Issue: "))   #NO. OF BOOK A PARTICULAR STUDENT CAN ISSUE AT A TIME
                while(booknum > len(currentBooksList)):
                    print(f"You Can not Issue {booknum} Book(s). Currently Only {len(currentBooksList)} Book(s) Available in Library.")
                    booknum = int(input(f"{self.name.capitalize()} how many Book(s) you want to Issue: "))
                print("")
                while(i!=booknum):
                    while(self.issued == False):                                             #CHECK WHEATHE A BOOK ISSUED OR NOT
                        bookname = input(f"\tEnter Your {i+1} Book Name:\t").lower()
                        self.issued = librabryObject.bookAssign(bookname)                    #IF BOOK ISSUED SUCCESSFULLY EXIT INNER WHILE LOOP
                    i += 1
                    self.issued = False
                print(f"\tYour {booknum} Book(s) Assign. Please Return Book(s) in next 30 Days \n")
                con = False     #WHEN ISSUED BOOK EQUALs TO NUMBER OF BOOKS ENTERED BY USER, OUTER WHILE LOOP EXIT
            except:
                print("-----  Enter Valid Input  -----\n")

#-------------------------------------------- MAIN LIBRARY CLASS -------------------------------------------------------
class Librabry(Student):
    def __init__(self):
        super().__init__()

    @staticmethod       #NOT TAE ANY ARGUMENT
    def availableBookList():
        print("")
        print("   These are the Books Currently Present in the Library   ".center(50))
        for index, i in enumerate(currentBooksList):    
            print(f"{index+1}. {i.capitalize()}")       #PRINT BOOKS CURRENTLY AVAILABLE IN THE LIBRARY
        print("")

    def bookAssign(self, name):
        self.issuebookname = name                                   #BOOK NAME ASSIGNMENT
        if self.issuebookname not in self.studentOwnBookLst:        #WHEATER STUDENT ALREADY ISSUED THE BOOK OR NOT
            if self.issuebookname in currentBooksList:              #CHECK WHEATHER REQUESTED BOOK AVAILABLE OR NOT
                self.studentOwnBookLst.append(self.issuebookname)   #ADD ASSIGNED BOOK IN THE PARTICULAR STUDENT OWN LIST WHO ASSIGN IT
                booksIssueList.append(self.issuebookname)           #ADD ASSIGNED BOOK IN THE ISSUED BOOKED LIST
                currentBooksList.remove(self.issuebookname)         #REMOVE ASSIGNED BOOK FROM THE CURRENTLY AVAILABLE BOOK LIST
                return True                                         #FOR CONFIRMATION THAT YES BOOK HAS BEEN ASSIGN
            else:
                print("  Book Not Available.  ".center(50,"-"))
                print("\nThese Book(s) Currently Available: ", currentBooksList)
                print("")
                return False
        else:
            print("\tYou Already Issued This Book")
            return False
            
    def bookReturn(self, name):
        self.returnbookname = name
        if self.returnbookname in self.studentOwnBookLst:       #CHEKC WHEATHER STUDENT OWN THE BOOK OR NOT
            currentBooksList.append(self.returnbookname)        #ADD RETURNED BOOK IN THE CURRENTLY AVAILABLE BOOK
            self.studentOwnBookLst.remove(self.returnbookname)  #REMOVE BOOK FROM STUDENT OWN LIST
            print("   Thanks for Returning Book   ".center(40,"-"))
        else:
            print(f"\t Either You Did Not Issued this Book OR You Entered Wrong Name. You Entered: {self.returnbookname}\n")

    def addNewBook(self, addbookname):
        self.addbookname = addbookname
        if self.addbookname in currentBooksList:            #CHECK NEW BOOK ALREADY EXITS OR NOT
            print(f"{self.addbookname} Already Available".center(60,"-"))
        else:
            currentBooksList.append(self.addbookname)       #TO ADD A NEW BOOK IN THE RECORD.CURRENTLLY AVAILABLE LIST
            print("  Thanks for Adding New Book.  ".center(60,"-"))
            print("")

    def deleteBook(self, delbookname):
        self.delbookname = delbookname
        if self.delbookname not in currentBooksList:
            print(f"No Book by name ({self.delbookname.capitalize()}) in the Library\n")
        else:
            currentBooksList.remove(self.delbookname)       #REMOVE BOOK FROM THE LIBRARY
            print(f"Book {self.delbookname.capitalize()} Removed from the Library\n")

    def ownerDetails(self, name):       #DISPLAY WHICH STUDENT OWN HOW MANY LIBRARY BOOKS.
        self.studentname = name
        l = ", ".join(self.studentOwnBookLst)
        print(f"Book(s) Issued by {self.studentname.capitalize()} are: {len(self.studentOwnBookLst)}. Those Book(s) are: {l.capitalize()}")
        print("")   

    def __str__(self):                  #DISPLAY COMPLETE STATUS OF THE LIBRABY BOOKS, STUDENTS, OWNERSHIP
        totalIssuedBook = len(booksIssueList)
        currentbooks = len(currentBooksList)
        return f'''
        Currently ({currentbooks}) Books Available in the Libraby.
        Total ({len(studentObjectList)}) Students Issued ({totalIssuedBook}) Book(s) from Library.
        \n'''   

#----------------------------------------------- MAIN PROGRAM CODE ---------------------------------------------------------
librabryObject = Librabry()         #LIBRARY OBJECT AND  STUDENT OBJECT WILL CREATE AT RUN TIME DYNAMICALLY
if __name__ == "__main__":
    while(True):
        print("   Welcome to J's Library   ".center(60,"-"))
        print('''Choose Your Option:
            1. Available Books List
            2. Issue Book
            3. Return Book
            4. Add New Book
            5. Delete A Book
            6. Student Detail
            7. Library Status
            8. Exit\n''')

        userInput = int(input("Enter Your Choice:\t"))
        if userInput == 1:
            librabryObject.availableBookList()          #DISPLAY ALL CURRENTLY AVAILABLE BOOKS

        elif userInput == 2:
            stuname = student = input("Enter Student Name:\t").lower()
            stuname = Student()                     #NEW STUDENT OBJECT CREATED
            stuname.newStudent(student)
            studentObjectList.append(stuname)       #STUDENT OBJECT ADDED IN THE STUDENT OBJECT LIST
        
        elif userInput == 3:
            studetailreturn = input("Enter Returnee Name:\t").lower()
            for i in range(len(studentObjectList)):
                if studentObjectList[i].name == studetailreturn:        #CHECK WHEATHER STUDENT EXITS IN THE LIBRARY DATABASE OT NOT
                    retbookname = input("Enter Return Book Name:\t")
                    librabryObject.bookReturn(retbookname)
                else:
                    print(f"   {studetailreturn.capitalize()} You Did Not Isued any Book From this Library   ".center(60,"-"))
                    print("")

        elif userInput == 4:
            abookname = input("Enter New Book Name:\t").lower()
            librabryObject.addNewBook(abookname)            #TO ADD NEW BOOK IN THE LIBRARY

        elif userInput == 5:
            dbookname = input("Enter Book Name:\t").lower()
            librabryObject.deleteBook(dbookname)            #TO REMOVE A BOOK FROM THE LIBRARY

        elif userInput == 6:
            a = []
            for i in range(len(studentObjectList)):
                a.append(studentObjectList[i].name)         #DISPLAY ALL THE STUDENT NAMES THAT ARE IN THE LIBRARY DATABSE
            print("\n----- List of Students who Issued Books from Library -----")
            print(a)
            studetail = input("\nEnter Name of the Student:\t").lower()     #CHOICE FOR USER WHOSES DATA HE/SHE WHANTS TO SEE
          
            for i in range(len(studentObjectList)):
                if studentObjectList[i].name == studetail:  #LOCATE THAT STUDENT FROM THE LIST OF STUDENT DATABAE
                    librabryObject.ownerDetails(studetail)  #DISPLAY ALL THE BOOK OWN BY THAT STUDENT
                    break
                else:
                    print(f"No Student by name:  {studetail.capitalize()}\n")
        
        elif userInput == 7:
            print(librabryObject)       #DISPLAY LIBRABY CURRENT STATUS

        elif userInput == 8:
            print("   THANKS. Visit Again.   ".center(50,"-"))
            print("")
            exit()
        else:
            print("   Invalid Input. Try Again.   ".center(50))
            print("")
#--------------------------------------------------- END ----------------------------------------------------------------