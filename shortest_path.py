import heapq

# Define the grid size
GRID_SIZE = 4

# Define the possible moves: up, down, left, right
MOVES = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def is_valid(x, y, grid, avoid=[]):
    """Check if a given cell is valid (within the grid and not an obstacle or a point to avoid)."""
    return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE and grid[x][y] != -1 and (x, y) not in avoid

def dijkstra(grid, start, end, avoid=[]):
    distances = [[float('inf') for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    distances[start[0]][start[1]] = 0
    predecessors = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    pq = [(0, start)]

    while pq:
        current_distance, (x, y) = heapq.heappop(pq)

        if (x, y) == end:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = predecessors[x][y]
            path.append(start)
            
            path.reverse()
            return current_distance, path

        for dx, dy in MOVES:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, grid, avoid) and distances[new_x][new_y] == float('inf'):
                new_distance = current_distance + 1
                distances[new_x][new_y] = new_distance
                predecessors[new_x][new_y] = (x, y)
                heapq.heappush(pq, (new_distance, (new_x, new_y)))
        
   
    return float('inf'), []

def shortest_path(grid, start, point1, point2, point3):
    dist1, path1 = dijkstra(grid, start, point1, [point2, point3])
    print(f"Path 1 taken: {path1}")
    x = path1.pop(dist1)
    x2 = path1.pop(dist1-1)


   
    dist2, path2 = dijkstra(grid, x2, point2, [point1, point3,start])
   
    path1.append(x2)
    path1.append(x)


    print(f"Path 2 taken: {path2}")

    x = path2.pop(dist2)
    x2 = path2.pop(dist2-1)
   # x = path2.pop(dist2-2)
    dist3, path3 = dijkstra(grid, x2, point3, [start, point1, point2])

    


    print(f"Path 3 taken: {path3}")
    path2.append(x2)
    path2.append(x)

    x = path3.pop(dist3)
    x2 = path3.pop(dist3-1)
    #path2.append(x)
   # x = path3.pop(dist3-2)
    dist4, path4 = dijkstra(grid, x2, start, [point1, point2, point3])

    path3.append(x2)
    path3.append(x)
    print(f"Path 4 taken: {path4}")
   # path3.append(x)
   
    return path1,path2,path3,path4

# Example
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
start = (0, 0)
point1 = (0, 1)
point2 = (0, 2)
point3 = (0, 3)

path1,path2,path3,path4 = shortest_path(grid, start, point1, point2, point3)
print(f"Path 1 returned: {path1}")
print(f"Path 2 returned: {path2}")
print(f"Path 3 returned: {path3}")
print(f"Path 4 returned: {path4}")
#print(f"Shortest Distance: {distance}")
#print(f"Path taken: {path}")