from typing import Self
from unittest import TestCase
from .main import binary_search, find_position


class TestBinarySearch(TestCase):
    def test_empty_array(self: Self):
        arr = []
        target = 5
        expected = -1

        self.assertEqual(binary_search(arr, target), expected)

    def test_first_and_last_element(self: Self) -> None:
        arr = [1, 2, 3, 7, 8, 9, 12, 34]
        target = 1
        expected = 0

        self.assertEqual(binary_search(arr, target), expected)

        target = 34
        expected = 7

        self.assertEqual(binary_search(arr, target), expected)

    def test_repeating_target(self: Self):
        arr = [0, 0, 0, 2, 2, 2, 3, 6, 6, 6, 6, 6, 6, 8, 8]
        target = 6
        expected = 7

        self.assertEqual(binary_search(arr, target), expected)


class TestFindPosition(TestCase):
    arr: list[int] = [0, 0, 0, 2, 2, 2, 3, 6, 6, 6, 6, 6, 6, 8, 8]

    def test_first_position(self):
        self.assertEqual(find_position(TestFindPosition.arr, 0)[0], 0)
        self.assertEqual(find_position(TestFindPosition.arr, 2)[0], 3)
        self.assertEqual(find_position(TestFindPosition.arr, 6)[0], 7)
        self.assertEqual(find_position(TestFindPosition.arr, 8)[0], 13)
        self.assertEqual(find_position(TestFindPosition.arr, 3)[0], 6)
        self.assertEqual(find_position([5, 7, 7, 8, 8, 10], 8)[0], 3)

    def test_ending_position(self):
        self.assertEqual(find_position(TestFindPosition.arr, 0)[1], 2)
        self.assertEqual(find_position(TestFindPosition.arr, 2)[1], 5)
        self.assertEqual(find_position(TestFindPosition.arr, 6)[1], 12)
        self.assertEqual(find_position(TestFindPosition.arr, 8)[1], 14)
        self.assertEqual(find_position(TestFindPosition.arr, 3)[1], 6)
        self.assertEqual(find_position([5, 7, 7, 8, 8, 10], 8)[1], 4)
