from maze import Maze
from agent import MazeBot

def main():
    maze = Maze(rows=10, cols=10)
    bot = MazeBot(maze)
    bot.run()

if __name__ == "__main__":
    main()