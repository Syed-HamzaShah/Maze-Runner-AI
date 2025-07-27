from queue import PriorityQueue

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {start: 0}

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        r, c = current
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 'X':
                temp_g = g_score[current] + 1
                if temp_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g
                    f_score = temp_g + heuristic(neighbor, goal)
                    open_set.put((f_score, neighbor))
    return None