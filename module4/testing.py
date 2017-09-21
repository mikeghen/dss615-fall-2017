from etl import extract, transform
import unittest

test_file_path = './data/OPEC_ORB_TEST.csv'

extract_data = [
('9/18/17', '53.78'),
('9/15/17', '53.64'),
('9/14/17', '53.63'),
('9/13/17', '52.92'),
('9/12/17', '52.08'),
('9/11/17', '51.82'),
('9/8/17', '52.53'),
('9/7/17', '52.48'),
('9/6/17', '52.04')]

transform_data = [
('9/18/17', 0),
('9/15/17', 0),
('9/14/17', 0),
('9/13/17', 0),
('9/12/17', 0),
('9/11/17', 52.818),
('9/8/17', 52.596000000000004),
('9/7/17', 52.366),
('9/6/17', 52.19)]

class MyTest(unittest.TestCase):
    def test_extract(self):
        opec_orb_data = extract(test_file_path)
        assert(extract_data==opec_orb_data)

    def test_transform(self):
        opec_orb_transform_data = transform(extract_data)
        assert(transform_data==opec_orb_transform_data)


if __name__ == '__main__':
    unittest.main()
