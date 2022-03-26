def get_rectangular_shape(area):
    """
    This function receives an area as input and return a
    generator of possible rectangular shapes.
    """
    for i in range(1, area + 1):
        if area % i == 0:
            yield i, area // i

print(get_rectangular_shape(5))