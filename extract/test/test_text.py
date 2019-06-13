from extract.text import get_text_from_xml_element, text_attrs_styles_are_equal
import xml.etree.ElementTree as ET

s = """
<text font="ArialMT" bbox="519.000,754.107,521.235,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975">Y</text>
"""


def test_get_text_from_xml_element():
    t = get_text_from_xml_element(ET.fromstring(s))
    assert t.contents == 'Y'
    assert t.attr['font'] == 'ArialMT'
    assert t.attr['bbox'] == '519.000,754.107,521.235,765.082'
    assert t.attr['colourspace'] == 'ICCBased'
    assert t.attr['size'] == '10.975'


def test_text_attrs_styles_are_equal_true_when_same():
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
    assert text_attrs_styles_are_equal(attr1, attr2) is True

def test_text_attrs_styles_are_equal_false_when_diff():
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
    assert text_attrs_styles_are_equal(attr1, attr2) is False


def test_text_attrs_styles_are_equal_true_when_only_bbox_diff():
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
    assert text_attrs_styles_are_equal(attr1, attr2) is True