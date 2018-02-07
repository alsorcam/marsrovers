import unittest
import math
from app.models import Rover, Plateau, Storage

class TestModels(unittest.TestCase):
    """
    TestCase for the models
    """

    def test_storage(self):
        plateau = [4, 3]
        deployment = {
            1: [3, 4, 'N'],
            2: [0, 2, 'W']
        }
        movement = {
            1: 'LMRLMRRLL',
            2: 'LMRRML'
        }
        storage = Storage(plateau, deployment, movement)

        self.assertIsNotNone(storage.get_plateau())
        self.assertIsNot(storage.get_plateau(), [])
        self.assertEqual(len(storage.get_plateau()), 2)
        
        self.assertIsNotNone(storage.get_deployment())
        self.assertIsNotNone(storage.get_deployment().keys())
        for key in storage.get_deployment().keys():
            self.assertIsNot(storage.get_deployment()[key], [])
            self.assertEqual(len(storage.get_deployment()[key]), 3)

            cardinal_point = storage.get_deployment()[key][2]
            self.assertIsNotNone(cardinal_point)
            self.assertIn(cardinal_point, ('N', 'S', 'W', 'E'))
            self.assertEqual(len(cardinal_point), 1)

        self.assertIsNotNone(storage.get_movements())
        self.assertIsNotNone(storage.get_movements().keys())
        for key in storage.get_movements().keys():
            self.assertNotEqual(storage.get_movements()[key], '')        
            self.assertIsInstance(storage.get_movements()[key], str)
            for move in storage.get_movements()[key]:
                self.assertIn(move, ('L', 'R', 'M'))
        

    def test_rover(self):
        rover = Rover([1, 2, 'N'])

        self.assertIsNotNone(rover.get_position())
        self.assertIsNot(rover.get_position(), [])
        self.assertEqual(len(rover.get_position()), 2)
        
        self.assertIsNotNone(rover.get_direction())
        self.assertIsNot(rover.get_direction(), [])
        self.assertEqual(len(rover.get_direction()), 2)

        self.assertIsNotNone(rover.get_compass())
        self.assertIn(rover.get_compass(), ('N', 'S', 'W', 'E'))
        self.assertEqual(rover.get_compass(), 'N')
        self.assertEqual(len(rover.get_compass()), 1)

        plateau = Plateau([5, 5])
        rover.move('L', plateau)
        self.assertEqual(rover.get_compass(), 'W')
        rover.move('RR', plateau)
        self.assertEqual(rover.get_compass(), 'E')
        rover.move('R', plateau)
        self.assertEqual(rover.get_compass(), 'S')
        rover.move('MM', plateau)
        self.assertEqual(rover.get_compass(), 'S')
        self.assertEqual(rover.get_position(), [1, 0])
        rover.move('M', plateau)
        self.assertEqual(rover.get_compass(), 'S')
        self.assertEqual(rover.get_position(), [1, 0])


    def test_plateau(self):
        plateau = Plateau([7, 6])

        self.assertIsNotNone(plateau.get_size())
        self.assertIsNot(plateau.get_size(), [])
        self.assertEqual(len(plateau.get_size()), 2)
        self.assertIsInstance(plateau.get_size()[0], int)
        self.assertIsInstance(plateau.get_size()[1], int)


if __name__ == '__main__':
    unittest.main()