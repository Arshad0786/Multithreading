# -*- coding: utf-8 -*-
import unittest
from MatrixCross import regularCross,multithreadCross, initializeA, initializeB

class MatrixCrossTest(unittest.TestCase):
    """
    def test_RegularCrossResultAccuracyTest(self):
        #測試矩陣相乘的正確性
        a = [[2, -4], [5, 3]]
        b = [[3, 2], [7, -1]]
        result = regularCross(a,b)
        self.assertEqual(result,[[-22, 8], [36, 7]])
    
    def test_RegularMultiSameCheck(self):
        self.assertEqual(regularCross(initializeA(),initializeB()), multithreadCross(initializeA(),initializeB()))
    """
    def test_RegularCrossAB(self):
        #測試作業規定矩陣的相乘時間
        regularCross(initializeA(),initializeB())


if __name__ == "__main__":
    unittest.main()
