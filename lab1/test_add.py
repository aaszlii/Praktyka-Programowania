import unittest
from myCode import Add

class TestAddFunction(unittest.TestCase):
    def testEmptyString(self):
        self.assertEqual(Add(''), 0)

    def testSingleNumber(self):
        self.assertEqual(Add('1'), 1)

    def testTwoNumbers(self):
        self.assertEqual(Add('1,2'), 3)

    def testMultipleNumbers(self):
        self.assertEqual(Add('1,2,3'), 6)
        self.assertEqual(Add('1,2,3,4'), 10)

    def testMultipleLines(self):
        self.assertEqual(Add('1,2\n3'),6)

    def testInvalidNewLine(self):
        with self.assertRaises(ValueError):
            Add("1,\n")

