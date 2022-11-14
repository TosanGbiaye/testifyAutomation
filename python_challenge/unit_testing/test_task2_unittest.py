import task2
import unittest

class TestTask2(unittest.TestCase):

    def test_power(self):
        self.assertEqual(task2.power(4, 2), 16)
        self.assertEqual(task2.power(10, 2), 100)

if __name__ == '__main__':
    unittest.main()