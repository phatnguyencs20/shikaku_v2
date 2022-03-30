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
        self.solving_time_blind = 0
        self.solving_time_heuristics = 0

        print("Puzzle loaded.\n")

    def draw(self, output_image):
        self.initial_state.draw(self.regions, output_image)

    def solve(self, log=None, benchmark=None, output_image=None):

        #time tracking for heuristic search
        start_time = time.time()
        self.goal_state, states_explored_heuristic = heuristic_search(self.initial_state)
        end_time = time.time()
        self.solving_time_heuristic = end_time - start_time

        #time tracking for blind search
        start_time = time.time()
        self.goal_state, states_explored_blind = blind_search(self.initial_state)
        end_time = time.time()
        self.solving_time_blind = end_time - start_time
        
        if log is not None:
            with open(log, 'w') as f:
                f.write("Puzzle size is: " + str(len(self.initial_state.state)) + "x" + str(len(self.initial_state.state[0])) + '\n')
                f.write("Number of regions: " + str(len(self.initial_state.actions)) + '\n\n')

                f.write("Heuristic search: \n")
                f.write("States explored: " + str(states_explored_heuristic) + '\n')
                f.write("Time taken to solve: " + str(self.solving_time_heuristic) + '\n\n')

                f.write("Blind search: \n")
                f.write("States explored: " + str(states_explored_blind) + '\n')
                f.write("Time taken to solve: " + str(self.solving_time_blind) + '\n\n')

                if self.goal_state is not None:
                    f.write("Solution found.\n")
                    f.write(str(self.goal_state.state))
                else:
                    f.write("No solution.")
        
        if output_image is not None and self.goal_state is not None:
            self.goal_state.draw(self.regions, output_image)
        
        if benchmark is not None:
            return self.height, self.width, self.solving_time_heuristic, states_explored_heuristic, self.solving_time_blind, states_explored_blind, (self.goal_state is not None)