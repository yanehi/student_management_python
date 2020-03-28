import unittest

class TestCalc(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(10, 5+5)
        
if __name__ == "__main__":
    unittest.main()