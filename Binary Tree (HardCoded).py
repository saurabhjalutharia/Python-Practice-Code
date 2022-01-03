from collections import deque
import os
os.system("cls")
#---------------------------------------------------------------- CLASS FOR NODE STRUCTURE --------------------------------------------------------------------
class Node:
    def __init__(self, data):
        self.nodeData=data                                  #HOLD THE NODE DATA 
        self.leftChildLink=None                             #HOLD NODE LEFT CHILD LINK
        self.rightChildLink=None                            #HOLD NODE RIGHT CHILD LINK
        
#-------------------------------------------------- BINARY TREE CLASS FOR PRE, IN, POST AND LEVEL ORDER CODE ---------------------------------------------------           
class BinaryTree:
    def __init__(self):
        self.rootNode=None                                  #CONSTRUCTOR, EVERY NODE WILL HAVE A ROOT VALUE
        self.nodeIndex=None                                 #CONSTRUCTOR, EVERY NODE WILL HAVE AN INDEX VALUE  
      
    def preorder(self):
        self._preorder(self.rootNode)                       #CALLS PREORDER FUNCTION PRIVATELY
        print()
    def _preorder(self, rootnode):
        if rootnode == None:                                #NODE HAS NO ROOT VALUE, SINGLE NODE OR NODE ITSELF IS HE MAIN ROOT NODE OF THE TREE
            return  
        print(rootnode.nodeData, " ", end="")               #PRINT ROOT NODE DATA
        self._preorder(rootnode.leftChildLink)              #NODE CALL ITS OWN LEFT CHILD LINK RECURSIVELY TILL LEFT CHILD LINK EXHAUSTED
        self._preorder(rootnode.rightChildLink)             #NODE CALL ITS OWN RIGHT CHILD LINK RECURSIVELY TILL RIGHT CHILD LINK EXHAUSTED

    def inorder(self):                                      
        self._inorder(self.rootNode)                        #CALLS INODER FUNCTION PRIVATELY
        print() 
    def _inorder(self, rootnode):   
        if rootnode == None:    
            return  
        self._inorder(rootnode.leftChildLink)               #NODE CALL ITS OWN LEFT CHILD LINK RECURSIVELY TILL LEFT CHILD LINK EXHAUSTED
        print(rootnode.nodeData, " ", end="")               #PRINT ROOT NODE DATA
        self._inorder(rootnode.rightChildLink)              #NODE CALL ITS OWN RIGHT CHILD LINK RECURSIVELY TILL RIGHT CHILD LINK EXHAUSTED

    def postorder(self):                                    
        self._postorder(self.rootNode)                      #CALLS PREORDER FUNCTION PRIVATELY
        print()
    def _postorder(self, rootnode):
        if rootnode == None:
            return
        self._postorder(rootnode.leftChildLink)             #NODE CALL ITS OWN LEFT CHILD LINK RECURSIVELY TILL LEFT CHILD LINK EXHAUSTED
        self._postorder(rootnode.rightChildLink)            #NODE CALL ITS OWN RIGHT CHILD LINK RECURSIVELY TILL RIGHT CHILD LINK EXHAUSTED
        print(rootnode.nodeData, " ", end="")               #PRINT ROOT NODE DATA
    
    def levelorder(self):
        queeu = deque()                                     #IMPORT DEQUE MODULE AS A QUEEU
        queeu.append(self.rootNode)                         #ADD ALL ROOT NODE IN THE QUEEU
        while len(queeu)!= 0:
            pointer = queeu.popleft()                       #A POINTER WILL POINTS TO THE LEFT CHILD OF THE ROOT NODE
            print(pointer.nodeData, " ", end="")            #POINTER WILL PRINT NODE LEFT CHILD NODE DATA
            if pointer.leftChildLink:                       
                queeu.append(pointer.leftChildLink)         #IF POINTED LEFT CHILD NODE HAVE MORE LEFT NODE CHILD THEY WILL ADD IN THE QUEEUE RECURSIVELY
            if pointer.rightChildLink:
                queeu.append(pointer.rightChildLink)        #IF POINTED RIGHT CHILD NODE HAVE MORE RIGHT NODE CHILD THEY WILL ADD IN THE QUEEUE RECURSIVELY
    
    @property                                               #SETTER PROPERTY
    def height(self):
        return self._height(self.rootNode)                  #CALLS HEIGHT FUNCTION PRIVATELY
    def _height(self, root):
        if root == None:                                    #TREE IS EMPTY, NO NODE IN THE TREE
            return 0 
        return 1 + max(self._height(root.leftChildLink), self._height(root.rightChildLink))         
        #FIRST ROOT NODE CALL ITS LEFT CHILD RECURSIVELY TILL IT REACHES TO THE END OF ALL THE LEFT CHILD
        #THEN IT WILL CALL ITS RIGHT CHILD RECURSIVELY TILL IT REACHES TO THE END OF ALL THE LEFT CHILD 
        #THEN IT TAKES THE MAXIMUM OF THE TWO CHILD NODE HEIGHT AND ADD 1 TO IT (ITS OWN HEIGHT) AND RETURN MAX HEIGHT

    def create_tree(self):
        self.rootNode = Node("D")
        self.rootNode.leftChildLink = Node("B")
        self.rootNode.rightChildLink = Node("F")
        self.rootNode.leftChildLink.leftChildLink = Node("A")
        self.rootNode.leftChildLink.rightChildLink = Node("C")
        self.rootNode.rightChildLink.leftChildLink = Node("E")
        self.rootNode.rightChildLink.rightChildLink = Node("G")

binaryTreeObject = BinaryTree()
binaryTreeObject.create_tree()
print("")

print("   Pre-Order Traversal of the Binary Tree   ".center(50,"-"))
binaryTreeObject.preorder()
print("")
print("   In-Order Traversal of the Binary Tree   ".center(50,"-"))
binaryTreeObject.inorder()
print("")
print("   Post-Order Traversal of the Binary Tree   ".center(50,"-"))
binaryTreeObject.postorder()
print("")
print("   Level-Order Traversal of the Binary Tree   ".center(50,"-"))
binaryTreeObject.levelorder()

print("\n\nTree height is ")
print(binaryTreeObject.height)