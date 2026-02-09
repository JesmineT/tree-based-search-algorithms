from UtilityFunctions import UtilityFunctions

class GridManipulationAndVisualization:
    @staticmethod # creates an empty grid with specified dimensions
    def create_empty_grid(num_rows, num_cols):
        return [['-' for _ in range(num_cols)] for _ in range(num_rows)]

    @staticmethod # marks the initial state on the grid
    def mark_initial_state(grid, point_x, point_y):
        grid[point_x][point_y] = 'X'  # Correct order: row, column

    @staticmethod # marks the goal states on the grid
    def mark_goal_states(grid, goal_states):
        for goal_state in goal_states:
            grid[goal_state[0]][goal_state[1]] = '♕'  # Correct order: row, column

    @staticmethod # marks obstacles on the grid
    def mark_obstacles(grid, obstacles, goal_states):
        for obstacle in obstacles:
            column, row, width, height = obstacle
            for i in range(row, row + height):
                for j in range(column, column + width):
                    if (i,j) not in goal_states:
                     grid[i][j] = '▢'  # Correct order: row, column

    @staticmethod # computes directions for the entire path
    def compute_path_directions(path): #gives direction for entire path
        directions = []
        for i in range(len(path) - 1):
            directions.append(UtilityFunctions.get_direction(path[i], path[i + 1]))
        return directions

    @staticmethod # prints the path with the grid
    def print_path_with_grid(filename, method, goal_found, number_of_nodes, path, grid, execution_time):
        directions = [UtilityFunctions.get_direction(path[i], path[i+1]) for i in range(len(path)-1)]
        direction_str = ' '.join(directions)
        path_str = ' '.join(map(str, path))
        print(f"\n{filename} {method} \n{goal_found} {number_of_nodes}\n{direction_str}\n{path_str}")
        print("Grid with Final Path:")
        GridManipulationAndVisualization.print_grid_with_path(grid, path)
        print(f"Execution Time: {execution_time} seconds")

    @staticmethod # prints the grid with the final path marked
    def print_grid_with_path(grid, path):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in path:
                    print('*', end=' ')
                else:
                    print(grid[i][j], end=' ')
            print()

    @staticmethod # prints a message when no path is found
    def print_no_path(filename, method, number_of_nodes):
        msg = "No goal is reachable;"
        print(f"{filename} {method}\n{msg} {number_of_nodes}")