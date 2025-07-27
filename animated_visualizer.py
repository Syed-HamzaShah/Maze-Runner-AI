import pygame
import time
from maze import Maze
from agent import MazeBot
from decision_tree_model import load_model
from search import a_star
import random
import math

# Constants
TILE_SIZE = 50
GRID_WIDTH = 10
GRID_HEIGHT = 10
WINDOW_WIDTH = TILE_SIZE * GRID_WIDTH
WINDOW_HEIGHT = TILE_SIZE * GRID_HEIGHT
HUD_HEIGHT = 70

# Colors
COLORS = {
    "empty": (245, 245, 245),
    "wall": (60, 60, 60),
    "enemy": (200, 50, 50),
    "start": (50, 205, 50),
    "goal": (65, 105, 225),
    "danger": (255, 140, 0),
    "visited": (210, 230, 255),
    "line": (100, 149, 237)  # dotted path line
}

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT + HUD_HEIGHT))
pygame.display.set_caption("Escape the Maze AI - Animated")
font = pygame.font.SysFont("consolas", 22)
emoji_font = pygame.font.SysFont("Segoe UI Emoji", 28)  # For robot emoji 🤖

def draw_dotted_line(start, end, color, radius=4, gap=10):
    """Draws a dotted line between two grid cells"""
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    dist = math.hypot(dx, dy)
    dots = int(dist // gap)
    for i in range(dots):
        t = i / dots
        x = start[0] + t * dx
        y = start[1] + t * dy
        pygame.draw.circle(screen, color, (int(x), int(y)), radius)

def draw_grid(maze, path=[], dangers=[], bot_pos=None, message="", visited=set(), health=100, steps=0):
    screen.fill((20, 20, 20))
    
    # Background checker pattern
    for r in range(GRID_HEIGHT):
        for c in range(GRID_WIDTH):
            color = (30, 30, 30) if (r + c) % 2 == 0 else (40, 40, 40)
            pygame.draw.rect(screen, color, pygame.Rect(c*TILE_SIZE, r*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Draw path as dotted line
    for i in range(len(path)-1):
        x1, y1 = path[i][1]*TILE_SIZE + TILE_SIZE//2, path[i][0]*TILE_SIZE + TILE_SIZE//2
        x2, y2 = path[i+1][1]*TILE_SIZE + TILE_SIZE//2, path[i+1][0]*TILE_SIZE + TILE_SIZE//2
        draw_dotted_line((x1, y1), (x2, y2), COLORS["line"], radius=3)

    # Draw tiles
    for r in range(GRID_HEIGHT):
        for c in range(GRID_WIDTH):
            tile = maze.grid[r][c]
            pos = (r, c)
            rect = pygame.Rect(c * TILE_SIZE + 2, r * TILE_SIZE + 2, TILE_SIZE - 4, TILE_SIZE - 4)

            if pos == bot_pos:
                continue  # Will draw robot later
            elif pos in dangers:
                color = COLORS["danger"]
            elif tile == "X":
                color = COLORS["wall"]
            elif tile == "E":
                color = COLORS["enemy"]
            elif tile == "S":
                color = COLORS["start"]
            elif tile == "G":
                color = COLORS["goal"]
            elif pos in visited:
                color = COLORS["visited"]
            else:
                color = COLORS["empty"]

            pygame.draw.rect(screen, color, rect, border_radius=6)

    # Draw robot (emoji)
    if bot_pos:
        r, c = bot_pos
        emoji = emoji_font.render("🤖", True, (255, 255, 255))
        emoji_rect = emoji.get_rect(center=(c * TILE_SIZE + TILE_SIZE // 2, r * TILE_SIZE + TILE_SIZE // 2))
        screen.blit(emoji, emoji_rect)

    # HUD
    pygame.draw.rect(screen, (35, 35, 35), (0, WINDOW_HEIGHT, WINDOW_WIDTH, HUD_HEIGHT))
    msg_text = font.render(message, True, (255, 255, 255))
    screen.blit(msg_text, (10, WINDOW_HEIGHT + 10))

    # Health bar
    pygame.draw.rect(screen, (100, 100, 100), (10, WINDOW_HEIGHT + 40, 150, 20), border_radius=4)
    health_color = (0, 255, 0) if health > 50 else (255, 165, 0) if health > 20 else (255, 0, 0)
    pygame.draw.rect(screen, health_color, (10, WINDOW_HEIGHT + 40, max(0, health * 1.5), 20), border_radius=4)

    # Step count
    step_text = font.render(f"Steps: {steps}", True, (200, 200, 200))
    screen.blit(step_text, (180, WINDOW_HEIGHT + 40))

    pygame.display.flip()

def main():
    maze = Maze(GRID_HEIGHT, GRID_WIDTH)
    bot = MazeBot(maze)
    path = a_star(maze.grid, bot.position, bot.goal)
    dangers = []
    visited = set()
    steps = 0

    if not path:
        draw_grid(maze, [], [], None, "No path found.")
        time.sleep(3)
        return

    for step in path:
        features = bot.sense_tile(step)
        danger = bot.predict_danger(features)
        if danger == 1:
            dangers.append(step)

    for step in path:
        r, c = step
        tile = maze.grid[r][c]
        features = bot.sense_tile((r, c))
        danger = bot.predict_danger(features)

        visited.add(bot.position)
        steps += 1

        if danger == 1:
            message = f"Danger at {step}! Avoiding..."
            draw_grid(maze, path, dangers, bot.position, message, visited, bot.health, steps)
            time.sleep(0.8)
            continue

        bot.position = step

        if tile == "E":
            bot.health -= 30
            message = f"Fighting at {step} - Health: {bot.health}"
            if bot.health <= 0:
                draw_grid(maze, path, dangers, bot.position, "Bot died.", visited, bot.health, steps)
                time.sleep(3)
                return
        else:
            message = f"Moved to {step} - Tile: {tile}"

        draw_grid(maze, path, dangers, bot.position, message, visited, bot.health, steps)
        time.sleep(0.5)

    draw_grid(maze, path, dangers, bot.position, "MazeBot escaped successfully!", visited, bot.health, steps)
    time.sleep(3)

if __name__ == "__main__":
    main()
