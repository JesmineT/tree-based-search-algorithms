# AI Pathfinding Algorithms
Implementation and comparison of 6 tree-based search algorithms for robot navigation on grid environments.

## Overview
**Algorithms Implemented:**
- **Uninformed**: BFS, DFS, Depth-Limited DFS
- **Informed**: GBFS, A*, Depth-Limited A*

**Features:**
- 25+ test cases (manual + randomized)
- Performance benchmarking (nodes generated, execution time, path optimality)
- JSON report generation
- Automated testing framework

## Usage
```bash
python Main.py <input_file> <algorithm> <test_case>
```

**Example:**
```bash
python Main.py input.txt A* RobotNav
```

**Algorithms:** `BFS`, `DFS`, `DL-DFS`, `GBFS`, `A*`, `DL-A*`

**Basic Test Cases:**
- `OpenSpace` - No obstacles
- `RobotNav` - Basic obstacle navigation
- `GoalSurrounded` - Limited goal access
- `Maze` - Complex pathfinding
- `FlappyBird` - Narrow passages
- `RandomObstacles` - 5% random coverage
- `Switzerland`, `X`, `GoalBlocked`, `DiverseObstacles`

**Research Test Cases:** Add `-Small`, `-Medium`, or `-Large` suffix to: `OpenSpace`, `Switzerland`, `X`, `FlappyBird`, `RandomObstacles`

## Results
### Algorithm Performance
| Algorithm | Speed | Optimality | Best Use Case |
|-----------|-------|------------|---------------|
| BFS | Slowest | Guaranteed shortest path | Small grids, unweighted graphs |
| DFS | Moderate | Not optimal | Memory-constrained scenarios |
| DL-DFS | Fast | Not optimal | Depth-limited exploration |
| GBFS | **Fastest** | Not guaranteed | Simple environments |
| **A*** | **Fast** | **Guaranteed optimal** | **General purpose (recommended)** |
| DL-A* | Very Fast | Optimal within depth | Depth-constrained scenarios |

### Summarized Findings
- **Informed algorithms** (GBFS, A*, DL-A*) are 40-60% faster than uninformed methods
- **A*** consistently finds shortest paths by balancing heuristic and actual cost
- **GBFS** is fastest but may miss optimal paths in complex environments
- **Depth-limited variants** show efficiency gains through constrained search
---

*Educational project demonstrating AI search algorithms for robot navigation*
