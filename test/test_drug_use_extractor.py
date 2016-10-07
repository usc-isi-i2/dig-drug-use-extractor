import sys
import time
import os
import unittest

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

from digExtractor.extractor import Extractor
from digExtractor.extractor_processor import ExtractorProcessor
from digDrugUseExtractor.drug_use_extractor import DrugUseExtractor

class TestDrugUseExtractorMethods(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_drug_use_extractor(self):
        doc = {'content': 'she is on drugs a dope whores and a junkie who is on some heavy drugs and does drugs and an adict, smells bad', 'b': 'world'}

        extractor = DrugUseExtractor().set_metadata({'extractor': 'drug'})
        extractor_processor = ExtractorProcessor().set_input_fields(['content']).set_output_field('extracted').set_extractor(extractor)
        updated_doc = extractor_processor.extract(doc)
        self.assertEqual(updated_doc['extracted']['value'], ['dope whores', 'junkie', 'adict', 'on drugs', 'on some heavy drugs', 'does drugs'])

    

if __name__ == '__main__':
    unittest.main()



