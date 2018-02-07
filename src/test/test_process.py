import unittest
from app.process import read_file, process_data

class TestProcess(unittest.TestCase):
    """
    TestCase for the data process functions
    """

    def test_read_file(self):
        path = '../test_input.txt'
        data = read_file(path)

        self.assertIsNotNone(data)
        self.assertIsNot(data, [])

    def test_process_data(self):
        path = '../test_input.txt'
        data = read_file(path)

        self.assertIsNotNone(data)
        self.assertIsNot(data, [])

        plateau, deployment, movements = process_data(data)

        self.assertIsNotNone(plateau)
        self.assertIsNot(plateau, [])
        self.assertEqual(len(plateau), 2)
        
        self.assertIsNotNone(deployment)
        self.assertIsNotNone(deployment.keys())
        for key in deployment.keys():
            self.assertIsNot(deployment[key], [])
            self.assertEqual(len(deployment[key]), 3)

            cardinal_point = deployment[key][2]
            self.assertIsNotNone(cardinal_point)
            self.assertIn(cardinal_point, ('N', 'S', 'W', 'E'))
            self.assertEqual(len(cardinal_point), 1)

        self.assertIsNotNone(movements)
        self.assertIsNotNone(movements.keys())
        for key in movements.keys():
            self.assertNotEqual(movements[key], '')        
            self.assertIsInstance(movements[key], str)
            for move in movements[key]:
                self.assertIn(move, ('L', 'R', 'M'))


if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()