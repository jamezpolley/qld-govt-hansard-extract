import sys
import argparse
import xml.etree.ElementTree as ET
from extract.text_box import get_text_box_from_xml_element


def main():
    """Tool to parse XML fom the queensland government."""

    parser = argparse.ArgumentParser(description='Extract content')
    parser.add_argument(dest='path_to_xml', action='store', type=str)
    results = parser.parse_args()

    root = ET.parse(results.path_to_xml).getroot()
    # todo: iterate by page, have some mechanism to identify text boxes based on positional details and/or style:
    #  - to ignore header and footer content
    #  - to identify headers
    xml_elements = root.findall('.//textbox')
    for xml_element in xml_elements:
        tb = get_text_box_from_xml_element(xml_element)
        for text_line in tb:
            text_line.compact_texts()
            t = ''
            for text in text_line:
                if not text.is_blank_node():
                    t += text.contents

            if t.strip():
                print(t)


if __name__ == '__main__':
    sys.exit(main())

