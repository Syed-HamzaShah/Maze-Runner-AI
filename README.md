Escape The Maze

**Escape The Maze** is a Python-based pathfinding visualization project that demonstrates intelligent agent behavior in solving maze puzzles using various search and decision algorithms.

Overview

This project simulates an agent navigating through a maze using search algorithms and decision trees. It includes both static and animated visualizations to better understand the underlying logic of the AI's movements.

Project Structure

```
Escape The Maze/
├── agent.py                 # Agent logic and movement
├── maze.py                  # Maze creation and representation
├── search.py                # Search algorithms (e.g., BFS, DFS, A*)
├── decision_tree_model.py   # Decision tree model for maze solving
├── visualizer.py            # Static visualizer
├── animated_visualizer.py   # Animated visualizer using matplotlib
├── main.py                  # Main entry point of the application
└── .vs/                     # Visual Studio settings (can be ignored)
```

How to Run

Prerequisites

Make sure you have Python 3.7+ installed. Then install required libraries:

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, install these manually:

```bash
pip install matplotlib numpy
```

Running the Project

To start the maze simulation:

```bash
python main.py
```

This will generate and visualize a maze with the agent solving it.

Features

- Maze generation and solving
- AI agent using decision trees
- BFS, DFS, and possibly A* search
- Animated and static visualizations using `matplotlib`


To-Do

- Add A* search
- Improve UI/UX
- Add GUI using `tkinter` or `pygame`
- Support for custom mazes


License

This project is licensed under the MIT License — feel free to use and modify!

---

Created with ❤️ using Python.