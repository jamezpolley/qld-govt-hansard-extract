class BBox:
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0


class BBoxFactoryMixin(object):
    def get_bbox(self):
        b = BBox()
        p = self.attr['bbox'].split(",")
        b.x0 = float(p[0])
        b.y0 = float(p[1])
        b.x1 = float(p[2])
        b.y1 = float(p[3])
        return b
