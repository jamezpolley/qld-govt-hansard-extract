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
    textboxes = root.findall('.//textbox')
    for textbox in textboxes:
        tb = get_text_box_from_xml_element(textbox)
        for text_line in tb.text_lines:
            text_line.compact_texts()
            for text in text_line.texts:
                print(text.contents)

    pass


if __name__ == '__main__':
    sys.exit(main())

