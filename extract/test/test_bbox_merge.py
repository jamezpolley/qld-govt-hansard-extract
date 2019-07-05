from extract.bbox import BBox
from extract.bbox_merge import bbox_merge
from extract.coordinate import Coordinate


def test_bbox_merge():
    bboxes = [
        BBox(Coordinate(466.681,788.160),Coordinate(472.219,801.755)),
        BBox(Coordinate(472.199,788.160),Coordinate(477.736,801.755)),
        BBox(Coordinate(477.717,788.160),Coordinate(480.485,801.755)),
        BBox(Coordinate(480.475,788.160),Coordinate(488.772,801.755)),
        BBox(Coordinate(488.876,788.160),Coordinate(494.413,801.755)),
        BBox(Coordinate(494.516,788.160),Coordinate(499.496,801.755)),
        BBox(Coordinate(499.316,788.160),Coordinate(502.085,801.755)),
        BBox(Coordinate(502.195,788.160),Coordinate(507.733,801.755)),
        BBox(Coordinate(507.713,788.160),Coordinate(513.251,801.755)),
        BBox(Coordinate(513.231,788.160),Coordinate(518.769,801.755)),
        BBox(Coordinate(518.870,788.160),Coordinate(524.408,801.755)),
        BBox(Coordinate(524.519,788.160),Coordinate(527.287,801.755)),
    ]
    merged_bbox = bbox_merge(*bboxes)

    assert merged_bbox.upper_left_coordinate.x == 466.681
    assert merged_bbox.upper_left_coordinate.y == 788.160
    assert merged_bbox.lower_right_coordinate.x == 527.287
    assert merged_bbox.lower_right_coordinate.y == 801.755
