from extract.bbox import BBox
from extract.bbox_merge import bbox_merge
from extract.coordinate import Coordinate
import unittest


class TestBBoxMergeMergesCoordinatesCorrectly(unittest.TestCase):
    def setUp(self):
        bboxes = (
            BBox(Coordinate(466.681, 770.160), Coordinate(472.219, 801.755)),
            BBox(Coordinate(472.199, 771.160), Coordinate(477.736, 100.755)),
            BBox(Coordinate(524.519, 788.160), Coordinate(527.287, 70.755)),
        )

        self.merged_bbox = bbox_merge(bboxes)

    def test_upper_left_x(self):
        self.assertEqual(self.merged_bbox.upper_left_coordinate.x, 466.681)

    def test_upper_left_y(self):
        self.assertEqual(self.merged_bbox.upper_left_coordinate.y, 788.160)

    def test_lower_right_x(self):
        self.assertEqual(self.merged_bbox.lower_right_coordinate.x, 527.287)

    def test_lower_right_y(self):
        self.assertEqual(self.merged_bbox.lower_right_coordinate.y, 70.755)
