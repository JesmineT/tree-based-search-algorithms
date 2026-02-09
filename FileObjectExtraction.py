import re
import sys

class FileObjectExtraction:
    @staticmethod # reads contents of the file
    def read_input_file(file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.readlines()
                return content
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            sys.exit(1)

    @staticmethod # extracts grid dimensions from the line
    def extract_grid_dimensions(line):
        numbers = re.findall(r'\d+', line)
        if len(numbers) >= 2:
            return int(numbers[1]), int(numbers[0])  # Reversed column and row
        else:
            print("Error: The first line should contain at least two numbers.")
            sys.exit(1)

    @staticmethod # extracts initial coordinates from the line
    def extract_point_coordinates(line):
        numbers = re.findall(r'\d+', line)
        if len(numbers) >= 2:
            return int(numbers[0]), int(numbers[1])  # Correct order: row, column
        else:
            print("Error: The second line should contain at least two numbers.")
            sys.exit(1)

    @staticmethod # extracts goal states from the line
    def extract_goal_states(line):
        goal_states = re.findall(r'\((\d+),(\d+)\)', line)
        return [(int(y), int(x)) for x, y in goal_states]  # Reversed column and row

    @staticmethod # extracts obstacles from lines
    def extract_obstacles(lines):
        obstacles = []
        for line in lines:
            numbers = re.findall(r'\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)', line)
            if numbers:
                column, row, width, height = map(int, numbers[0])
                obstacles.append((column, row, width, height))
        return obstacles