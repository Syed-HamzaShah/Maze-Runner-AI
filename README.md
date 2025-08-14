# Escape The Maze

**Escape The Maze** is a Python project that demonstrates intelligent agent behavior in solving randomly generated maze puzzles using search algorithms and decision trees. The project includes both static and animated visualizations to help you understand the AI's logic and pathfinding process.

---

## Features

- **Maze Generation:** Randomly generates mazes with obstacles and enemies.
- **AI Agent:** Uses a decision tree to predict danger and A\* search for pathfinding.
- **Visualization:**
  - Static visualization with Pygame.
  - Animated visualization showing the agent's movement and decisions.
- **Customizable:** Easily adjust maze size and agent logic.

---

## Project Structure

```
Escape-The-Maze/
├── agent.py                 # Agent logic and movement
├── maze.py                  # Maze creation and representation
├── search.py                # Search algorithms (A*)
├── decision_tree_model.py   # Decision tree model for danger prediction
├── visualizer.py            # Static visualizer (Pygame)
├── animated_visualizer.py   # Animated visualizer (Pygame)
├── main.py                  # Main entry point
├── data/
│   └── danger_data.csv      # Training data for decision tree
├── models/
│   └── decision_tree.pkl    # Saved decision tree model
└── requirements.txt         # Python dependencies
```

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/Escape-The-Maze.git
   cd Escape-The-Maze
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   If `requirements.txt` is missing, install manually:
   ```bash
   pip install pygame scikit-learn pandas matplotlib numpy
   ```

---

## Usage

### 1. Train the Decision Tree Model

Before running the maze, ensure the decision tree model is trained:

```bash
python decision_tree_model.py
```

### 2. Run the Main Simulation

```bash
python main.py
```

### 3. Visualize the Maze

- **Static Visualization:**
  ```bash
  python visualizer.py
  ```
- **Animated Visualization:**
  ```bash
  python animated_visualizer.py
  ```

---

## Customization

- **Maze Size:** Change `rows` and `cols` in `main.py`, `visualizer.py`, or `animated_visualizer.py`.
- **Agent Logic:** Modify `agent.py` to experiment with different AI behaviors.

---

## To-Do

- Add more search algorithms (BFS, DFS)
- Improve UI/UX
- Add GUI options (Tkinter, Pygame menus)
- Support for custom maze input

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Credits

Created with ❤️ by Hamza.
