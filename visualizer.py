import pygame
from maze import Maze
from agent import MazeBot
from decision_tree_model import load_model
from search import a_star
import random

# Constants
TILE_SIZE = 50
GRID_WIDTH = 10
GRID_HEIGHT = 10
WINDOW_WIDTH = TILE_SIZE * GRID_WIDTH
WINDOW_HEIGHT = TILE_SIZE * GRID_HEIGHT

# Colors
COLORS = {
    "empty": (255, 255, 255),
    "wall": (100, 100, 100),
    "enemy": (255, 0, 0),
    "start": (0, 255, 0),
    "goal": (0, 0, 255),
    "path": (200, 200, 0),
    "danger": (255, 165, 0)
}

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Escape the Maze AI")

def draw_grid(maze, path=[], dangers=[]):
    for r in range(GRID_HEIGHT):
        for c in range(GRID_WIDTH):
            rect = pygame.Rect(c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            tile = maze.grid[r][c]
            if (r, c) in path:
                color = COLORS["path"]
            elif (r, c) in dangers:
                color = COLORS["danger"]
            elif tile == "X":
                color = COLORS["wall"]
            elif tile == "E":
                color = COLORS["enemy"]
            elif tile == "S":
                color = COLORS["start"]
            elif tile == "G":
                color = COLORS["goal"]
            else:
                color = COLORS["empty"]
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

def main():
    maze = Maze(GRID_HEIGHT, GRID_WIDTH)
    bot = MazeBot(maze)
    path = a_star(maze.grid, bot.position, bot.goal)
    dangers = []

    if path:
        for step in path:
            features = bot.sense_tile(step)
            danger = bot.predict_danger(features)
            if danger == 1:
                dangers.append(step)

    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_grid(maze, path=path, dangers=dangers)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()