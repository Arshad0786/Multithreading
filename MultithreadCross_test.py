# -*- coding: utf-8 -*-
import unittest
from MatrixCross import  multithreadCross, initializeA, initializeB

class MatrixCrossTest(unittest.TestCase):
    """
    def test_multithreadCrossResultAccuracyTest(self):
        a = [[2, -4], [5, 3]]
        b = [[3, 2], [7, -1]]
        result = multithreadCross(a,b)
        self.assertEqual(result,[[-22, 8], [36, 7]])

    def test_RegularMultiSameCheck(self):
        self.assertEqual(regularCross(initializeA(),initializeB()), multithreadCross(initializeA(),initializeB()))
    """

    def test_multithreadCrossAB(self):
        #測試作業規定矩陣的相乘時間
        multithreadCross(initializeA(),initializeB())

if __name__ == "__main__":
    unittest.main()
