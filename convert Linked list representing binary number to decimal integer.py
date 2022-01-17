import os
os.system("cls")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
class ListNode:
    def __init__(self, data = 0, next = None):
      self.val = data                               #NODE DATA DEFAULT '0'
      self.nextLink = next                          #NODE NEXT LINK DEFAULT NONE
#------------------------------------------------------------------------------------------------------------------------------------------------------------
def create_list(elements):                          #FUNCTION THAT WILL CREATE THE LIST
    head = ListNode(elements[0])                    #HEAD CONTAIN THE FIRST ELEMENT OF THE LIST
    for element in elements[1:]:                    #LOOP TILL WE REACH THE END OF THE LIST
        pointer = head                              #A NEW POINTER POINTS TO THE HEAD AND TRAVERSE THE LIST
        while pointer.nextLink:                     #POINTER REACH TO THE LAST NODE
            pointer = pointer.nextLink
        pointer.nextLink = ListNode(element)        #ADD NEW NODE ELEMENT AT THE LAST OF THE LIST
    return head
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
   def binaryToDecimal(self, node):
        nodeList = []                               #EMPTY NODE LIST
        while node:
            nodeList.append(node.val)               #ADD NODE DATA INTO THE NODE LIST
            node = node.nextLink                    #MOVE TO THE NEXT NODE
        k = 0
        value = 0
        for i in range(len(nodeList)-1,-1,-1):
            if (nodeList[i] == 1):                  #CONSIDERING ONLY '1' VALUE BECAUSE IN BINARY '0' NOT CONTRIBUTE
                value += (2**k)                     #CONVERTING BINARY VALUE INTO INTEGER VALUE
            k += 1                                  #K REPRESENT TO 2's POWER
        return value
#------------------------------------------------------------------------------------------------------------------------------------------------------------
object1 = Solution()
head = create_list([1,0,1,1])
print(object1.binaryToDecimal(head))