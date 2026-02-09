import os
import sys
import time
from FileObjectExtraction import FileObjectExtraction
from GridManipulationAndVisualization import GridManipulationAndVisualization
from BasicTestCases import BasicTestCases
from ResearchTestCases import ResearchTestCases
from SearchAlgorithms import SearchAlgorithms
from UtilityFunctions import UtilityFunctions
from ReportAndData import ReportAndData

class Main:
    def main():   

        obstacles = []

        if len(sys.argv) != 4:
            print("Usage: python script.py input.txt 'search algorithm' 'test case'")
            sys.exit(1)

        input_file = sys.argv[1]
        algorithm = sys.argv[2]
        test_case = sys.argv[3]

        basic_test_cases = BasicTestCases(input_file)
        research_test_cases = ResearchTestCases(input_file)

        if algorithm not in ["BFS", "DFS", "DL-DFS", "GBFS", "A*", "DL-A*"]:
            print("Error: Algorithm not found.")
            sys.exit(1)

        if test_case in ["OpenSpace", "RobotNav", "GoalSurrounded", "Switzerland", "X", "GoalBlocked", "DiverseObstacles", "FlappyBird", "Maze", "RandomObstacles", "OpenSpace-Small", "OpenSpace-Medium", "OpenSpace-Large", "Switzerland-Small", "Switzerland-Medium", "Switzerland-Large", "X-Small", "X-Medium", "X-Large", "FlappyBird-Small", "FlappyBird-Medium", "FlappyBird-Large", "RandomObstacles-Small", "RandomObstacles-Medium", "RandomObstacles-Large"]:
            if os.path.isfile(input_file) and os.path.getsize(input_file) > 0:
                UtilityFunctions.clear_test_case_content(input_file)
        else:
            print("Error: Test case not found.")
            sys.exit(1)

        if test_case == "OpenSpace":
            print("Test Case Generated: OpenSpace")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                basic_test_cases.generate_openspace_testcase()

        if test_case == "RobotNav":
            print("Test Case Generated: RobotNav")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                basic_test_cases.generate_robotnav_testcase()

        if test_case == "GoalSurrounded":
            print("Test Case Generated: GoalSurrounded")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                basic_test_cases.generate_goalsurrounded_testcase()

        if test_case == "Switzerland":
            print("Test Case Generated: Switzerland")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                basic_test_cases.generate_switzerland_testcase()

        if test_case == "X":
            print("Test Case Generated: X")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                basic_test_cases.generate_x_testcase()
        
        if test_case == "GoalBlocked":
            print("Test Case Generated: GoalBlocked")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                basic_test_cases.generate_goalblocked_testcase()
        
        if test_case == "DiverseObstacles":
            print("Test Case Generated: DiverseObstacles")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                basic_test_cases.generate_diverseobstacles_testcase()

        if test_case == "FlappyBird":
            print("Test Case Generated: FlappyBird")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                basic_test_cases.generate_flappybird_testcase()
        
        if test_case == "Maze":
            print("Test Case Generated: Maze")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                basic_test_cases.generate_maze_testcase()

        if test_case == "RandomObstacles":
            print("Test Case Generated: RandomObstacles")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                basic_test_cases.generate_randomobstacles_testcase()

        if test_case == "OpenSpace-Small":
            print("Test Case Generated: OpenSpace with the size 'Small'")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                research_test_cases.generate_openspace_testcase_small()

        if test_case == "OpenSpace-Medium":
            print("Test Case Generated: OpenSpace with the size 'Medium'")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                research_test_cases.generate_openspace_testcase_medium()

        if test_case == "OpenSpace-Large":
            print("Test Case Generated: OpenSpace with the size 'Large'")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                research_test_cases.generate_openspace_testcase_large()

        if test_case == "Switzerland-Small":
            print("Test Case Generated: Switzerland with the size 'Small'")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                research_test_cases.generate_switzerland_testcase_small()
        
        if test_case == "Switzerland-Medium":
            print("Test Case Generated: Switzerland with the size 'Medium'")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                research_test_cases.generate_switzerland_testcase_medium()

        if test_case == "Switzerland-Large":
            print("Test Case Generated: Switzerland with the size 'Large'")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                research_test_cases.generate_switzerland_testcase_large()

        if test_case == "X-Small":
            print("Test Case Generated: X with the size 'Small'")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                research_test_cases.generate_x_testcase_small()

        if test_case == "X-Medium":
            print("Test Case Generated: X with the size 'Medium'")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                research_test_cases.generate_x_testcase_medium()

        if test_case == "X-Large":
            print("Test Case Generated: X with the size 'Large'")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                research_test_cases.generate_x_testcase_large()

        if test_case == "FlappyBird-Small":
            print("Test Case Generated: FlappyBird with the size 'Small'")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                research_test_cases.generate_flappybird_testcase_small()

        if test_case == "FlappyBird-Medium":
            print("Test Case Generated: FlappyBird with the size 'Medium'")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                research_test_cases.generate_flappybird_testcase_medium()
        
        if test_case == "FlappyBird-Large":
            print("Test Case Generated: FlappyBird with the size 'Large'")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                research_test_cases.generate_flappybird_testcase_large()

        if test_case == "RandomObstacles-Small":
            print("Test Case Generated: RandomObstacles with the size 'Small'")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                research_test_cases.generate_randomobstacles_small()
        
        if test_case == "RandomObstacles-Medium":
            print("Test Case Generated: RandomObstacles with the size 'Medium'")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                research_test_cases.generate_randomobstacles_medium()

        if test_case == "RandomObstacles-Large":
            print("Test Case Generated: RandomObstacles with the size 'Large'")
            if not os.path.isfile(input_file) or os.path.getsize(input_file) == 0:
                research_test_cases.generate_randomobstacles_large()
            
        content = FileObjectExtraction.read_input_file(input_file)

        if len(content) < 3:
            print("Error: Input file should contain at least three lines.") # dimension state, initial state, goal state
            sys.exit(1)

        first_line = content[0].strip()
        num_cols, num_rows = FileObjectExtraction.extract_grid_dimensions(first_line)  # Correct order: columns, rows

        second_line = content[1].strip()
        point_y, point_x = FileObjectExtraction.extract_point_coordinates(second_line)  # Correct order: row, column

        third_line = content[2].strip()
        goal_states = FileObjectExtraction.extract_goal_states(third_line)

        initial_state = (point_x, point_y)  # Correct order: row, column

        grid = GridManipulationAndVisualization.create_empty_grid(num_rows, num_cols)
        search_algos = SearchAlgorithms(grid, initial_state, goal_states)
        
        GridManipulationAndVisualization.mark_initial_state(grid, point_x, point_y)
        GridManipulationAndVisualization.mark_goal_states(grid, goal_states)

        if len(content) > 3:
            obstacles = FileObjectExtraction.extract_obstacles(content[3:])
            GridManipulationAndVisualization.mark_obstacles(grid, obstacles, goal_states)

        print("Empty Grid:")
        UtilityFunctions.print_grid(grid)
        print("Initial State:")
        print(initial_state)
        print("Goal States:")
        print(goal_states)
        print("Obstacles:")
        print(obstacles)

        start_time = time.time()  # Measure start time

        if algorithm == "BFS":
            print(f"Path from {initial_state} to one goal:")
            path, nodes_generated, goal_found = search_algos.bfs()
            if path:
                directions = GridManipulationAndVisualization.compute_path_directions(path)
                end_time = time.time()  # Measure end time
                execution_time = end_time - start_time
                GridManipulationAndVisualization.print_path_with_grid(input_file, algorithm, goal_found, nodes_generated, path, grid, execution_time)
                ReportAndData.add_report_data(input_file, {
                    "algorithm": algorithm,
                    "goal found": goal_found,
                    "nodes generated": nodes_generated,
                    "path": path,
                    "directions": directions,
                    "execution time": execution_time,
                }, test_case, algorithm)

            else:
                GridManipulationAndVisualization.print_no_path(input_file, algorithm, nodes_generated)
                ReportAndData.add_report_data(input_file, {
                    "algorithm": algorithm,
                    "goal found": goal_found,
                    "nodes generated": nodes_generated,
                    "path": None,
                    "directions": None,
                    "execution time": None,
                }, test_case, algorithm)
            
        if algorithm == "DFS":
            print(f"Path from {initial_state} to one goal:")
            path, nodes_generated, goal_found = search_algos.dfs()
            if path:
                directions = GridManipulationAndVisualization.compute_path_directions(path)
                end_time = time.time()  # Measure end time
                execution_time = end_time - start_time
                GridManipulationAndVisualization.print_path_with_grid(input_file, algorithm, goal_found, nodes_generated, path, grid, execution_time)
                ReportAndData.add_report_data(input_file, {
                    "algorithm": algorithm,
                    "goal found": goal_found,
                    "nodes generated": nodes_generated,
                    "path": path,
                    "directions": directions,
                    "execution time": execution_time,
                }, test_case, algorithm)
            else:
                GridManipulationAndVisualization.print_no_path(input_file, algorithm, nodes_generated)
                ReportAndData.add_report_data(input_file, {
                    "algorithm": algorithm,
                    "goal found": goal_found,
                    "nodes generated": nodes_generated,
                    "path": None,
                    "directions": None,
                    "execution time": None,
                }, test_case, algorithm)

        if algorithm == "DL-DFS":
            max_depth = 1000
            print(f"Path from {initial_state} to one goal:")
            path, nodes_generated, goal_found = search_algos.depthlimited_dfs(max_depth)
            if path:
                directions = GridManipulationAndVisualization.compute_path_directions(path)
                end_time = time.time()  # Measure end time
                execution_time = end_time - start_time
                GridManipulationAndVisualization.print_path_with_grid(input_file, algorithm, goal_found, nodes_generated, path, grid, execution_time)
                ReportAndData.add_report_data(input_file, {
                    "algorithm": algorithm,
                    "goal found": goal_found,
                    "nodes generated": nodes_generated,
                    "path": path,
                    "directions": directions,
                    "execution time": execution_time,
                    "max depth": max_depth,
                }, test_case, algorithm)
            else:
                GridManipulationAndVisualization.print_no_path(input_file, algorithm, nodes_generated)
                ReportAndData.add_report_data(input_file, {
                    "algorithm": algorithm,
                    "goal found": goal_found,
                    "nodes generated": nodes_generated,
                    "path": None,
                    "directions": None,
                    "execution time": None,
                    "max depth": max_depth,
                }, test_case, algorithm)

        if algorithm == "GBFS":
            print(f"Path from {initial_state} to one goal:")
            path, nodes_generated, goal_found = search_algos.gbfs()
            if path:
                directions = GridManipulationAndVisualization.compute_path_directions(path)
                end_time = time.time()  # Measure end time
                execution_time = end_time - start_time
                GridManipulationAndVisualization.print_path_with_grid(input_file, algorithm, goal_found, nodes_generated, path, grid, execution_time)
                ReportAndData.add_report_data(input_file, {
                    "algorithm": algorithm,
                    "goal found": goal_found,
                    "nodes generated": nodes_generated,
                    "path": path,
                    "directions": directions,
                    "execution time": execution_time,
                }, test_case, algorithm)
            else:
                GridManipulationAndVisualization.print_no_path(input_file, algorithm, nodes_generated)
                ReportAndData.add_report_data(input_file, {
                    "algorithm": algorithm,
                    "goal found": goal_found,
                    "nodes generated": nodes_generated,
                    "path": None,
                    "directions": None,
                    "execution time": None,
                }, test_case, algorithm)

        if algorithm == "A*":
            print(f"Path from {initial_state} to one goal:")
            path, nodes_generated, goal_found = search_algos.astar()
            if path:
                directions = GridManipulationAndVisualization.compute_path_directions(path)
                end_time = time.time()  # Measure end time
                execution_time = end_time - start_time
                GridManipulationAndVisualization.print_path_with_grid(input_file, algorithm, goal_found, nodes_generated, path, grid, execution_time)
                ReportAndData.add_report_data(input_file, {
                    "algorithm": algorithm,
                    "goal found": goal_found,
                    "nodes generated": nodes_generated,
                    "path": path,
                    "directions": directions,
                    "execution time": execution_time,
                }, test_case, algorithm)
            else:
                GridManipulationAndVisualization.print_no_path(input_file, algorithm, nodes_generated)
                ReportAndData.add_report_data(input_file, {
                    "algorithm": algorithm,
                    "goal found": goal_found,
                    "nodes generated": nodes_generated,
                    "path": None,
                    "directions": None,
                    "execution time": None,
                }, test_case, algorithm)

        if algorithm == "DL-A*":
            max_depth = 1000
            print(f"Path from {initial_state} to one goal:")
            path, nodes_generated, goal_found = search_algos.depthlimited_astar(max_depth)
            if path:
                directions = GridManipulationAndVisualization.compute_path_directions(path)
                end_time = time.time()  # Measure end time
                execution_time = end_time - start_time
                GridManipulationAndVisualization.print_path_with_grid(input_file, algorithm, goal_found, nodes_generated, path, grid, execution_time)
                ReportAndData.add_report_data(input_file, {
                    "algorithm": algorithm,
                    "goal found": goal_found,
                    "nodes generated": nodes_generated,
                    "path": path,
                    "directions": directions,
                    "execution time": execution_time,
                    "max depth": max_depth,
                }, test_case, algorithm)
            else:
                GridManipulationAndVisualization.print_no_path(input_file, algorithm, nodes_generated)
                ReportAndData.add_report_data(input_file, {
                    "algorithm": algorithm,
                    "goal found": goal_found,
                    "nodes generated": nodes_generated,
                    "path": None,
                    "directions": None,
                    "execution time": None,
                    "max depth": max_depth,
                }, test_case, algorithm)

        ReportAndData.write_report()

    if __name__ == "__main__":
        main()
