"""
https://docs.python.org/3/library/unittest.html
"""
import unittest
from app.utils import COMPASS_TO_DIR, DIR_TO_COMPASS, array_to_string

class TestUtils(unittest.TestCase):
    """
    TestCase for the utilities
    """

    def test_array_to_string(self):
        stringN = array_to_string([0, 1])
        stringS = array_to_string([0, -1])
        stringW = array_to_string([-1, 0])
        stringE = array_to_string([1, 0])

        self.assertIsNotNone(stringN)
        self.assertEqual(stringN, '0 1')

        self.assertIsNotNone(stringS)
        self.assertEqual(stringS, '0 -1')
        
        self.assertIsNotNone(stringW)
        self.assertEqual(stringW, '-1 0')
        
        self.assertIsNotNone(stringE)
        self.assertEqual(stringE, '1 0')


    def test_dir_to_compass(self):
        for key in DIR_TO_COMPASS.keys():
            self.assertIsInstance(key, str)
            self.assertEqual(DIR_TO_COMPASS[key], 1)
            self.assertIn(DIR_TO_COMPASS[key], ('N', 'S', 'W', 'E'))
        
        self.assertIsNotNone(DIR_TO_COMPASS['0 1'])
        self.assertEqual(DIR_TO_COMPASS['0 1'], 'N')
        
        self.assertIsNotNone(DIR_TO_COMPASS['0 -1'])
        self.assertEqual(DIR_TO_COMPASS['0 -1'], 'S')
        
        self.assertIsNotNone(DIR_TO_COMPASS['1 0'])
        self.assertEqual(DIR_TO_COMPASS['1 0'], 'E')
        
        self.assertIsNotNone(DIR_TO_COMPASS['-1 0'])
        self.assertEqual(DIR_TO_COMPASS['-1 0'], 'W')


    def test_compass_to_dir(self):
        for key in COMPASS_TO_DIR.keys():
            self.assertIsInstance(key, str)
            self.assertEqual(key, 1)
            self.assertIn(key, ('N', 'S', 'W', 'E'))
        
        self.assertIsNotNone(COMPASS_TO_DIR['N'])
        self.assertEqual(len(COMPASS_TO_DIR['N']), 2)
        self.assertEqual(COMPASS_TO_DIR['N'], [0, 1])
        
        self.assertIsNotNone(COMPASS_TO_DIR['S'])
        self.assertEqual(len(COMPASS_TO_DIR['S']), 2)
        self.assertEqual(COMPASS_TO_DIR['S'], [0, -1])
        
        self.assertIsNotNone(COMPASS_TO_DIR['E'])
        self.assertEqual(len(COMPASS_TO_DIR['E']), 2)
        self.assertEqual(COMPASS_TO_DIR['E'], [1, 0])
        
        self.assertIsNotNone(COMPASS_TO_DIR['W'])
        self.assertEqual(len(COMPASS_TO_DIR['W']), 2)
        self.assertEqual(COMPASS_TO_DIR['W'], [-1, 0])


if __name__ == '__main__':
    unittest.main()