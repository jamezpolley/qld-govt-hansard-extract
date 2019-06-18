from .text import Text, get_text_from_xml_element, text_attrs_styles_are_equal
import copy


class TextLine():
    """A class containing information from a <textline> node"""
    attr = {}

    texts = []

    def __init__(self):
        self.texts = []
        self.attr = {}

    def add_text_child(self, text):
        self.texts.append(text)

    """ compacts text nodes by their style attributes """
    def compact_texts(self):
        merged_texts = []
        ctext = Text()
        for text in self.texts:
            if text_attrs_styles_are_equal(ctext.attr, text.attr) is False:
                merged_texts.append(copy.deepcopy(ctext))
                ctext = Text()
                ctext.attr = text.attr

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
