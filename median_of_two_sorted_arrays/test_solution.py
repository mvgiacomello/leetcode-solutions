import unittest
from median_of_two_sorted_arrays import solution


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(2.0, solution.median_sorted_arrays(nums1=[1, 3], nums2=[2]))
        self.assertEqual(2.5, solution.median_sorted_arrays(nums1=[1, 2], nums2=[3, 4]))
        self.assertEqual(3, solution.median_sorted_arrays(nums1=[1, 2, 3], nums2=[3, 4, 5]))
        with self.assertRaises(ValueError):
            solution.median_sorted_arrays(nums1=[], nums2=[])


if __name__ == '__main__':
    unittest.main()
