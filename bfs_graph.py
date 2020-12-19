from collections import defaultdict
class Graph :                           #Graph-BFS Traversal Implementation in Python 
    def __init__(self):
        self.graph = defaultdict(list)
       
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def bFS(self,s):
        
        visited = [False] *(max(self.graph)+1)
        
        queue = []
        
        queue.append(s)
        visited[s] = True
    
        while queue: 
            s = queue.pop(0)
            print(s,end = ' ')
            
            for i in self.graph[s] :
                
                if visited[i] == False:
                    visited[i] = True
                    queue.append(i)
                    
                    
graph = Graph()

graph.addEdge(0,1)
graph.addEdge(0,2)
graph.addEdge(1,2)
graph.addEdge(2,0)
graph.addEdge(2,3)
graph.addEdge(3,3)

graph.bFS(2)
                    
            
        
