"""
This file contains two functions, blind_search and heuristic_search.
"""

from queue import Queue
import heapq
from .state import *

def blind_search(state):
    """
    This function solves the problem using BFS.
    Return a goal state, if any, and the number of states explored.
    """

    state_space = Queue()
    state_space.put(state)
    count = 1

    while not state_space.empty():
        #get the next state
        s = state_space.get()

        #checking for goal state
        if s.is_goal():
            return s, count
        
        #generate new states if not a goal state
        for i in s.next_states():
            state_space.put(i)
            count += 1
    
    #no solution found
    return None, count

def heuristic_search(state):
    """
    This function solves the problem by using Best First Search.
    Return a goal state, if any, and the number of states explored.
    """
    state_space = []
    heapq.heappush(state_space, state)
    count = 1

    while not len(state_space) == 0:
        #get the best state available
        s = heapq.heappop(state_space)

        #checking for goal state
        if s.is_goal():
            return s, count
        
        #generating new states if not a goal state
        for i in s.next_states_heuristic():
            heapq.heappush(state_space, i)
            count += 1
    
    #no solution found
    return None, count