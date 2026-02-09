from UtilityFunctions import UtilityFunctions

# this class generates the basic test cases (test cases with fixed grid dimensions)
class BasicTestCases:
    def __init__(self, input_file):
        self.input_file = input_file
        
    def generate_openspace_testcase(self):
        with open(self.input_file, 'w') as f:
            f.write("[11,5]\n") 
            f.write("(0,0)\n") 
            f.write("(4,10) | (0,10)\n") 

    def generate_robotnav_testcase(self):
        with open(self.input_file, 'w') as f:
            f.write("[5,11]\n") 
            f.write("(0,1)\n") 
            f.write("(10,3) | (7,0)\n") 
            f.write("(2,0,2,2)\n(8,0,1,2)\n(10,0,1,1)\n(2,3,1,2)\n(3,4,3,1)\n(9,3,1,1)\n(8,4,2,1)")

    def generate_goalsurrounded_testcase(self):
        with open(self.input_file, 'w') as f:
            f.write("[5,11]\n")
            f.write("(10,2)\n")
            f.write("(5,3) | (3,0)\n")
            f.write("(5,2,1,1)\n(4,3,1,1)\n(6,2,1,3)\n(4,0,1,1)\n(2,1,2,1)")

    def generate_switzerland_testcase(self):
        with open(self.input_file, 'w') as f:
            f.write("[11,13]\n")
            f.write("(6,5)\n")
            f.write(" (6,10) | (12,5) | (6,0) | (0,5)\n")
            f.write("(5,0,1,5)\n(0,4,5,1)\n(7,0,1,5)\n(8,4,5,1)\n(0,6,5,1)\n(5,6,1,5)\n(7,6,1,5)\n(8,6,5,1)")

    def generate_x_testcase(self):
        with open(self.input_file, 'w') as f:
            f.write("[11,13]\n")
            f.write("(6,5)\n")
            f.write("(0,10) | (12,10) | (0,0) | (12,0) \n")
            f.write("(0,1,1,9)\n(1,2,1,7)\n(2,3,1,5)\n(3,4,1,3)\n(4,5,1,1)\n(8,5,1,1)\n(9,4,1,3)\n(10,3,1,5)\n(11,2,1,7)\n(12,1,1,9)\n(2,0,9,1)\n(3,1,7,1)\n(4,2,5,1)\n(5,3,3,1)\n(6,4,1,1)\n(6,6,1,1)\n(5,7,3,1)\n(4,8,5,1)\n(3,9,7,1)\n(2,10,9,1)")

    def generate_goalblocked_testcase(self):
        with open(self.input_file, 'w') as f:
            f.write("[5,11]\n")
            f.write("(10,2)\n")
            f.write("(5,3) | (3,0)\n")
            f.write("(5,2,1,1)\n(4,3,1,1)\n(6,2,1,3)\n(4,0,1,1)\n(2,1,2,1)\n(2,0,1,1)\n(5,4,1,1)")

    def generate_diverseobstacles_testcase(self):
        with open(self.input_file, 'w') as f:
            f.write("[11,15]\n")
            f.write("(0,5)\n")
            f.write("(13,0) | (14,8)\n")
            f.write("(0,4,4,1)\n(3,5,1,1)\n(0,8,2,2)\n(2,0,4,3)\n(3,8,2,1)\n(3,7,3,1)\n(5,5,2,3)\n(7,0,5,4)\n(8,7,6,2)\n(4,10,5,1)\n(6,9,1,1)\n(10,5,5,1)\n(13,2,2,3)\n(13,9,2,2)\n(8,5,1,2)")

    def generate_flappybird_testcase(self):
        with open(self.input_file, 'w') as f:
            f.write("[9,20]\n")
            f.write("(0,4)\n")
            f.write("(19,8) | (19,4) | (19,0)\n")
            f.write("(0,0,1,4)\n(0,5,1,4)\n(2,0,1,3)\n(2,4,1,5)\n(4,0,1,7)\n(4,8,1,1)\n(6,0,1,5)\n(6,6,1,3)\n(8,1,1,8)\n(10,0,1,3)\n(10,4,1,5)\n(12,0,1,5)\n(12,6,1,3)\n(14,0,1,8)\n(16,0,1,4)\n(16,5,1,4)\n(18,1,1,3)\n(18,5,1,3)")

    def generate_maze_testcase(self):
        with open(self.input_file, 'w') as f:
            f.write("[19,19]\n")
            f.write("(9,9)\n")
            f.write("(1,17) | (17,1)\n")
            f.write("(0,0,1,19)\n(1,0,18,1)\n(0,18,19,1)\n(18,0,1,19)\n(2,1,1,2)\n(1,4,1,1)\n(1,6,2,1)\n(1,14,2,1)\n(4,2,3,1)\n(6,3,1,2)\n(3,4,1,1)\n(4,3,1,5)\n(2,8,9,1)\n(10,6,1,2)\n(2,9,1,4)\n(2,16,11,1)\n(12,14,1,2)\n(13,14,4,1)\n(16,12,1,2)\n(14,17,1,1)\n(14,16,3,1)\n(16,10,2,1)\n(15,8,3,1)\n(14,6,1,7)\n(10,12,4,1)\n(10,13,1,3)\n(16,2,1,5)\n(12,4,4,1)\n(12,5,1,6)\n(8,10,4,1)\n(8,11,1,4)\n(4,10,1,5)\n(6,9,1,4)\n(5,14,3,1)\n(8,1,1,6)\n(6,6,2,1)\n(9,4,2,1)\n(10,2,1,2)\n(11,2,4,1)")

    def generate_randomobstacles_testcase(self): #semi-automated (obstacles are randomized, but having a fixed grid dimension)
        with open(self.input_file, 'w') as f:
            rows = 15
            cols = 13
            f.write(f"[{rows},{cols}]\n")
            f.write("(0,0)\n")
            f.write("(12,14)\n")
            obstacles = UtilityFunctions.randomized_obstacles((rows, cols))
            for obstacle in obstacles:
                f.write(f"({obstacle[1]},{obstacle[0]},{obstacle[2]},{obstacle[3]})\n")