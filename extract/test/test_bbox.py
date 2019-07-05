from extract.bbox import BBoxMixin


class TestBboxClass(BBoxMixin):
    """A test class to demonstrate BBoxFactoryMixin"""
    attr = {
        'bbox': '459.840,753.697,462.075,765.210'
    }


def test_bbox_mixin():
    t = TestBboxClass()
    bb = t.bbox
    assert bb.upper_left_coordinate.x == 459.84
    assert bb.upper_left_coordinate.y == 753.697
    assert bb.lower_right_coordinate.x == 462.075
    assert bb.lower_right_coordinate.y == 765.21
