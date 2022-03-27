def get_rectangular_shape(area):
    """
    This function receives an area as input and return a
    generator of possible rectangular shapes.
    """
    for i in range(1, area + 1):
        if area % i == 0:
            yield i, area // i

import numpy as np

reachability = np.array([1, 2, 3, 4])
b = int(np.where(reachability == 2)[0])
print(b)