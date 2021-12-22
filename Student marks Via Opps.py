import os
os.system("cls")
#--------------------------------------------------------------------------------------------------------------------------------------------------
studentNameListObj=[]                               #TO CONTAIN STUDENT OBJECTS
lists = []                                          #FOR STORING THE MAX SUM AMOUNG ALL THE STUDENT
subjectList = ["Physics", "Chemistry", "Maths"]

#------------------------------------------------------ CALSS DEFINATION -------------------------------------------------------------------------
class Data(object):
    def __init__(self):
        self.sujectMarkList = []                    #EACH STUDENT OBJECT MARKS ADD IN THIS LIST
        self.totalMarks = None                      #FILL BY THE SUM OF EACH STUDENT's OBJECT SUBJECT MARKS LIST
    def name(self, name):
        self.name = name                            #ASSIGN NAME TO THE OBJECT WHICH WAS ENTERED BY USER
    def printData(self):
        sums = sum(self.sujectMarkList)
        print(f"{self.name} Marks are: {self.sujectMarkList} in PCM Respectively and Total Sum is: {sums} with Average {sums/3}\n")
    def heighestSum(self):
        self.totalMarks = sum(self.sujectMarkList)
        lists.append(self.totalMarks)
    @staticmethod
    def ranker():    
        MaxMarks = max(lists)
        for i in range(len(studentNameListObj)):
            if(studentNameListObj[i].totalMarks==MaxMarks):
                print(f"   {studentNameListObj[i].name} is the I'st RANKER   ".center(50,"-"))

#--------------------------------------------- CREATING STUDENT OBJECT AND MARKS DATABSE -----------------------------------------------------            
totalstudent = int(input("Enter Total No. of Students in the Class:\t"))
for i in range(totalstudent):
    print(f"\nEnter {i+1} Student Name:\t", end="")
    studentName = studentNameobj = input("")                                #USER ENTER STUDENT NAME
    studentNameobj = Data()                                                 #OBJECT INITIATE WITH THE STUDENT NAME
    studentNameListObj.append(studentNameobj)                               #OBJECT ADD IN THE LIST OF STUDENT OBJECT
    studentNameListObj[i].name(studentName)                                 #INITIATED OBJECT ASSIGN THE NAME ENTERED BY THE USER
    for j in range(len(subjectList)):                                       #ITERATE AMOUNG ALL SUBJECT IN THE LIST SUBJECT
        print(f"\tEnter {studentNameListObj[i].name} {subjectList[j]} Marks:  ", end="")        #NAME AND EACH SUBJECT ITERATIVELY PRINT
        studentNameListObj[i].sujectMarkList.append(int(input("")))         #EACH STUDENT OBJECT MARKS LIST WILL BE FILLED BY MARKS VIA USER
print("")
for i in range(len(studentNameListObj)):
    studentNameListObj[i].printData()                                       #PRINTT THE DETAILS OF THE STUDENTS ALONG THEIR MARKS AND AVERAGE
print("")
for i in range(len(studentNameListObj)):
    studentNameListObj[i].heighestSum()                                     #WILL CREATE THE MAX LIST WHO HAS THE HEIGHEST MARKS AMOUNG ALL THE STUDENTS
print(Data.ranker())                                                        #PRINT THE RANKER NAME
#-------------------------------------------------- CODE ENDED -------------------------------------------------------------------------------