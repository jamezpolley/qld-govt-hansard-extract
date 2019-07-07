from extract.coordinate import Coordinate, upper_left_most_coordinate, lower_right_most_coordinate
import unittest


class TestUpperLeftMostCoordinate(unittest.TestCase):
    def setUp(self):
        coordinates = [
            Coordinate(466.681, 788.160),
            Coordinate(472.199, 788.160),
            Coordinate(477.717, 788.160),
            Coordinate(480.475, 788.160),
            Coordinate(488.876, 788.160),
            Coordinate(494.516, 788.160),
            Coordinate(499.316, 788.160),
            Coordinate(502.195, 788.160),
            Coordinate(507.713, 788.160),
            Coordinate(513.231, 788.160),
            Coordinate(518.870, 788.160),
            Coordinate(524.519, 788.160),
        ]
        self.coord = upper_left_most_coordinate(coordinates)

    def test_x(self):
        self.assertEqual(self.coord.x, 466.681)

    def test_y(self):
        self.assertEqual(self.coord.y, 788.160)


class TestLowerRightMostCoordinate(unittest.TestCase):
    def setUp(self):
        coordinates = (
            Coordinate(472.219, 801.755),
            Coordinate(477.736, 801.755),
            Coordinate(480.485, 801.755),
            Coordinate(488.772, 801.755),
            Coordinate(494.413, 801.755),
            Coordinate(499.496, 801.755),
            Coordinate(502.085, 801.755),
            Coordinate(507.733, 801.755),
            Coordinate(513.251, 801.755),
            Coordinate(518.769, 801.755),
            Coordinate(524.408, 801.755),
            Coordinate(527.287, 801.755),
        )
        self.coord = lower_right_most_coordinate(coordinates)

    def test_x(self):
        self.assertEqual(self.coord.x, 527.287)

    def test_y(self):
        self.assertEqual(self.coord.y, 801.755)
