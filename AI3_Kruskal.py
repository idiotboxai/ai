# Disjoint Set (Union-Find) Data Structure to keep track of connected components
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

# Kruskal's Algorithm to find MST
def kruskal(vertices, edges):
    mst = []
    total_weight = 0
    disjoint_set = DisjointSet(vertices)

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    for u, v, weight in edges:
        # If u and v are not in the same set, include this edge in the MST
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append((u, v, weight))
            total_weight += weight
    
    return mst, total_weight

def main():
    # Taking input from the user
    vertices = int(input("Enter the number of vertices: "))
    edges_count = int(input("Enter the number of edges: "))
    
    edges = []
    print("Enter each edge as (vertex1, vertex2, weight):")
    for _ in range(edges_count):
        u, v, weight = map(int, input().split())
        edges.append((u, v, weight))
    
    # Running Kruskal's algorithm
    mst, total_weight = kruskal(vertices, edges)

    # Display the result
    print("\nEdges in the MST:")
    for u, v, weight in mst:
        print(f"Edge ({u}, {v}) with weight {weight}")
    print(f"Total weight of the MST: {total_weight}")

# Calling the main function to execute the program
if __name__ == "__main__":
    main()



Enter the number of vertices: 6
Enter the number of edges: 9
Enter each edge as (vertex1, vertex2, weight):
0 1 4
0 2 4
1 2 2
1 0 4
2 3 3
2 5 2
2 4 4
3 4 3
5 4 3


(1, 2, 2)
(2, 5, 2)
(2, 3, 3)
(3, 4, 3)
(5, 4, 3)
(0, 1, 4)
(0, 2, 4)
(2, 4, 4)
(1, 0, 4)


(1, 2, 2)
(2, 5, 2)
(2, 3, 3)
(3, 4, 3)
(0, 1, 4)

