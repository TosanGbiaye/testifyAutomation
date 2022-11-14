import task10
import unittest

class TestTask10(unittest.TestCase):

    def test_sentence_case(self):
        self.assertEqual(task10.sentence_case("TODAY IS GONNA BE A GREAT DAY"), "Today is gonna be a great day")



if __name__ == '__main__':
    unittest.main()