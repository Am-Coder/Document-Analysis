from collections import defaultdict 


#Node structure for graph
class Node:

    def __init__(self,src,dest,wt):
        self.src = src
        self.dest = dest
        self.wt = wt


#This class represents an un-directed graph using adjacency list representation 
class Graph: 
   
    def __init__(self,vertices): 
        self.V = vertices #No. of vertices 
        self.V_org = vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
   
    # function to add an edge to graph 
    def addEdge(self,u,v,w): 
        self.graph[u].append(Node(u,v,w))
        self.graph[v].append(Node(v,u,w))

    #function to print graph
    def printGraph(self):
        for i in self.graph:
            print(str(i) + " is connected to ")
            for node in self.graph[i]:
                print(str(node.dest) + "(Weight = " + str(node.wt) + ")" + " ")
            print("\n")

    
    def BFS(self, s, max_levels):
        visited = set()
 
        queue = []
 
        queue.append(s)
        visited.add(s)
        level = 0
        result = {}
        while queue:
            aux = []
            result[level] = []
            
            while queue:
                s = queue.pop(0)
                visited.add(s)
                result[level].append(s)
                for node in self.graph[s]:
                    if node.dest not in visited:
                        aux.append(node.dest)
                        visited.add(node.dest)
            level += 1
            if level > max_levels:
                break
            for node in aux:
                queue.append(node)
            
        return result            
                    
# Create a graph SAMPLE use 
g = Graph(4) 
g.addEdge(0, 1, 2) 
g.addEdge(0, 2, 2) 
g.addEdge(1, 2, 1) 
g.addEdge(1, 3, 1) 
g.addEdge(2, 3, 2) 
# g.printGraph()
print(g.BFS(3,3))

g = Graph(4) 
g.addEdge('a', 'b', 2) 
g.addEdge('a', 'c', 2) 
g.addEdge('b', 'c', 1) 
g.addEdge('b', 'd', 1) 
g.addEdge('c', 'd', 2) 
# g.printGraph()
print(g.BFS('d',3))
