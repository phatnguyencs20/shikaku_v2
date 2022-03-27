"""
This file contains the Shikaku class, which helps process the input file and redirect the solving process.
"""

from .state import State
from .agent import blind_search, heuristic_search
import numpy as np
import re
import time

class Shikaku:
    def __init__(self, filename):
        print("Loading puzzle...")
        with open(filename) as f:
            contents = f.read()
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line.split()) for line in contents)

        self.regions = []
        for i in range(self.height):
            line = contents[i].split()
            for j in range(self.width):
                try:
                    if re.match("[0-9]+", line[j]):
                        self.regions.append((i, j, int(line[j])))
                    elif re.match("[#-]+", line[j]):
                        continue
                    else:
                        raise Exception("Invalid puzzle!")
                except IndexError:
                    raise Exception("Invalid puzzle!")
        
        self.initial_state = State(np.full((self.height, self.width), -1), self.regions)
        self.goal_state = None
        self.solving_time = 0
        print("Puzzle loaded.\n")

    def draw(self, output_image):
        self.initial_state.draw(self.regions, output_image)

    def solve(self, heuristic=False, info=False, output_image=None):
        if heuristic:
            print("Solving using heuristic search...")
            start_time = time.time()
            self.goal_state = heuristic_search(self.initial_state)
            end_time = time.time()
            print("Solved!\n")
            self.solving_time = end_time - start_time
        else:
            print("Solving using blind search...")
            start_time = time.time()
            self.goal_state = blind_search(self.initial_state)
            end_time = time.time()
            print("Solved!\n")
            self.solving_time = end_time - start_time
        
        if info:
            print("Solving time: ", self.solving_time)
            if self.goal_state is not None:
                print("Solution found:")
                #print(self.goal_state.state)
            else:
                print("No solution.")
        
        if output_image is not None and self.goal_state is not None:
            self.goal_state.draw(self.regions, output_image)