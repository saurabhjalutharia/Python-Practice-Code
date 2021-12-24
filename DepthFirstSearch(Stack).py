import os
os.system("cls")
#---------------------------------------------------------- NODE STRUCTURE ----------------------------------------------------------------------------
class Node(object):
	def __init__(self, name):                          #NODE CONSTRUCTOR
		self.name = name                               #NODE NAME/DATA
		self.adjacenciesList = []                      #LIST CONTAIN ALL OTHER NODE ADJACENT TO OUR MAIN NODE/ROOT NODE
		self.visited = False                           #CHECK WHEATHER WE ALREADY VISITED THE NODE AND ITS ADJACANT NODES, DEFAULT FALSE

#-------------------------------------------- DEPTH FIRST SEARCH USING STACK DATA STRUCTURE -------------------------------------------------------------
class DepthFirstSearch(object): 
	def dfsFunction(self, node):                               #NODE FROM WHERE SEARH START/FIRST NODE
	    node.visited = True                            #MARK NODEAS VISITED
	    print(f"{node.name}")                          #PRINT NODE DATA
	    for n in node.adjacenciesList:                 #REPEAT TILL WE DONT VISIT ALL THE NODE ADJACENT TO OUR ROOT NODE
		    if not n.visited:                          #CHECK WHEATHER THE ADJACENT NODE ALREADY VISITEDOR NOT
			    self.dfsFunction(n)                    #RECURSIVE CALL ON FUNCTION DFS TILL WE VISIT ALL NODE
                                                       #IF VISITED TRUE BACKTRACK TO THE MAIN NODE AND START AGAIN ON DIFFERENT NODE                                    
#-------------------------------------------------------------------------------------------------------------------------------------------------

node1 = Node("A")                                      #                    A
node2 = Node("B")                                      #                   / \    
node3 = Node("C")                                      #                  B    C
node4 = Node("D")                                      #                 / 
node5 = Node("E")                                      #	            D 	
node6 = Node("F")                                      #	           / \
                                                       #              F   E        
node1.adjacenciesList.append(node2)
node1.adjacenciesList.append(node3)
node2.adjacenciesList.append(node4)
node4.adjacenciesList.append(node6)
node4.adjacenciesList.append(node5)	
#-------------------------------------------------------------------------------------------------------------------------------------------------	
dfsObject = DepthFirstSearch()
dfsObject.dfsFunction(node1)
#-------------------------------------------------------------------------------------------------------------------------------------------------