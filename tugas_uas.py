import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if neighbor in grid and grid[neighbor] == 0:
                new_g_score = g_score[current] + 1
                if neighbor not in g_score or new_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = new_g_score
                    heapq.heappush(open_set, (new_g_score + heuristic(neighbor, goal), neighbor))
    return None

car_brand = input("Masukkan brand mobil yg kamu sukail: ")
print(f"Mobil {car_brand} ,sabar beliau sedang berada di jalur balap")

size = 5
grid = {(x, y): 0 for x in range(size) for y in range(size)}
grid[(2, 2)] = 1  # Obstacle

start, goal = (0, 0), (4, 4)
path = astar(grid, start, goal)

if path:
    print(f"Jalur tercepat untuk {car_brand}: {path}")
else:
    print(f"Tidak ada jalur tersedia untuk {car_brand}!")