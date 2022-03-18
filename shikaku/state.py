from copy import deepcopy
from queue import Queue
from .colors import Colors
import numpy as np
import re

class State():
    def __init__(self, state, actions):
        self.state = state
        self.actions = actions


    @classmethod
    def get_rectangular_shape(cls, area):
        for i in range(1, area + 1):
            if area % i == 0:
                yield i, area // i


    def is_goal(self):
        return np.amin(self.state) > -1 and len(self.actions) == 0


    def next_states(self):
        if len(self.actions) > 0:
            action = self.actions[0]
            for h, w in State.get_rectangular_shape(action[2]):
                for i in range(h):
                    for j in range(w):
                        new_state = self.apply_to(h, w, i + action[0], j + action[1])
                        if new_state is not None:
                            yield new_state


    def apply_to(self, height, width, x_coord, y_coord):
        id = np.amax(self.state) + 1
        state = deepcopy(self.state)

        for i in range(x_coord + 1 - height, x_coord + 1):
            for j in range(y_coord + 1 - width, y_coord + 1):
                try:
                    if i >= 0 and j >= 0 and state[i][j] == -1:
                        state[i][j] = id
                    else:
                        return None
                except IndexError:
                    return None
        
        return State(state, self.actions[1:])


    def draw(self, filename):
        from PIL import Image, ImageDraw
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
                    fill = (0, 0, 0)
                else:
                    fill = Colors[self.state[i][j] % len(Colors)]
                
                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )
        
        img.save(filename)
