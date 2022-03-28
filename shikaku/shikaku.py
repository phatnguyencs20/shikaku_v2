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

        #store width and height of the puzzle
        self.height = len(contents)
        self.width = max(len(line.split()) for line in contents)

        #store all regions, serving for drawing
        self.regions = []
        for i in range(self.height):
            line = contents[i].split()
            for j in range(self.width):
                try:
                    if re.match("[0-9]+", line[j]):
                        self.regions.append((i, j, int(line[j])))
                    elif re.match("[-]+", line[j]):
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

    def solve(self, heuristic=False, info=False, log=None, output_image=None):
        if heuristic:
            start_time = time.time()
            self.goal_state, states_explored = heuristic_search(self.initial_state)
            end_time = time.time()
            self.solving_time = end_time - start_time
        else:
            start_time = time.time()
            self.goal_state, states_explored = blind_search(self.initial_state)
            end_time = time.time()
            self.solving_time = end_time - start_time
        
        if log is not None:
            with open(log, 'w') as f:
                f.write("Puzzle size is: " + str(len(self.initial_state.state)) + "x" + str(len(self.initial_state.state[0])) + '\n')
                f.write("Number of regions: " + str(len(self.initial_state.actions)) + '\n')
                f.write("States explored: " + str(states_explored) + '\n')
                f.write("Time taken to solve: " + str(self.solving_time) + '\n')
                if self.goal_state is not None:
                    f.write("Solution found.")
                else:
                    f.write("No solution.")
        
        if info:
            print("Solving time: ", self.solving_time)
            if self.goal_state is not None:
                print("Solution found.")
            else:
                print("No solution.")
        
        if output_image is not None and self.goal_state is not None:
            self.goal_state.draw(self.regions, output_image)