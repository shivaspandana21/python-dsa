class Graph:
    def __init__(self,vertices):
        self.vertices = vertices

        self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.list = [[] for _ in range(vertices)]


    def add_edge(self,s,d):
        self.matrix[s][d] = 1
        self.matrix[d][s] = 1

    def add_elements(self,s,d):
        self.list[s].append(d)
        self.list[d].append(s)
    
    def bfs(self,node):
        visited = [False]*self.vertices     # marking for visited or not

        queue = []      # for acquiring current node and its neighbours 

        visited[node] = True

        queue.append(node)

        while queue:
            current = queue.pop(0)
            print(current,end=" ")

            for n in self.list[current]:
                if  not visited[n]:
                    visited[n] = True       # marking neighbour as visited
                    queue.append(n)         # add neighbour in queue


    # in this function we will be using an "UTILITY FUNCTION" which is a helper function which performs a specific task here it is performing recursion.
    
    def dfs(self,node):
        visited = [False]*self.vertices

        print("\nDFS :- ", end=" ")

        self.dfsUtil(node,visited)
        


    def dfsUtil(self,node,visited):
        visited[node] = True

        print(node,end=" ")
        # visit all adjacent vertices
        for n in self.list[node]:
            if not visited[n]:
                self.dfsUtil(n,visited)     # visiting neighbours recursively

        



    def display(self):
        for row in self.matrix:
            print(row)
        print()

        for row in range(self.vertices):
            print(f"{row} -> {self.list[row]}")

g = Graph(6)

# g.add_edge(0,1)
# g.add_edge(1,2)
# g.add_edge(1,3)
# g.add_edge(2,4)
# g.add_edge(4,1)

g.add_elements(0,3)
g.add_elements(3,1)
g.add_elements(3,4)
g.add_elements(4,1)
g.add_elements(1,2)
g.add_elements(4,5)
g.display()

g.bfs(0)
g.dfs(0)