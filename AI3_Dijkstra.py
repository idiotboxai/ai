import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))  # Comment this line for directed graph

    def dijkstra(self, start):
        dist = {}
        for node in self.graph:
            dist[node] = float('inf')
        dist[start] = 0

        pq = [(0, start)]
        while pq:
            current_dist, current_vertex = heapq.heappop(pq)

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_dist + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        for vertex in sorted(dist):
            print(f"Distance from {start} to {vertex} is {dist[vertex]}")

g = Graph()
n = int(input("Enter number of edges: "))
for _ in range(n):
    u, v, w = map(int, input("Enter edge with weight (u v w): ").split())
    g.add_edge(u, v, w)

start_node = int(input("Enter starting node: "))
print("Shortest distances using Dijkstra's Algorithm:")
g.dijkstra(start_node)


o/p

Enter number of edges: 4
Enter edge with weight (u v w): 0 1 4
Enter edge with weight (u v w): 0 2 1
Enter edge with weight (u v w): 2 1 2
Enter edge with weight (u v w): 1 3 1
Enter starting node: 0



Shortest distances using Dijkstra's Algorithm:
Distance from 0 to 0 is 0
Distance from 0 to 1 is 3
Distance from 0 to 2 is 1
Distance from 0 to 3 is 4

