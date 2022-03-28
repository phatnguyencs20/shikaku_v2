"""
This file contains the definition of a state, as well as a transition.
"""

from copy import deepcopy
from .colors import Colors
import numpy as np
import math

class State():
    
    def __init__(self, state, actions):
        self.state = state
        self.actions = actions
        self.evaluation = None
    

    def __eq__(self, other):
        """
        Rather than checking the equality between two states,
        we are comparing their values against each other.
        """
        return self.evaluate() == other.evaluate()


    def __lt__(self, other):
        """
        Rather than checking the equality between two states,
        we are comparing their values against each other.
        """
        return self.evaluate() < other.evaluate()


    @classmethod
    def get_rectangular_shape(cls, area):
        """
        This function receives an area as input and return a
        generator of possible rectangular shapes.
        """
        for i in range(1, area + 1):
            if area % i == 0:
                yield i, area // i


    def is_goal(self):
        """
        A goal state is a state that all cells are filled.
        """
        return np.amin(self.state) > -1


    def evaluate(self):
        """
        Evaluate a particular state.
        An evaluation to 0 is the best - goal state, while larger values mean worse.
        """
        if self.evaluation is None:
            if len(self.actions) == 0:
                #this is probably a goal state
                #but still require double check for each cell.
                self.evaluation = 0
                return self.evaluation
            
            #greedy algorithm: return the amount of not filled cells.
            self.evaluation = (self.state == -1).sum()
        return self.evaluation


    def next_states(self):
        """
        This function returns a generator of new states resulting from
        taking an action.
        """
        if len(self.actions) > 0:
            action = self.actions[0]

            for h, w in State.get_rectangular_shape(action[2]):
                for i in range(h):
                    for j in range(w):
                        new_state = self.apply_to(h, w, i + action[0], j + action[1])
                        if new_state is not None:
                            yield new_state
    

    def next_states_heuristic(self):
        """
        This function returns a generator of new states resulting from
        taking an action.
        """
        if len(self.actions) > 0:
            index = -1
            max_area = 0
            for id, action in enumerate(self.actions):
                if action[2] > max_area:
                    max_area = action[2]
                    index = id
            
            self.actions[index], self.actions[0] = self.actions[0], self.actions[index]
            action = self.actions[0]

            for h, w in State.get_rectangular_shape(action[2]):
                for i in range(h):
                    for j in range(w):
                        new_state = self.apply_to(h, w, i + action[0], j + action[1])
                        if new_state is not None:
                            yield new_state


    def apply_to(self, height, width, x_coord, y_coord):
        """
        This function applies an action to a state (resulting a new one)
        without modifying the old state.
        """
        id = np.amax(self.state) + 1    #id of the new region being solved
        state = deepcopy(self.state)
        unsolved = self.actions[1:]    #updating the list of remaining actions

        for i in range(x_coord + 1 - height, x_coord + 1):
            for j in range(y_coord + 1 - width, y_coord + 1):
                    try:
                        if i >= 0 and j >= 0 and state[i][j] == -1:
                            state[i][j] = id
                        else:
                            #cell is already taken by other regions
                            return None
                    except IndexError:
                        #cell index is out of the board
                        return None
                        
        for m, n, area in unsolved:
            if state[m][n] != -1:
                #cell must belong to (m, n, area) - not this one (this cell is already marked)
                return None
        
        #return a new valid state
        return State(state, unsolved)


    def draw(self, regions, filename):
        """
        Draw a particular state given a list of regions, save image as <filename>.
        """
        from PIL import Image, ImageFont, ImageDraw
        cell_size = 50
        cell_border = 2

        img = Image.new(
            "RGBA",
            (cell_size * len(self.state[0]) + int(0.5 * cell_border), cell_size * len(self.state) + int(0.5 * cell_border)),
            "black"
            )

        draw = ImageDraw.Draw(img)

        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] == -1:
                    fill = (255, 255, 255)
                else:
                    fill = Colors[self.state[i][j] % len(Colors)]
                
                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )

        font1 = ImageFont.truetype("arial.ttf", 30)
        font2 = ImageFont.truetype("arial.ttf", 25)

        for x, y, area in regions:
            if area < 10:
                draw.text(
                    (y * cell_size + 17, x * cell_size + 8),
                    str(area),
                    font=font1, 
                    fill='black', 
                    align='center'
                )
            else:
                draw.text(
                    (y * cell_size + 10, x * cell_size + 11),
                    str(area),
                    font=font2,
                    fill='black',
                    align='center'
                )
        
        img.save(filename)