import json

class ReportAndData:

    execution_data = {
        "report_generation": {}
        }

    test_case_execution_times = {
        # DFS is faster than BFS (DFS uses less time)
        # GBFS is faster than A* (GBFS uses less time)
        "OpenSpace": {
            "BFS": {"min_time": 0.05, "max_time": 0.15}, 
            "DFS": {"min_time": 0.01, "max_time": 0.1}, 
            "DL-DFS": {"min_time": 0.005, "max_time": 0.05}, 
            "GBFS": {"min_time": 0.005, "max_time": 0.045}, 
            "A*": {"min_time": 0.005, "max_time": 0.055}, 
            "DL-A*": {"min_time": 0.003, "max_time": 0.048}, 
        },

        # DFS is faster than BFS (DFS uses less time)
        # GBFS is faster than A* (GBFS uses less time) 
        "RobotNav": {
            "BFS": {"min_time": 0.015, "max_time": 0.2}, 
            "DFS": {"min_time": 0.01, "max_time": 0.15},  
            "DL-DFS": {"min_time": 0.005, "max_time": 0.075}, 
            "GBFS": {"min_time": 0.001, "max_time": 0.05},  
            "A*": {"min_time": 0.015, "max_time": 0.06}, 
            "DL-A*": {"min_time": 0.015, "max_time": 0.05},
        },

        # DFS is faster than BFS (DFS uses less time)
        # GBFS is faster than A* (GBFS uses less time)
        "GoalSurrounded": {
            "BFS": {"min_time": 0.04, "max_time": 0.2}, 
            "DFS": {"min_time": 0.03, "max_time": 0.15}, 
            "DL-DFS": {"min_time": 0.025, "max_time": 0.1}, 
            "GBFS": {"min_time": 0.02, "max_time": 0.07}, 
            "A*": {"min_time": 0.015, "max_time": 0.08}, 
            "DL-A*": {"min_time": 0.01, "max_time": 0.075}, 
        },

        # DFS is faster than BFS (DFS uses less time)
        # GBFS is faster than A* (GBFS uses less time)
        "Switzerland": {
            "BFS": {"min_time": 0.015, "max_time": 0.1}, 
            "DFS": {"min_time": 0.005, "max_time": 0.05}, 
            "DL-DFS": {"min_time": 0.005, "max_time": 0.04}, 
            "GBFS": {"min_time": 0.004, "max_time": 0.03}, 
            "A*": {"min_time": 0.001, "max_time": 0.05}, 
            "DL-A*": {"min_time": 0.001, "max_time": 0.045}, 
        },

        # DFS is faster than BFS (DFS uses less time)
        # GBFS is faster than A* (GBFS uses less time)
        "X": {
            "BFS": {"min_time": 0.05, "max_time": 0.35}, 
            "DFS": {"min_time": 0.01, "max_time": 0.3}, 
            "DL-DFS": {"min_time": 0.01, "max_time": 0.25}, 
            "GBFS": {"min_time": 0.005, "max_time": 0.08}, 
            "A*": {"min_time": 0.05, "max_time": 0.25}, 
            "DL-A*": {"min_time": 0.04, "max_time": 0.2}, 
        },

        # BFS is FASTER than DFS (BFS uses LESS time)
        # GBFS is faster than A* (GBFS uses less time)
        "DiverseObstacles": {
            "BFS": {"min_time": 0.04, "max_time": 0.55}, 
            "DFS": {"min_time": 0.05, "max_time": 0.65}, 
            "DL-DFS": {"min_time": 0.05, "max_time": 0.6}, 
            "GBFS": {"min_time": 0.01, "max_time": 0.25}, 
            "A*": {"min_time": 0.05, "max_time": 0.35}, 
            "DL-A*": {"min_time": 0.05, "max_time": 0.3}, 
        },

        # BFS is FASTER than DFS (BFS uses LESS time)
        # GBFS is faster than A* (GBFS uses less time)
        "FlappyBird": {
            "BFS": {"min_time": 0.05, "max_time": 0.55}, 
            "DFS": {"min_time": 0.1, "max_time": 0.65}, 
            "DL-DFS": {"min_time": 0.05, "max_time": 0.6}, 
            "GBFS": {"min_time": 0.07, "max_time": 0.3}, 
            "A*": {"min_time": 0.06, "max_time": 0.35}, 
            "DL-A*": {"min_time": 0.06, "max_time": 0.34}, 
        },

        # BFS is FASTER than DFS (BFS uses LESS time)
        # A* is FASTER than GBFS (A* uses LESS TIME)
        "Maze": {
            "BFS": {"min_time": 0.05, "max_time": 0.6}, 
            "DFS": {"min_time": 0.15, "max_time": 1.5}, 
            "DL-DFS": {"min_time": 0.15, "max_time": 1.3}, 
            "GBFS": {"min_time": 0.07, "max_time": 0.55}, 
            "A*": {"min_time": 0.05, "max_time": 0.45}, 
            "DL-A*": {"min_time": 0.05, "max_time": 0.4}, 
        },

        # overall,
        # DL-DFS & DL-A* are faster than their original DFS and A* (DL searches use less time)
        # informed searches (GBFS, A*, DL-A*) overall use less time than informed searchs (BFS, DFS, DL-DFS)
    }

    @staticmethod # this method adds the data collected into the JSON file
    def add_report_data(txt_filename, data, test_case, algorithm):
        if txt_filename not in ReportAndData.execution_data["report_generation"]:
            ReportAndData.execution_data["report_generation"][txt_filename] = {}

        if "searches" not in ReportAndData.execution_data["report_generation"][txt_filename]:
            ReportAndData.execution_data["report_generation"][txt_filename]["searches"] = []

        existing_data = {}
        try:
            with open('report.json', 'r') as report_file:
                existing_data = json.load(report_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass

        if "report_generation" in existing_data:
            if txt_filename in existing_data["report_generation"]:
                if "searches" in existing_data["report_generation"][txt_filename]:
                    ReportAndData.execution_data["report_generation"][txt_filename]["searches"] = existing_data["report_generation"][txt_filename]["searches"]

        # Check if execution time falls within the specified range
        min_time = ReportAndData.test_case_execution_times.get(test_case, {}).get(algorithm, {}).get("min_time", None)
        max_time = ReportAndData.test_case_execution_times.get(test_case, {}).get(algorithm, {}).get("max_time", None)
        if min_time is not None and max_time is not None:
            execution_time = data.get("execution time")
            if execution_time is not None and min_time <= execution_time <= max_time:
                message = "Execution time within expected range. Pathfinding algorithm likely performed efficiently."
            else:
                message = "Execution time outside expected range. While the algorithm found the path, there were slight variations in execution time across runs."
            data["execution time message"] = message

        if data["goal found"]:
            search_entry = {
                "test_case_type": test_case,
                "search_data": data,
            }
            # Check if the test case should have time execution range
            if test_case not in ["RandomObstacles", "OpenSpace-Small", "OpenSpace-Medium", "OpenSpace-Large",
                                "Switzerland-Small", "Switzerland-Medium", "Switzerland-Large", "X-Small",
                                "X-Medium", "X-Large", "FlappyBird-Small", "FlappyBird-Medium", "FlappyBird-Large",
                                "RandomObstacles-Small", "RandomObstacles-Medium", "RandomObstacles-Large"]:
                search_entry["execution_times"] = {
                    algorithm: {
                        "min_time": ReportAndData.test_case_execution_times.get(test_case, {}).get(algorithm, {}).get("min_time", None),
                        "max_time": ReportAndData.test_case_execution_times.get(test_case, {}).get(algorithm, {}).get("max_time", None),
                        "message": message
                    }
                }
            ReportAndData.execution_data["report_generation"][txt_filename]["searches"].append(search_entry)
        else:
            ReportAndData.execution_data["report_generation"][txt_filename]["searches"].append({
                "test_case_type": test_case,
                "search_data": data
            })

        if algorithm == "DL-DFS" or algorithm == "DL-A*":
            if "max_depth" in ReportAndData.execution_data["report_generation"][txt_filename]:
                del ReportAndData.execution_data["report_generation"][txt_filename]["max_depth"]

    @staticmethod # this method writes the report into the JSON file
    def write_report():
        with open('report.json', 'w') as report_file:
            json.dump(ReportAndData.execution_data, report_file, indent=4)
