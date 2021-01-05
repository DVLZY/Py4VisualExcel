import unittest
import numpy as np


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    # ndarray 与 list
    def test_ndarray(self):
        a = [1, 2, 3, 4]  # 定义列表
        b = np.array([1, 2, 3, 4])  # 定义数组
        print(a)  # [1, 2, 3, 4]
        print(b)  # [1 2 3 4]
        print(type(a))  # <class 'list'>
        print(type(b))  # <class 'numpy.ndarray'>
        print(a[1:])  # [2, 3, 4]
        print(b[1:])  # [2 3 4]

        '''
        ndarray优势
        1、对数学运算的支持较好
        2、对多维数据的存储支持较好
        '''

    # ndarray 创建
    def test_createArray(self):
        a = np.array([1, 2, 3, 4])
        b = np.array([[1, 2], [3, 4], [5, 6]])  # 二维数组

        c = np.arange(3, 9, 2)  # 创建指定步长的数组  [3 5 7]
        d = np.random.randn(3)  # 创建随机数组 [ 0.67273811 -1.51273043 -0.00857895]

        e = np.arange(25).reshape(5, 5)  # 利用转换数组的行列创建多维数组
        '''
        [[ 0  1  2  3  4]
         [ 5  6  7  8  9]
         [10 11 12 13 14]
         [15 16 17 18 19]
         [20 21 22 23 24]]
        '''
        f = np.random.randint(0, 10, (4, 4))  # 创建4*4的取值为0~10的数组
        '''
        [[8 1 2 9]
         [1 1 1 2]
         [2 3 6 5]
         [2 1 6 5]]
        '''


if __name__ == '__main__':
    unittest.main()
