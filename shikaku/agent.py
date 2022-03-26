"""
This file contains two functions, blind_search and heuristic_search.
"""

from queue import Queue
import heapq
from .state import State

def blind_search(state):
    """
    This function solves the problem using BFS.
    """
    frontier = Queue()
    frontier.put(state)
    count = 1

    while not frontier.empty():
        s = frontier.get()
        if s.is_goal():
            print("States explored: ", count)
            return s
        
        for i in s.next_states():
            frontier.put(i)
            count += 1
        
    return None

def heuristic_search(state):
    """
    This function solves the problem by using Best First Search.
    """
    pq = []
    heapq.heappush(pq, state)
    count = 1
    while not len(pq) == 0:
        s = heapq.heappop(pq)
        if s.is_goal():
            print("States explored: ", count)
            return s
        
        for i in s.next_states():
            heapq.heappush(pq, i)
            count += 1
    
    return None