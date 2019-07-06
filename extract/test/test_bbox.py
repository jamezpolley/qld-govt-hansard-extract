from extract.bbox import BBoxMixin
import unittest


class TestBboxClass(BBoxMixin):
    """A test class to demonstrate BBoxFactoryMixin"""
    attr = {
        'bbox': '459.840,753.697,462.075,765.210'
    }


class TestBboxParsesCorrectly(unittest.TestCase):
    def setUp(self):
        self.bbox = TestBboxClass().bbox

    def test_upper_left_x(self):
        self.assertEqual(self.bbox.upper_left_coordinate.x, 459.84)

    def test_upper_left_y(self):
        self.assertEqual(self.bbox.upper_left_coordinate.y, 753.697)

    def test_lower_right_x(self):
        self.assertEqual(self.bbox.lower_right_coordinate.x, 462.075)

    def test_lower_right_y(self):
        self.assertEqual(self.bbox.lower_right_coordinate.y, 765.210)
