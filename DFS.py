import os
os.system("cls")

initial_state="Initial"
visited_state="Visited"
finished_state="Finished"

class GraphNode(object):
    def __init__(self, name,state):
        self.name = name
        self.state =state
        self.children = []
        self.predecessor=None
        self.discoverytime=None
        self.finishingtime=None
        
        
    def display_node(self):
        print("Node: ",self.name)
        print("Adjacency List/Children \t",[i.name for i in self.children], end="")
        print("\n")
         
    def add_child(self,new_node):
        self.children.append(new_node)
    
    def remove_child(self,del_node):
        if del_node in self.children:
            self.children.remove(del_node)

class DiGraph(object):
    def __init__(self,node_list):
        self.nodes = node_list
        self.time=0
        
    def add_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            
    def add_edge_list(self,node1,nodelist):
        for i in nodelist:
            if(node1 in self.nodes and i in self.nodes):
                node1.add_child(i)

            
            
    def remove_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            
    def dfs(self,node_start):
        """ """
        qu=[]
        qu.append(node_start)
        
        while qu:
            v=qu.pop()
            print(v.name)
            v.state=visited_state
            for u in v.children:
                if u.state==initial_state:
                    qu.append(u)
                    u.predecessor=v
                    
    def dfs_all_recursive(self,node_start):
        """ This method calls dfs if some of the nodes are not reachable from source node"""
        self.time=0 
        
        for v in self.nodes:
            v.state=initial_state
        
        print("Calling bfs from node",node_start.name)  
        self.dfs_recursive(node_start)
        
        for v in self.nodes:
            if v.state==initial_state:
                print("Calling bfs from node",v.name)
                self.dfs_recursive(v)
                
        for v in self.nodes:
            print("Node ",v.name, "Discovery Time", v.discoverytime , "Finishing Time ", v.finishingtime)
            
    def dfs_recursive(self,v):
        """ """
        print("Node ",v.name , " visited")
       
        self.time+=1
        v.discoverytime=self.time
        
        for u in v.children:
            if u.state==initial_state:
                self.dfs_recursive(u)
                
        v.state=finished_state
        self.time+=1
        v.finishingtime=self.time
       

                    
    
    def dfs_all(self,node_start):
        """ This method calls dfs if some of the nodes are not reachable from source node"""
        for v in self.nodes:
            v.state=initial_state
        
        print("Calling bfs from node",node_start.name)  
        self.dfs(node_start)
        
        for v in self.nodes:
            if v.state==initial_state:
                print("Calling bfs from node",v.name)
                self.dfs(v)
                    
    def dfs_tree_edges(self,node_start):
        """ DFS Spanning Tree"""
        print("DFS Spanning tree edges")
        self.dfs_all(node_start)
        for v in self.nodes:
            if v.predecessor!=None:
                print("Tree Edge " ,v.predecessor.name , ">>", v.name )
node0 = GraphNode(0,initial_state)
node1 = GraphNode(1,initial_state)
node2 = GraphNode(2,initial_state)
node3 = GraphNode(3,initial_state)
node4 = GraphNode(4,initial_state)
node5 = GraphNode(5,initial_state)
node6 = GraphNode(6,initial_state)
node7 = GraphNode(7,initial_state)
node8 = GraphNode(8,initial_state)
node9 = GraphNode(9,initial_state)
node10 = GraphNode(10,initial_state)
node11 = GraphNode(11,initial_state)

Vertex_list3=[node0,node1,node2,node3,node4,node5,node6,node7,node8,node9,node10,node11]

graph3 = DiGraph(Vertex_list3) 

graph3.add_edge_list(node0,[node1,node3])
graph3.add_edge_list(node1,[node2,node5,node4])
graph3.add_edge_list(node2,[node5,node7])
graph3.add_edge_list(node3,[node6])
graph3.add_edge_list(node4,[node3])
graph3.add_edge_list(node5,[node3,node6,node8])
graph3.add_edge_list(node7,[node8,node10])
graph3.add_edge_list(node8,[node11])
graph3.add_edge_list(node9,[node6])
graph3.add_edge_list(node11,[node9])


for i in Vertex_list3:
    i.display_node()
print("Demo of depth first traversal")
graph3.dfs(node0)
graph3.dfs_all(node2)
graph3.dfs_tree_edges(node0)
graph3.dfs_all_recursive(node0)
graph3.dfs_all_recursive(node4)