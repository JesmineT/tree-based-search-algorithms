import random

class UtilityFunctions:
    
    @staticmethod # this function is used in Main class
    def clear_test_case_content(file_path):
        try:
            with open(file_path, 'w') as file:
                file.write('')
                print(f"Cleared existing content in '{file_path}'")
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod # this function is used in GridManipulationAndVisualization class
    def get_direction(prev_node, next_node): #gives direction between two adjacent nodes
            prev_row, prev_column = prev_node
            next_row, next_column = next_node

            if prev_row < next_row:
                return "'DOWN'"
            elif prev_row > next_row:
                return "'UP'"
            elif prev_column < next_column:
                return "'RIGHT'"
            elif prev_column > next_column:
                return "'LEFT'"
            else:
                return "stay"
       
    @staticmethod # ths function is used in SearchAlgorithms and Main class
    def print_grid(grid):
            for row in grid:
                print(' '.join(row))

    @staticmethod # this function is used in SearchAlgorithms class
    def manhattan_distance(node, goal_state):
            x1, y1 = node
            x2, y2 = goal_state
            return abs(x1 - x2) + abs(y1 - y2)

    @staticmethod # this function is used in ResearchTestCases and BasicTestCases class
    def randomized_obstacles(grid_dimensions): 
        num_rows, num_cols = grid_dimensions
        total_cells = num_rows * num_cols
        num_obstacles = int(total_cells * 0.05)  # 2% of the total cells
        obstacles = []
        for _ in range(num_obstacles):
            row = random.randint(0, num_rows - 1)
            col = random.randint(0, num_cols - 1)
            width = random.randint(1, min(num_cols - col, 5))  # Random width, maximum of 5 cells
            height = random.randint(1, min(num_rows - row, 5))  # Random height, maximum of 5 cells
            obstacles.append((row, col, width, height))
        return obstacles

    @staticmethod # this function is used in ResearchTestCases class
    def randomobstacles_utils(f, rows, cols): 
        f.write(f"[{rows},{cols}]\n") # Define grid
        f.write("(0,0)\n") # Define initial state
        f.write(f"({cols-1},{rows-1})\n") # Define goals
        obstacles = UtilityFunctions.randomized_obstacles((rows, cols))
        for obstacle in obstacles:
            f.write(f"({obstacle[1]},{obstacle[0]},{obstacle[2]},{obstacle[3]})\n") # Define obstacles

    @staticmethod # this function is used in ResearchTestCases class
    def openspace_utils(f, rows, cols): 
        f.write(f"[{rows},{cols}]\n") # Define grid
        f.write("(0,0)\n") # Define initial state
        f.write(f"({cols-1},{rows-1})\n") # Define goals

    @staticmethod # this function is used in ResearchTestCases class
    def switzerland_utils(f, rows, cols):
        f.write(f"[{rows},{cols}]\n") # Define grid
        f.write(f"({cols//2},{rows//2})\n") # Define initial state
        f.write(f"(0,{rows//2}) | ({cols//2},0) | ({cols-1},{rows//2}) | ({cols//2},{rows-1})\n") # Define goals

        # define top obstacles
        for i in range(rows//2):
            f.write(f"({(cols//2)-1},{i},1,1)\n")
            f.write(f"({(cols//2)+1},{i},1,1)\n")

        # define left obstacles
        for i in range(cols//2):
            f.write(f"({i},{(rows//2)-1},1,1)\n")
            f.write(f"({i},{(rows//2)+1},1,1)\n")

        # define bottom obstacles
        for i in range(rows//2):
            f.write(f"({(cols//2)-1},{rows-i-1},1,1)\n")
            f.write(f"({(cols//2)+1},{rows-i-1},1,1)\n")

        # define right obstacles
        for i in range(cols//2):
            f.write(f"({(cols//2)+1 + i},{(rows//2)-1},1,1)\n")
            f.write(f"({(cols//2)+1 + i},{(rows//2)+1},1,1)\n")

    @staticmethod # this function is used in ResearchTestCases class
    def x_utils(f, size):
        f.write(f"[{size},{size}]\n") # Define grid
        initial_row = size // 2
        initial_col = size // 2
        f.write(f"({initial_col},{initial_row})\n") # Define initial state
        goal1_row = 0
        goal1_col = 0
        goal2_row = size - 1
        goal2_col = size - 1
        goal3_row = 0
        goal3_col = size - 1
        goal4_row = size - 1
        goal4_col = 0
        f.write(f"({goal1_col},{goal1_row}) | ({goal2_col},{goal2_row}) | ({goal3_col},{goal3_row}) | ({goal4_col},{goal4_row})\n") # Define goals

        # Define Top obstacles
        top_initial_row = initial_row - 1
        num_obstacles = 1
        for i in range(top_initial_row - 1, -1, -1):
            for _ in range(num_obstacles):
                f.write(f"({initial_col},{i},1,1)\n")
                initial_col -= 1
            num_obstacles += 2
            initial_col = size // 2 + (top_initial_row - i)

        initial_col = size // 2

        # Define Bottom obstacles
        bottom_initial_row = initial_row + 1 
        num_obstacles = 1
        for i in range(bottom_initial_row + 1, size):
            for _ in range(num_obstacles):
                f.write(f"({initial_col},{i},1,1)\n")
                initial_col -= 1
            num_obstacles += 2
            initial_col = size // 2 + (i - bottom_initial_row)

        initial_col = size // 2

        # Define Left obstacles
        num_obstacles = 1
        for i in range(initial_col - 1, -1, -1):
            for _ in range(num_obstacles):
                f.write(f"({i},{initial_row},1,1)\n")
                initial_row -= 1
            num_obstacles += 2
            initial_row = size // 2 + (initial_col - i)

        # Define Right obstacles
        initial_row = size // 2  
        num_obstacles = 1
        for i in range(initial_col + 1, size):
            for _ in range(num_obstacles):
                f.write(f"({i},{initial_row},1,1)\n")
                initial_row -= 1
            num_obstacles += 2
            initial_row = size // 2 + (i - initial_col)

    @staticmethod # this function is used in ResearchTestCases class
    def flappybird_utils(f, rows, cols, initial_col, initial_row):
        f.write(f"[{rows},{cols}]\n") # Define grid      
        f.write(f"{initial_col}, {initial_row}\n") # Define initial state
                
        goal1_row = 0
        goal1_col = cols - 1
        goal2_row = rows // 2
        goal2_col = cols - 1
        goal3_row = rows - 1
        goal3_col = cols - 1     
        f.write(f"({goal1_col},{goal1_row}) | ({goal2_col},{goal2_row}) | ({goal3_col},{goal3_row})\n") # Define goals

        # Populate obstacles above and below the initial position column
        for i in range(rows):
            if i != rows // 2:
                f.write(f"({initial_col},{i},1,1)\n")

        # Populate obstacles for every column in a line vertically
        for col in range(1, min(cols - 1, cols - 2)):
            # Generate a random row index to skip
            random_row = random.randint(0, rows - 1)
            for row in range(rows):
                if col % 2 == 0:
                    if row != random_row:
                        f.write(f"({col},{row},1,1)\n")

        # Populate obstacles just before the goal column vertically
        for i in range(rows):
            if i != goal1_row and i != goal2_row and i != goal3_row:
                f.write(f"({goal1_col - 1},{i},1,1)\n")
                f.write(f"({goal2_col - 1},{i},1,1)\n")
                f.write(f"({goal3_col - 1},{i},1,1)\n")
