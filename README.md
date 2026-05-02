## Overview
 
Traditional DSA learning relies on static diagrams and textbook explanations, making it hard to intuitively grasp how algorithms actually execute. This platform solves that by providing step-by-step visual animations, pseudocode walkthroughs, and a level-based interactive experience — turning abstract concepts into something you can see and interact with in real time.
 
---
 
## Features
 
- **Algorithm Visualizations** — Watch sorting, searching, tree operations, and graph traversals animate step by step
- **Level-Based Learning** — Progress through structured challenges across difficulty levels
- **Interactive Problem Solving** — Participate actively rather than passively reading theory
- **Real-Time Execution** — Recursive calls, backtracking steps, and graph traversals displayed dynamically
- **Hashing Module** — Visual demonstration of collision handling via chaining and open addressing
---
 
## Algorithm Design Techniques Covered
 
| Technique | Algorithms |
|---|---|
| Divide and Conquer | Binary Search, Merge Sort, Quick Sort |
| Greedy Method | Fractional Knapsack, Prim's, Kruskal's |
| Dynamic Programming | Multistage Graph |
| Backtracking | N-Queens Problem (Eight Queens) |
| Branch and Bound | Travelling Salesman Problem (TSP) |
| Hashing | Chaining, Open Addressing |
 
---
 
## Data Structures Covered
 
- **Linear:** Stack, Queue
- **Trees:** Binary Tree, BST, AVL Tree, Red-Black Tree, Min/Max Heap, M-Way Tree, B-Tree
- **Graphs:** General Graph traversal and visualization
---
 
## Tech Stack
 
| Layer | Technology |
|---|---|
| Backend | Python (Flask) |
| Frontend | HTML, CSS, JavaScript |
| Templating | Jinja2 (Flask render_template) |
| Styling | Custom CSS with glassmorphism design, Google Fonts (Poppins) |
 
---
 
## Project Structure
 
```
project/
├── app.py               # Flask application with all route definitions
└── templates/
    ├── index.html       # Home page with navigation grid
    ├── sorting.html     # Sorting algorithms module
    ├── searching.html   # Searching algorithms module
    ├── stack.html       # Stack visualization
    ├── queue.html       # Queue visualization
    ├── level3.html      # Level 3 challenges
    ├── level4.html      # Level 4 challenges
    ├── binary_tree.html
    ├── bst.html
    ├── avl.html
    ├── red_black.html
    ├── min_heap.html
    ├── max_heap.html
    ├── m_way.html
    ├── b_tree.html
    ├── graph.html
    ├── hashing.html
    ├── nqueens.html
    ├── dp.html
    ├── greedy.html
    └── tsp.html
```
 
---
 
## Getting Started
 
### Prerequisites
 
- Python 3.8+
- pip
### Installation
 
```bash
# Clone the repository
git clone <your-repo-url>
cd dsa-learning-platform
 
# Install Flask
pip install flask
 
# Run the application
python app.py
```
 
The app will start at `http://127.0.0.1:5000` with debug mode enabled.
 
---
 
## Routes
 
| Route | Description |
|---|---|
| `/` | Home — navigation hub |
| `/sorting` | Sorting algorithms (Merge Sort, Quick Sort, etc.) |
| `/searching` | Binary Search and other searching techniques |
| `/stack` | Stack operations visualization |
| `/queue` | Queue operations visualization |
| `/level3` | Level 3 interactive challenges |
| `/level4` | Level 4 interactive challenges |
| `/binary_tree` | Binary Tree visualization |
| `/bst` | Binary Search Tree |
| `/avl` | AVL Tree (self-balancing) |
| `/red_black` | Red-Black Tree |
| `/min_heap` / `/max_heap` | Heap data structures |
| `/m_way` | M-Way Tree |
| `/b_tree` | B-Tree |
| `/graph` | Graph traversal (BFS/DFS) |
| `/hashing` | Hash Table with collision handling |
| `/nqueens` | N-Queens backtracking visualizer |
| `/dp` | Dynamic Programming (Multistage Graph) |
| `/greedy` | Greedy algorithms |
| `/tsp` | Travelling Salesman Problem (Branch & Bound) |
 
---
 
## Design Highlights
 
The UI uses a dark glassmorphism aesthetic with a gradient background (`#0f172a → #1e293b → #020617`), frosted-glass card components, and an indigo-cyan gradient button scheme — designed to keep the focus on the algorithm visualizations while remaining visually polished.
 
---
 
## Educational Goals
 
- Improve conceptual understanding of DSA
- Develop logical thinking through active problem-solving
- Demonstrate real-world implementation challenges (e.g., hash collisions)
- Make DSA learning engaging enough to stick
---
 
