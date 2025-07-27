from decision_tree_model import load_model
from search import a_star
import random

class MazeBot:
    def __init__(self, maze):
        self.maze = maze
        self.grid = maze.grid
        self.model = load_model()
        self.position = (0, 0)
        self.goal = (maze.rows - 1, maze.cols - 1)
        self.health = 100

    def sense_tile(self, pos):
        r, c = pos
        tile = self.grid[r][c]
        features = {
            'tile_type': 0 if tile == ' ' else 1,
            'enemy_type': 1 if tile == 'E' else 0,
            'noise_level': random.randint(0, 100),
            'light_level': random.randint(0, 100)
        }
        return features

    def predict_danger(self, features):
        df = [[features['tile_type'], features['enemy_type'], features['noise_level'], features['light_level']]]
        return self.model.predict(df)[0]

    def run(self):
        self.maze.display()
        print("\n🔍 Planning escape...\n")

        path = a_star(self.grid, self.position, self.goal)
        if not path:
            print("❌ No path found!")
            return

        for step in path:
            r, c = step
            tile = self.grid[r][c]
            features = self.sense_tile((r, c))
            danger = self.predict_danger(features)

            if danger == 1:
                print(f"⚠️ Danger detected at {step}. Avoiding if possible.")
                continue

            print(f"➡️ Moving to {step} - Tile: {tile}")
            self.position = step

            if tile == 'E':
                print("⚔️ Enemy encountered! Fighting...")
                self.health -= 30
                if self.health <= 0:
                    print("💀 MazeBot died.")
                    return

        print("🎉 MazeBot escaped successfully!")