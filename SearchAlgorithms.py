from collections import deque
from UtilityFunctions import UtilityFunctions

# this class stores all the 6 search algorithms
class SearchAlgorithms:
    def __init__(self, grid, start, goal_states):
        self.grid = grid
        self.start = start
        self.goal_states = goal_states
    
    def bfs(self):                
        rows = len(self.grid)
        cols = len(self.grid[0])
        visited = [[False] * cols for _ in range(rows)]
        queue = deque([(self.start, 0)]) # (initial state, step count)
        visited[self.start[0]][self.start[1]] = True # Mark initial state as visited
        parent = {}
        nodes_generated = 0
        goal_found = None

        while queue:
            nodes_generated += 1
            current_node, step_count = queue.popleft() # Dequeue the first element
            row, col = current_node # Unpack current node coordinates

            print("Current Grid State:")
            self.grid[row][col] = 'C'
            UtilityFunctions.print_grid(self.grid)

            if current_node in self.goal_states:
                goal_found = current_node
                path = [] # Reconstruct the path by backtracking until the start node
                
                while current_node != self.start: 
                    path.append(current_node) # Each current node added into path list 
                    current_node = parent[current_node] # Current nodes updated to parent nodes to BT towards initial node
                path.append(self.start) # Initial node added to path 
                path.reverse() # Reverse the path to obtain correct order
                return path, nodes_generated, goal_found 

            neighbors = [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]
            print("Possible States:")

            # Iterate through each neighbor of the current node
            for neighbor in neighbors: 
                row, col = neighbor
                if 0 <= row < rows and 0 <= col < cols and not visited[row][col] and self.grid[row][col] != '▢':
                    print(neighbor) # Prints valid neighbouring nodes
                    queue.append(((row, col), step_count + 1)) # Enqueue neighbor with incremented step count for exploration in next iteration
                    visited[row][col] = True # Mark neighbor as visited/prevents revisiting
                    parent[(row, col)] = current_node # Save current as the parent for backtracking to other children nodes/neighbouring
            print("--------------------------------------")

        return None, nodes_generated, goal_found

    def dfs(self):
        rows = len(self.grid)
        cols = len(self.grid[0])
        visited = [[False] * cols for _ in range(rows)]
        # (initial state, list of unexplored neighbour w direction priority)
        stack = [(self.start, [(self.start[0] - 1, self.start[1]), (self.start[0], self.start[1] - 1), (self.start[0] + 1, self.start[1]), (self.start[0], self.start[1] + 1)])]
        visited[self.start[0]][self.start[1]] = True
        parent = {}
        nodes_generated = 1 # Initial state
        goal_found = None

        while stack:
            current_node, neighbors = stack[-1]  # Retrieve top element of stack = current & unexplored neighbours
            row, col = current_node

            print("Current Grid State:")
            self.grid[row][col] = 'C'
            UtilityFunctions.print_grid(self.grid)

            if current_node in self.goal_states:
                goal_found = current_node
                path = [] # Reconstruct path
                while current_node != self.start:
                    path.append(current_node)
                    current_node = parent[current_node]
                path.append(self.start)
                path.reverse()
                return path, nodes_generated, goal_found
            
            neighbors = [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]
            print("Next State:")

            next_neighbor = None # Explore unvisited neighbors

            for neighbor in neighbors:
                row, col = neighbor
                if 0 <= row < rows and 0 <= col < cols and not visited[row][col] and self.grid[row][col] != '▢':
                    print(neighbor)
                    next_neighbor = neighbor
                    break  # Ensure finding of first valid neighbour w priority up, left, down, right
            
            if next_neighbor is not None: # If valid unvisited neighbour found,
                stack[-1][1].remove(next_neighbor)  #  Removed from list of unexplored neighbours of current node
                # For exploration in the next iteration
                stack.append((next_neighbor, [(next_neighbor[0] - 1, next_neighbor[1]), (next_neighbor[0], next_neighbor[1] - 1), (next_neighbor[0] + 1, next_neighbor[1]), (next_neighbor[0], next_neighbor[1] + 1)]))
                visited[next_neighbor[0]][next_neighbor[1]] = True # Mark neighbour as visited
                parent[next_neighbor] = current_node # Save current node as parent for backtracking
                nodes_generated += 1 

            else:
                stack.pop()  # If no valid unvisited neighbors, backtrack
            print("--------------------------------------")

        return None, nodes_generated, goal_found

    def depthlimited_dfs(self, max_depth):
        rows = len(self.grid)
        cols = len(self.grid[0])
        visited = [[False] * cols for _ in range(rows)]
        stack = [(self.start, [(self.start[0] - 1, self.start[1]), (self.start[0], self.start[1] - 1), (self.start[0] + 1, self.start[1]), (self.start[0], self.start[1] + 1)])]  # Initial node and unexplored neighbors
        visited[self.start[0]][self.start[1]] = True
        parent = {}
        nodes_generated = 1
        goal_found = None

        while stack:
            current_node, neighbors = stack[-1] # Retrieve top element of stack = current & unexplored neighbours
            row, col = current_node
            
            print("Current Grid State:")
            self.grid[row][col] = 'C'
            UtilityFunctions.print_grid(self.grid)

            if current_node in self.goal_states:
                goal_found = current_node
                path = []
                while current_node != self.start:
                    path.append(current_node)
                    current_node = parent[current_node]
                path.append(self.start)
                path.reverse() 
                return path, nodes_generated, goal_found

            neighbors = [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]
            print("Next State:")

            if len(stack) <= max_depth: # Explore unvisited neighbors up to the maximum depth
                next_neighbor = None

                for neighbor in neighbors:
                    row, col = neighbor
                    if 0 <= row < rows and 0 <= col < cols and not visited[row][col] and self.grid[row][col] != '▢':
                        print(neighbor)
                        next_neighbor = neighbor
                        break  # Find the first valid neighbor according to the priority of up, left, down, right

                if next_neighbor is not None:
                    stack[-1][1].remove(next_neighbor)  # Remove the explored neighbor from unexplored neighbors
                    stack.append((next_neighbor, [(next_neighbor[0] - 1, next_neighbor[1]), (next_neighbor[0], next_neighbor[1] - 1), (next_neighbor[0] + 1, next_neighbor[1]), (next_neighbor[0], next_neighbor[1] + 1)]))
                    visited[next_neighbor[0]][next_neighbor[1]] = True
                    parent[next_neighbor] = current_node
                    
                    nodes_generated += 1 

                else:
                    stack.pop()  # If no valid unvisited neighbors, backtrack
            else:
                stack.pop()  # If maximum depth reached, backtrack
            print("--------------------------------------")
        
        return None, nodes_generated, goal_found

    def gbfs(self):
        rows = len(self.grid)
        cols = len(self.grid[0])
        visited = [[False] * cols for _ in range(rows)]

        # A deque initialized with start position
        queue = deque([self.start])

        visited[self.start[0]][self.start[1]] = True
        parent = {}
        nodes_generated = 0
        goal_found = None

        while queue:
            nodes_generated += 1

            # Sort the queue based on heuristic value f(n) = h(n)
            # elements with the smaller heuristic value x[1] will appear first in the sorted queue
            queue = deque(sorted(queue, key=lambda x: min(UtilityFunctions.manhattan_distance(x, goal) for goal in self.goal_states)))

            current_node = queue.popleft()
            row, col = current_node

            print("Current Grid State:")
            self.grid[row][col] = 'C'
            UtilityFunctions.print_grid(self.grid)

            if current_node in self.goal_states:
                goal_found = current_node
                path = []
                while current_node != self.start:
                    path.append(current_node)
                    current_node = parent[current_node]
                path.append(self.start)
                path.reverse()
                return path, nodes_generated, goal_found

            neighbors = [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]
            
            # Explore neighbors based on direction priority
            for neighbor in neighbors:
                row, col = neighbor
                if 0 <= row < rows and 0 <= col < cols and not visited[row][col] and self.grid[row][col] != '▢':
                    print("Next State:", neighbor)
                    queue.append(neighbor)
                    visited[row][col] = True
                    parent[neighbor] = current_node

            print("--------------------------------------")
        return None, nodes_generated, goal_found
    
    def astar(self):
        rows = len(self.grid)
        cols = len(self.grid[0])
        visited = [[False] * cols for _ in range(rows)]
        
        # Calculate distances from the start to all goal states
        distances = [UtilityFunctions.manhattan_distance(self.start, goal) for goal in self.goal_states]
        
        # Find the index of the goal state with the shortest distance
        goal_index = min(range(len(self.goal_states)), key=lambda i: distances[i])
        
        # Initialize the queue with the shortest goal state
        queue = deque([(self.start, 0, distances[goal_index])])
        
        visited[self.start[0]][self.start[1]] = True
        parent = {}
        nodes_generated = 0
        goal_found = None

        while queue:
            nodes_generated += 1

            # Sort based on f(n) = g(n) + h(n)
            queue = deque(sorted(queue, key=lambda x: x[1] + x[2]))
            
            current_node, cost, _ = queue.popleft()
            row, col = current_node

            print("Current Grid State:")
            self.grid[row][col] = 'C'
            UtilityFunctions.print_grid(self.grid)

            # Check if the current node is a goal state
            if current_node in self.goal_states:
                goal_found = current_node
                path = []
                while current_node != self.start:
                    path.append(current_node)
                    current_node = parent[current_node]
                path.append(self.start)
                path.reverse()
                return path, nodes_generated, goal_found

            neighbors = [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]
            print("Possible States:")
            
            for neighbor in neighbors:
                row, col = neighbor
                if 0 <= row < rows and 0 <= col < cols and not visited[row][col] and self.grid[row][col] != '▢':
                    print(neighbor)

                    g_value = cost + 1  # same cost for each step
                    h_value = min(UtilityFunctions.manhattan_distance(neighbor, goal) for goal in self.goal_states)
                    
                    # key=lambda x: x[1] + x[2]))
                    queue.append((neighbor, g_value, h_value))
                    visited[row][col] = True
                    parent[neighbor] = current_node
            print("--------------------------------------")

        return None, nodes_generated, goal_found

    def depthlimited_astar(self, max_depth):
        rows = len(self.grid)
        cols = len(self.grid[0])
        visited = [[False] * cols for _ in range(rows)]

        # Calculate distances from the start to all goal states
        distances = [UtilityFunctions.manhattan_distance(self.start, goal) for goal in self.goal_states]
        
        # Find the index of the goal state with the shortest distance
        goal_index = min(range(len(self.goal_states)), key=lambda i: distances[i])
        
        # Initialize the queue with the shortest goal state
        queue = deque([(self.start, 0, distances[goal_index])])

        visited[self.start[0]][self.start[1]] = True
        parent = {}
        nodes_generated = 0  
        goal_found = None

        while queue:
            nodes_generated += 1

            # Sort based on f(n) = g(n) + h(n)
            queue = deque(sorted(queue, key=lambda x: x[1] + x[2]))
            
            current_node, cost, _ = queue.popleft()
            row, col = current_node

            print("Current State:")
            self.grid[row][col] = 'C'
            UtilityFunctions.print_grid(self.grid)

            # Check if the current node is a goal state
            if current_node in self.goal_states:
                goal_found = current_node
                path = []
                while current_node != self.start:
                    path.append(current_node)
                    current_node = parent[current_node]
                path.append(self.start)
                path.reverse()
                return path, nodes_generated, goal_found

            if cost >= max_depth:
                continue  # Skip exploring further if depth exceeds the maximum allowed depth

            neighbors = [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]
            print("Possible States:")

            for neighbor in neighbors:
                row, col = neighbor
                if 0 <= row < rows and 0 <= col < cols and not visited[row][col] and self.grid[row][col] != '▢':
                    print(neighbor)

                    g_value = cost + 1  # same cost for each step
                    h_value = min(UtilityFunctions.manhattan_distance(neighbor, goal) for goal in self.goal_states)
                    
                    # key=lambda x: x[1] + x[2]))
                    queue.append((neighbor, g_value, h_value))
                    visited[row][col] = True
                    parent[neighbor] = current_node
            print("--------------------------------------")

        return None, nodes_generated, goal_found