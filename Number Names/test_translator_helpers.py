from translator_helpers import Helpers
import unittest


class TestTranslatorHelpers(unittest.TestCase):
    
    def test_should_ouput_5_when_given_number_with_5_digits(self):
        self.assertEqual(5, Helpers().number_of_digits(12340))
    
    def test_should_get_first_digit(self):
        self.assertEqual(3, Helpers().get_first_digit(34509006543))
        
    def test_should_be_able_to_left_shift_number(self):
        self.assertEqual(4509006543, Helpers().left_shift(34509006543))
    

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
