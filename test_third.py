import third
import unittest

class Test_your_name_work(unittest.TestCase):

    def test_string(self):
        self.assertEqual(third.count_letter_in_string('aniko',"o"), 1)

    def test_not_string_input(self):
        self.assertRaises(TypeError, third.count_letter_in_string, 3)

    def test_Uppercase_or_Lowercase(self):
        self.assertEqual(third.count_letter_in_string('Aniko',"a"), 0)

if __name__ == '__main__':
    unittest.main()
a
