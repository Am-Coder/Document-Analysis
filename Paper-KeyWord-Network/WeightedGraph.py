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
        visited = [False] * (self.V + 1)
 
        queue = []
 
        queue.append(s)
        visited[s] = True
        level = 0
        result = {}
        while queue:
            aux = []
            result[level] = []
            
            while queue:
                s = queue.pop(0)
                visited[s] = True
                result[level].append(s)
                for node in self.graph[s]:
                    if visited[node.dest] == False:
                        aux.append(node.dest)
                        visited[node.dest] = True
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
