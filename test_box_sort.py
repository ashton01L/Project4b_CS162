# Author: Ashton Lee
# Github User: ashton01L
# Date: 10/26/2024
# Description: Unit tests for Box class whose init method takes three parameters and uses them to initialize the private
# length, width and height data members of a Box.

import unittest
from box_sort import Box, box_sort

class TestBoxSort(unittest.TestCase):
    """
    Test cases to appropriately tests functionality and edge cases for Box class and box_sort method
    """
    def test_volume_calculation(self):
        """
        Tests volume calculation for box
        """
        box = Box(2, 3, 4)
        self.assertEqual(box.volume(), 24)

    def test_volume_zero(self):
        """
        Tests volume calculation returns zero when calculation equals zero
        """
        box = Box(0, 3, 4)
        self.assertEqual(box.volume(), 0)

    def test_sort_order(self):
        """
        Tests order of sort from greatest volume to least as per box_sort requirement
        """
        b1 = Box(3, 2, 5)  # Volume = 30
        b2 = Box(1, 1, 1)  # Volume = 1
        b3 = Box(2, 3, 4)  # Volume = 24
        box_list = [b1, b2, b3]
        box_sort(box_list)
        self.assertEqual([box.volume() for box in box_list], [30, 24, 1])

    def test_equal_volumes(self):
        """
        Tests sort doesn't error when volumes of multiple boxes are equal
        """
        b1 = Box(2, 3, 4)  # Volume = 24
        b2 = Box(4, 3, 2)  # Volume = 24
        box_list = [b1, b2]
        box_sort(box_list)
        self.assertEqual([box.volume() for box in box_list], [24, 24])

    def test_single_box(self):
        """
        Tests does not error out when only single box is listed
        """
        box_list = [Box(2, 3, 4)]
        box_sort(box_list)
        self.assertEqual(box_list[0].volume(), 24)

    def test_empty_list(self):
        """
        Tests no error when list of boxes is empty
        """
        box_list = []
        box_sort(box_list)
        self.assertEqual(box_list, [])

    def test_getters(self):
        """
        Tests getter methods
        """
        box = Box(5, 6, 7)
        self.assertEqual(box.get_length(), 5)
        self.assertEqual(box.get_width(), 6)
        self.assertEqual(box.get_height(), 7)

    def test_large_volumes(self):
        """
        Tests boxes with very large volumes
        """
        b1 = Box(1e6, 1e6, 1e6)  # Very large volume
        b2 = Box(1, 1, 1)
        box_list = [b1, b2]
        box_sort(box_list)
        self.assertEqual([box.volume() for box in box_list], [1e18, 1])

    def test_negative_dimensions(self):
        """
        Tests boxes with a negative volume
        """
        box = Box(-2, 3, 4)
        self.assertEqual(box.volume(), -24)


if __name__ == "__main__":
    unittest.main()
