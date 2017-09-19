from etl import extract, transform, load
import unittest

test_file_path = './data/OPEC_ORB_TEST.csv'

extract_data = []

transform_data = []

class MyTest(unittest.TestCase):
    def test_extract(self):
        opec_orb_data = extract(test_file_path)
        assert(extract_data==opec_orb_data)

    def test_transform(self):
        opec_orb_transform_data = transform(extract_data)
        assert(transform_data==opec_orb_transform_data)

    def test_load(self):
        assert(1==0)

if __name__ == '__main__':
    unittest.main()
