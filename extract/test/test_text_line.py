from extract.text_line import get_text_line_from_xml_element
import xml.etree.ElementTree as ET

s = """<textline bbox="459.840,753.697,521.235,765.210">
<text font="Arial-BoldMT" bbox="459.840,753.697,462.075,765.210" colourspace="ICCBased" ncolour="[0]" size="11.513">I</text>
<text font="Arial-BoldMT" bbox="462.120,753.697,467.483,765.210" colourspace="ICCBased" ncolour="[0]" size="11.513">S</text>
<text font="Arial-BoldMT" bbox="467.402,753.697,472.765,765.210" colourspace="ICCBased" ncolour="[0]" size="11.513">S</text>
<text font="Arial-BoldMT" bbox="472.802,753.697,478.607,765.210" colourspace="ICCBased" ncolour="[0]" size="11.513">N</text>
<text font="Arial-BoldMT" bbox="478.562,753.697,480.797,765.210" colourspace="ICCBased" ncolour="[0]" size="11.513"> </text>
<text font="ArialMT" bbox="480.840,754.107,485.310,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975">1</text>
<text font="ArialMT" bbox="485.278,754.107,489.748,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975">3</text>
<text font="ArialMT" bbox="489.716,754.107,494.186,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975">2</text>
<text font="ArialMT" bbox="494.154,754.107,498.624,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975">2</text>
<text font="ArialMT" bbox="498.600,754.107,501.277,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975">-</text>
<text font="ArialMT" bbox="501.240,754.107,505.710,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975">0</text>
<text font="ArialMT" bbox="505.678,754.107,510.148,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975">3</text>
<text font="ArialMT" bbox="510.116,754.107,514.586,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975">3</text>
<text font="ArialMT" bbox="514.554,754.107,519.024,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975">0</text>
<text font="ArialMT" bbox="519.000,754.107,521.235,765.082" colourspace="ICCBased" ncolour="[0]" size="10.975"> </text>
<text>
</text>
</textline>"""

def test_get_text_line_from_xml_element():
    t = get_text_line_from_xml_element(ET.fromstring(s))
    assert len(t.texts) == 16


def test_text_line_compact_tests():
    x = get_text_line_from_xml_element(ET.fromstring(s))

    x.compact_texts()

    assert len(x.texts) == 2

    assert x.texts[0].attr['font'] == 'Arial-BoldMT'
    assert x.texts[0].attr['size'] == '11.513'
    assert x.texts[0].bbox.upper_left_coordinate.x == 459.840
    assert x.texts[0].bbox.upper_left_coordinate.y == 753.697
    assert x.texts[0].bbox.lower_right_coordinate.x == 480.797
    assert x.texts[0].bbox.lower_right_coordinate.y == 765.210
    assert x.texts[0].contents == 'ISSN '

    assert x.texts[1].attr['font'] == 'ArialMT'
    assert x.texts[1].attr['size'] == '10.975'
    assert x.texts[1].bbox.upper_left_coordinate.x == 480.840
    assert x.texts[1].bbox.upper_left_coordinate.y == 754.107
    assert x.texts[1].bbox.lower_right_coordinate.x == 521.235
    assert x.texts[1].bbox.lower_right_coordinate.y == 765.082
    assert x.texts[1].contents == '1322-0330 '
