"""
This file contains two functions, blind_search and heuristic_search.
"""

from queue import Queue
from .state import State

def blind_search(state):
    """
    This function solves the problem using BFS.
    """
    frontier = Queue()
    frontier.put(state)

    while not frontier.empty():
        s = frontier.get()
        if s.is_goal():
            return s
        
        for i in s.next_states():
            frontier.put(i)
        
    return None

def heuristic_search(state):
    """
    This function solves the problem by using xyz.
    """
    pass