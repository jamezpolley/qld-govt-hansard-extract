from .coordinate import lower_right_most_coordinate, upper_left_most_coordinate
from .bbox import BBox


def bbox_merge(bboxes):
    upper_left_coordinates = []
    lower_right_coordinates = []
    for bbox in bboxes:
        try:
            upper_left_coordinates.append(bbox.upper_left_coordinate)
            lower_right_coordinates.append(bbox.lower_right_coordinate)
        except AttributeError:
            pass

    upper_left_coordinate = upper_left_most_coordinate(upper_left_coordinates)
    lower_right_coordinate = lower_right_most_coordinate(lower_right_coordinates)

    return BBox(upper_left_coordinate, lower_right_coordinate)
