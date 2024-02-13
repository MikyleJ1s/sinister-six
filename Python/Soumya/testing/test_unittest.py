import inc_dec    # The code to test
import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(inc_dec.increment(3), 4)

    # This test is designed to fail for demonstration purposes.
    def test_decrement(self):
        self.assertEqual(inc_dec.decrement(3), 2)
        
    def test_add(self):
        self.assertEqual(inc_dec.add(1,2), 3)
        
    def test_factorial(self):
        self.assertEqual(inc_dec.factorial(3), 6)
        self.assertEqual(inc_dec.factorial(-1), "Does not exist")
    
    def test_fibonacci(self):
        self.assertEqual(inc_dec.fibonacci(3), 2)        
        self.assertEqual(inc_dec.fibonacci(-1), "Invalid")


if __name__ == '__main__':
    unittest.main()

# unittest is a module