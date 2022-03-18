from queue import Queue
from .state import State

def blind_search(state: State):
    frontier = Queue()
    frontier.put(state)

    while not frontier.empty():
        s = frontier.get()
        if s.is_goal():
            return s
        
        for i in s.next_states():
            frontier.put(i)
        
    return None