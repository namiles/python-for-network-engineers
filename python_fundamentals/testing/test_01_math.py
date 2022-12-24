import unittest
from my_maths import multiply, subtract

# Create a class that inherits from TestCase
class TestMyMath(unittest.TestCase):

    # Methods must start with "test_"
    def test_mulitply(self):
        result = multiply(2, 4)
        # Use assertEqual and expect the result to be 8, which is the result of 4*2
        self.assertEqual(result, 8)

    # Methods must start with "test_"
    def test_subtract(self):
        result = subtract(4, 2)
        # Use assertEqual and expect the result to be 2, which is the result of 4-2
        self.assertEqual(result, 2)

    def test_stuff(self):
        my_list = [2, 5, 7, 8]
        my_num = multiply(2, 4)

        # use assertIn to check if my_num is present in my_list.
        # If it's in the list, return true/pass
        self.assertIn(my_num, my_list)


if __name__ == "__main__":
    unittest.main()
    # OR python3 -m unittest test_maths.py
