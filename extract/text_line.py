from .text import Text, get_text_from_xml_element, text_attrs_styles_are_equal
from .bbox_merge import bbox_merge
import copy


class TextLine(object):
    """A class containing information from a <textline> node"""

    def __init__(self):
        self.texts = []
        self.attr = {}

    def add_text_child(self, text):
        self.texts.append(copy.deepcopy(text))

    """ compacts text nodes by their style attributes, merging their bboxes """
    def compact_texts(self):
        merged_texts = []
        ctext = Text()
        bboxes = []
        for text in self.texts:
            if text_attrs_styles_are_equal(copy.copy(ctext.attr), copy.copy(text.attr)) is False:
                # New style of text, finish up last iteration
                # Make new bbox
                if len(bboxes) > 0:
                    bbox = bbox_merge(*bboxes)
                    ctext.attr['bbox'] = "{},{},{},{}".format(
                        bbox.upper_left_coordinate.x,
                        bbox.upper_left_coordinate.y,
                        bbox.lower_right_coordinate.x,
                        bbox.lower_right_coordinate.y
                    )

                bboxes = [] # reset bboxes

                merged_texts.append(ctext)
                ctext = Text() # reset ctext
                ctext.attr = text.attr # Set the ctext attributes to be the current text node (copying styles etc)

            bboxes.append(text.bbox)
            ctext.contents += text.contents

        if len(merged_texts) > 0:
            merged_texts.pop(0)

        self.texts = merged_texts


def get_text_line_from_xml_element(xml_element):
    t = TextLine()
    t.attr = xml_element.attrib
    for text_node in xml_element.findall('./text'):
        t.add_text_child(get_text_from_xml_element(text_node))

    return t
