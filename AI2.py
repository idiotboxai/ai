import heapq

# Directions: Up, Down, Left, Right
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Function to calculate Manhattan Distance
def manhattan_distance(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

# A* Algorithm Implementation
def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = []  # Priority queue to store nodes to be explored
    heapq.heappush(open_list, (0 + manhattan_distance(start, goal), 0, start))  # (f, g, (x, y))
    
    g_cost = {}  # Dictionary to store g-values (cost from start)
    g_cost[start] = 0
    
    came_from = {}  # To reconstruct the path
    
    while open_list:
        f, g, current = heapq.heappop(open_list)
        
        # If we reached the goal, reconstruct the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()  # To show the path from start to goal
            return path
        
        # Explore the neighbors
        for direction in DIRECTIONS:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            
            # Check if the neighbor is within bounds and not an obstacle
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                new_g = g + 1  # Each move has a cost of 1
                
                if neighbor not in g_cost or new_g < g_cost[neighbor]:
                    g_cost[neighbor] = new_g
                    f = new_g + manhattan_distance(neighbor, goal)
                    heapq.heappush(open_list, (f, new_g, neighbor))
                    came_from[neighbor] = current
    
    return None  # If no path is found

# Function to take user input
def get_user_input():
    # Get grid size
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    # Initialize the grid
    grid = []
    print("Enter the grid values (0 for open path, 1 for obstacle):")
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        grid.append(row)
    
    # Get start and goal positions
    start = tuple(map(int, input("Enter start position (row col): ").split()))
    goal = tuple(map(int, input("Enter goal position (row col): ").split()))
    
    return grid, start, goal

# Main function to execute A* algorithm with user input
def main():
    grid, start, goal = get_user_input()

    # Run A* algorithm to find the path
    path = a_star(grid, start, goal)
    
    # Print the result
    if path:
        print("Path found:", path)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()


o/p

Enter number of rows: 5
Enter number of columns: 5
Enter the grid values (0 for open path, 1 for obstacle):
Row 1: 0 0 0 0 0
Row 2: 1 1 1 1 0
Row 3: 0 0 0 1 0
Row 4: 0 1 0 0 0
Row 5: 0 1 0 1 0
Enter start position (row col): 0 0
Enter goal position (row col): 4 4


S 0 0 0 0
1 1 1 1 0
0 0 0 1 0
0 1 0 0 0
0 1 0 1 G


Path found: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (3, 3), (3, 2), (2, 2), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]


