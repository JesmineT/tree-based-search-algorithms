import random
from UtilityFunctions import UtilityFunctions

# this class generates the research test cases (test cases with randomized grid dimensions)
class ResearchTestCases:
    def __init__(self, input_file):
        self.input_file = input_file

    def generate_randomobstacles_small(self):
        rows = random.randint(5, 10)
        cols = random.randint(5, 10)
        with open(self.input_file, 'w') as f:
            UtilityFunctions.randomobstacles_utils(f, rows, cols)

    def generate_randomobstacles_medium(self):
        rows = random.randint(11, 15)
        cols = random.randint(11, 15)
        with open(self.input_file, 'w') as f:
            UtilityFunctions.randomobstacles_utils(f, rows, cols)

    def generate_randomobstacles_large(self):
        rows = random.randint(16, 20)
        cols = random.randint(16, 20)
        with open(self.input_file, 'w') as f:
            UtilityFunctions.randomobstacles_utils(f, rows, cols)

    def generate_openspace_testcase_small(self):
        rows = random.randint(5, 11)
        cols = random.randint(3, 5)
        with open(self.input_file, 'w') as f:
            UtilityFunctions.openspace_utils(f, rows, cols)

    def generate_openspace_testcase_medium(self):
        rows = random.randint(12, 21)
        cols = random.randint(6, 15)
        with open(self.input_file, 'w') as f:
            UtilityFunctions.openspace_utils(f, rows, cols)

    def generate_openspace_testcase_large(self):
        rows = random.randint(22, 31)
        cols = random.randint(16, 25)
        with open(self.input_file, 'w') as f:
            UtilityFunctions.openspace_utils(f, rows, cols)
    
    def generate_switzerland_testcase_small(self):
        rows = random.randint(3,9)
        cols = random.randint(3,9)
        rows = rows + 1 if rows % 2 == 0 else rows
        cols = cols + 1 if cols % 2 == 0 else cols
        with open(self.input_file, 'w') as f:
            UtilityFunctions.switzerland_utils(f, rows, cols)

    def generate_switzerland_testcase_medium(self):
        rows = random.randint(9, 15)
        cols = random.randint(9, 15)
        rows = rows + 1 if rows % 2 == 0 else rows
        cols = cols + 1 if cols % 2 == 0 else cols
        with open(self.input_file, 'w') as f:
            UtilityFunctions.switzerland_utils(f, rows, cols)

    def generate_switzerland_testcase_large(self):
        rows = random.randint(15, 21)
        cols = random.randint(15, 21)
        rows = rows + 1 if rows % 2 == 0 else rows
        cols = cols + 1 if cols % 2 == 0 else cols
        with open(self.input_file, 'w') as f:
            UtilityFunctions.switzerland_utils(f, rows, cols)
            
    def generate_x_testcase_small(self):
        size = random.randint(5, 11)  # Choose a random odd size for the square
        size = size + 1 if size % 2 == 0 else size  # Ensure size is odd
        with open(self.input_file, 'w') as f:
            UtilityFunctions.x_utils(f, size)

    def generate_x_testcase_medium(self):
        size = random.randint(11, 17)  # Choose a random odd size for the square
        size = size + 1 if size % 2 == 0 else size  # Ensure size is odd
        with open(self.input_file, 'w') as f:
            UtilityFunctions.x_utils(f, size)

    def generate_x_testcase_large(self):
        size = random.randint(17, 23)  # Choose a random odd size for the square
        size = size + 1 if size % 2 == 0 else size  # Ensure size is odd
        with open(self.input_file, 'w') as f:
            UtilityFunctions.x_utils(f, size)

    def generate_flappybird_testcase_small(self):
        rows = random.randint(5, 10)
        cols = random.randint(5, 10)
        rows = rows if rows % 2 != 0 else rows - 1 # ensures row is odd
        cols = cols if cols % 2 == 0 else cols + 1 # ensures col is even
        with open(self.input_file, 'w') as f:            
            UtilityFunctions.flappybird_utils(f, rows, cols, initial_col=0, initial_row=rows // 2)

    def generate_flappybird_testcase_medium(self):
        rows = random.randint(10, 15)
        cols = random.randint(10, 15)
        rows = rows if rows % 2 != 0 else rows - 1 # ensures row is odd
        cols = cols if cols % 2 == 0 else cols + 1 # ensures col is even
        with open(self.input_file, 'w') as f:
            UtilityFunctions.flappybird_utils(f, rows, cols, initial_col=0, initial_row=rows // 2)

    def generate_flappybird_testcase_large(self):
        rows = random.randint(15, 20)
        cols = random.randint(15, 20)
        rows = rows if rows % 2 != 0 else rows - 1 # ensures row is odd
        cols = cols if cols % 2 == 0 else cols + 1 # ensures col is even
        with open(self.input_file, 'w') as f:
            UtilityFunctions.flappybird_utils(f, rows, cols, initial_col=0, initial_row=rows // 2)
