from .coordinate import Coordinate


class BBox(object):
    """Represents a bounding box."""

    def __init__(self, upper_left_coordinate, lower_right_coordinate):
        """Create a BBox from two coordinate pairs.
        Returns:
        BBox object
        """
        self.upper_left_coordinate = upper_left_coordinate
        self.lower_right_coordinate = lower_right_coordinate


class BBoxMixin(object):
    """Mixin class for node types which contain a BBox.

    The coordinates for the bbox should be contained in
        self.attr['bbox']. The coordinates are assumed to be in the form
        of a comma-seperated string like so: "x0, y0, x1, y1"

    Adds a bbox read-only bbox property.
    
    (See https://docs.python.org/3/library/functions.html#property for more about
    properties, and a description of how to make this property read/write if desired)."""

    @property
    def bbox(self):
        points = self.attr['bbox'].split(",")

        # All coordinates are cast to floats, which potentially introduces a loss of precision.
        # TODO: investigate whether it would make more sense to use decimal.Decimal to preserve precision

        upper_left_coordinate = Coordinate(float(points[0]), float(points[1]))
        lower_right_coordinate = Coordinate(float(points[2]), float(points[3]))
        box = BBox(upper_left_coordinate, lower_right_coordinate)
        return box