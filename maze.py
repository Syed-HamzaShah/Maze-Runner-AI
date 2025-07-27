import random

class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = self.generate_maze()

    def generate_maze(self):
        maze = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                if random.random() < 0.15:
                    maze[r][c] = 'X'  # Obstacle
                elif random.random() < 0.1:
                    maze[r][c] = 'E'  # Enemy
        maze[0][0] = 'S'
        maze[self.rows - 1][self.cols - 1] = 'G'
        return maze

    def display(self):
        for row in self.grid:
            print(" ".join(row))