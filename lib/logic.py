import os
import tool
import json
from lxml import etree
from io import BytesIO

PWD_PATH = os.getcwd()
OUTPUT_SEQUENCE_JSON=os.getenv('OUTPUT_SEQUENCE_JSON')

class Logic:
    def __init__(self, file):
        self.name_file = file

    def condition_test(self, xpath):
        tree = etree.parse(BytesIO(self.name_file), etree.HTMLParser())
        if tree.xpath(xpath):
            return True
        else:
            return False

    def test(self):
        results = {}
        file = tool.FileOparetion(OUTPUT_SEQUENCE_JSON)
        xpath_dict = json.loads(file.get_content())

        for key, x_path in xpath_dict.items():
            result = self.condition_test(x_path)
            results[key] = result
        
        return results
        