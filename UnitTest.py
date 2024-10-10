from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.testCases = {1: {'s': '())', 'output': 1},
                          2: {'s': '(((', 'output': 3}}
        self.obj = Solution()
        return super().setUp()
    
    def test_Case1(self):
        s, output = self.testCases[1].values()
        result = self.obj.minAddToMakeValid(s)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    def test_Case2(self):
        s, output = self.testCases[2].values()
        result = self.obj.minAddToMakeValid(s)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()