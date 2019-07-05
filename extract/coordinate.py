class Coordinate(object):
    """Represents x/y coordinates"""

    def __init__(self, x, y):
        self.x = x
        self.y = y


def upper_left_most_coordinate(coordinates):
    ys = []
    xs = []
    for coord in coordinates:
        xs.append(coord.x)
        ys.append(coord.y)

    return Coordinate(min(xs), max(ys))


def lower_right_most_coordinate(coordinates):
    ys = []
    xs = []
    for coord in coordinates:
        xs.append(coord.x)
        ys.append(coord.y)

    return Coordinate(max(xs), min(ys))