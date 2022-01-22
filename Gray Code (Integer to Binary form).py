import os
os.system("cls")
#----------------------------------------------------------------------------------------------------------------------------------------------------
class Solution():
    def grayCode(self, inputNumber):
        if (inputNumber <= 0):                          #BASE CONDITION
            return
        finalList = list()                              #THIS LIST WILL STORE ALL THE GENERATED CODES
        finalList.append("0")                           #START WITH ONE BIT PATTERN
        finalList.append("1")
        i = 2
        j = 0

        while(True):                                    #EVERY ITERATION OF THIS LOOP GENERATES 2*i CODES FROM PREVIOUSY GENERATED i CODES
            if i >= 1 << inputNumber:
                break
            for j in range(i - 1, -1, -1):
                finalList.append(finalList[j])          #ADD THE OREVIOUSLY GENERATED CODES
            for j in range(i):                          #ADD 0 TO THE FIRST HALF
                finalList[j] = "0" + finalList[j]       #ADD IN THE FINAL LIST IN REVERSE ORDER
            for j in range(i, 2 * i):                   #ADD 1 TO THE SECOND HALF
                finalList[j] = "1" + finalList[j]       #FINAL NUMBER OF LIST HAS DOUBLE NUMBER OF CODES
            i = i << 1
        for i in range(len(finalList)):
            print(finalList[i])                         #PRINT THE CONTENTS OF THE FINAL LIST

#-------------------------------------------------------------------------------------------------------------------------------------------------
query = 2
object1 = Solution()
print(object1.grayCode(query))
#----------------------------------------------------------------------------------------------------------------------------------------------------