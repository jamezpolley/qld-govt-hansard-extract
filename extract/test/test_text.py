from extract.text import get_text_from_xml_element, text_attrs_styles_are_equal
import xml.etree.ElementTree as ET
import unittest


class TestGetTextFromXmlElement(unittest.TestCase):
    def setUp(self):
        s = """
                <text font="ArialMT" bbox="519.000,754.107,521.235,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975">Y</text>
        """
        self.text = get_text_from_xml_element(ET.fromstring(s))

    def test_contents_retained(self):
        self.assertEqual(self.text.contents, 'Y')

    def test_font_retained(self):
        self.assertEqual(self.text.attr['font'], 'ArialMT')

    def test_bbox_retained(self):
        self.assertEqual(self.text.attr['bbox'], '519.000,754.107,521.235,765.082')

    def test_colour_space_retained(self):
        self.assertEqual(self.text.attr['colourspace'], 'ICCBased')

    def test_size_retained(self):
        self.assertEqual(self.text.attr['size'], '10.975')


class TestTextAttrsStylesAreEqual(unittest.TestCase):
    def test_text_attrs_styles_are_equal_true_when_same(self):
        attr1 = {
            'font': "ArialMT",
            'bbox':  "519.000,754.107,521.235,765.082",
            'colourspace': "ICCBased",
            'ncolour':  "[0]",
            'size':  "10.975",
        }
        attr2 = {
            'font': "ArialMT",
            'bbox':  "519.000,754.107,521.235,765.082",
            'colourspace': "ICCBased",
            'ncolour':  "[0]",
            'size':  "10.975",
        }
        self.assertTrue(text_attrs_styles_are_equal(attr1, attr2))

    def test_text_attrs_styles_are_equal_false_when_diff(self):
        attr1 = {
            'font': "ArialMT",
            'bbox':  "519.000,754.107,521.235,765.082",
            'colourspace': "ICCBased",
            'ncolour':  "[0]",
            'size':  "10.974",
        }
        attr2 = {
            'font': "Arial",
            'bbox':  "519.000,754.107,521.235,765.082",
            'colourspace': "ICCBased",
            'ncolour':  "[0]",
            'size':  "10.975",
        }
        self.assertFalse(text_attrs_styles_are_equal(attr1, attr2))

    def test_text_attrs_styles_are_equal_true_when_only_bbox_diff(self):
        attr1 = {
            'font': "ArialMT",
            'bbox':  "519.000,754.107,52.235,765.082",
            'colourspace': "ICCBased",
            'ncolour':  "[0]",
            'size':  "10.975",
        }
        attr2 = {
            'font': "ArialMT",
            'bbox':  "519.000,754.107,521.235,765.082",
            'colourspace': "ICCBased",
            'ncolour':  "[0]",
            'size':  "10.975",
        }
        self.assertTrue(text_attrs_styles_are_equal(attr1, attr2))