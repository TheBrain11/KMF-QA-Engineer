import unittest
import TestThis

class TestMethods(unittest.TestCase):
    def test_multiply(self):
        string = "You can't have egg, bacon, sausage, and spam without spam."
        self.assertRaises(ValueError, TestThis.multiply, string, 1)

    def test_print_text(self):
        expected_result = 'Test passed!'
        result = TestThis.print_text('Any string is fine here', TestThis.Requests())
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

