# Graph with the implementaion of Adj Matrix
class Graph:
    def __init__(self,size):
        self.adj_matrix = [[0]*size for i in range(size)]
        self.size = size
        self.vertex_data = ['']*size

    def add_edge(self,u,v):
        if 0<= u <self.size and 0<= v < self.size:
            self.adj_matrix[u][v] = 1
            # self.adj_matrix[v][u] = 1

    def remove_edge(self,u,v):
        pass

    def add_vertex(self,vertex,data):
        if 0 <= vertex <= self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix")
        for row in self.adj_matrix:
            print(" ".join(map(str,row)))
        for vertex,data in enumerate(self.vertex_data):
            print(f"vertex{vertex} : {data}")





g = Graph(7)

g.add_vertex(0, 'A')
g.add_vertex(1, 'B')
g.add_vertex(2, 'C')
g.add_vertex(3, 'D')
g.add_vertex(4, 'E')
g.add_vertex(5, 'F')
g.add_vertex(6, 'G')

g.add_edge(3, 0)  # D -> A
g.add_edge(3, 4)  # D -> E
g.add_edge(4, 0)  # E -> A
g.add_edge(0, 2)  # A -> C
g.add_edge(2, 5)  # C -> F
g.add_edge(2, 6)  # C -> G
g.add_edge(5, 1)  # F -> B
g.add_edge(1, 2)  # B -> C

g.print_graph()