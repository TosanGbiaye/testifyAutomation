import task9
import unittest

class TestTask9(unittest.TestCase):

    def test_upper_case(self):
        self.assertEqual(task9.upper_case("sandra"), "SANDRA")
        self.assertEqual(task9.upper_case("Tosan"), "TOSAN")


if __name__ == '__main__':
    unittest.main()