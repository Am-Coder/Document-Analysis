import re
import os
import glob
from collections import defaultdict 
from itertools import combinations 

#Node structure for graph
class Node:

    def __init__(self,src,dest,wt):
        self.src = src
        self.dest = dest
        self.wt = wt


#Class to represent an un-directed graph using adjacency list representation 
class Graph: 
   
    def __init__(self,vertices): 
        self.V = vertices #No. of vertices 
        self.V_org = vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
        self.path = "C:/Users/Shubhi/Downloads/Krapivin2009/keys/*.key"
        self.dictKeywords = {}
        
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
    

#Class to calculate weight of the edges
class weightGenerator:
    
    def __init__(self,path): 
        self.path = path
        self.dictKeywords = {}
        self.nodesPair = []
        self.subsetSize = 2
        
    #function to extract list of keywords in all the research papers
    def extractDictOfKeywords(self):
        listFiles = glob.glob(self.path)
        self.dictKeywords = {int(os.path.splitext(os.path.basename(filename))[0]) : [keyword for keyword in re.split("\n", "".join(open(filename,"r+").readlines())) if keyword] for filename in listFiles}
        return self.dictKeywords
    
    #function to find combination pairs of 2 research papers at a time
    def rSubset(self, arr): 
        self.nodesPair = list(combinations(arr, self.subsetSize)) 
        return self.nodesPair
    
    #function to extract weight
    def pathWeight(self, x, y):
        s1 = set(x)
        s2 = set(y)
        return(len(s1.intersection(s2)))
        

        
# Driver Function 
if __name__ == "__main__": 
    path = "C:/Users/Shubhi/Downloads/Krapivin2009/keys/*.key"
    weightGen = weightGenerator(path)
    dictKeywords = weightGen.extractDictOfKeywords()
    keysList = dictKeywords.keys()
    nodesCount = len(keysList)
    nodesPair = weightGen.rSubset(keysList) 
    
    g = Graph(nodesCount) 
    for i in nodesPair:
        edgeWeight = weightGen.pathWeight(dictKeywords[i[0]],dictKeywords[i[1]])
        if edgeWeight>0:
            g.addEdge(i[0], i[1], edgeWeight)

    g.printGraph()