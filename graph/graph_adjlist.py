from collections import deque

class Graph:
    def __init__(self) -> None:
        self.vertices={}
        
    def add_vertex(self,vertex):
        if vertex not in self.vertices:
            self.vertices[vertex]=[]

            
    def add_edges(self,vertex1,vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)

        else:
            raise ValueError("vertices not found in graph")
        
    def display(self):
        print(self.vertices)
        
    def bfs(self,start):
        visited=set()
        queue=deque([start])
        bfs_ord=[]
        while queue:
            vertex=queue.popleft()
            if vertex not in visited:
                bfs_ord.append(vertex)
                visited.add(vertex)
                for i in self.vertices[vertex]:
                    if i not in visited:
                        queue.append(i)
                        
        return bfs_ord

    
    def dfs(self,start,visites=None,dfs_ord=None):
        if visites is None:
            visites=set()
        if dfs_ord is None:
            dfs_ord=[]
        visites.add(start)
        dfs_ord.append(start)
        for nei in self.vertices[start]:
            if nei not in visites:
                self.dfs(nei,visites,dfs_ord)
        return dfs_ord        
        
        
gr=Graph()
gr.add_vertex('A')
gr.add_vertex('B')
gr.add_vertex('C')
gr.add_vertex('D')
gr.display()
gr.add_edges('A','B')
gr.add_edges('A','D')
gr.add_edges('C','B')
gr.add_edges('B','A')
gr.add_edges('B','D')
gr.add_edges('D','C')       

gr.display()
print(gr.bfs('B'))
print(gr.dfs('D'))