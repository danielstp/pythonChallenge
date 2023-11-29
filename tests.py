#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test DataCapture
"""
import unittest
from statistics import DataCapture, LIMIT_MAX, LIMIT_MIN


class TestDataCapture(unittest.TestCase):
    """Tests for validate DataCapture

    Args:
        unittest (DataCapture): tests for validate DataCapture
    """

    def setUp(self):
        """Initialize the DataCapture objects"""
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        capture.add(LIMIT_MIN)
        capture.add(LIMIT_MAX)
        self.stats = capture.build_stats()

    def test_less(self):
        """Test less method"""
        self.assertEqual(self.stats.less(4), 3)
        self.assertEqual(self.stats.less(3), 1)
        self.assertEqual(self.stats.less(6), 4)
        with self.assertRaises(IndexError):
            self.stats.less(LIMIT_MAX + 1)
        with self.assertRaises(IndexError):
            self.stats.less(LIMIT_MIN - 1)

    def test_greater(self):
        """test greater method"""
        self.assertEqual(self.stats.greater(4), 3)
        self.assertEqual(self.stats.greater(3), 4)
        self.assertEqual(self.stats.greater(2), 6)
        with self.assertRaises(IndexError):
            self.stats.greater(LIMIT_MAX + 1)
        with self.assertRaises(IndexError):
            self.stats.greater(LIMIT_MIN - 1)

    def test_between(self):
        """test between method"""
        self.assertEqual(self.stats.between(8, 10), 1)
        self.assertEqual(self.stats.between(5, 10), 2)
        self.assertEqual(self.stats.between(8, 9), 1)
        self.assertEqual(self.stats.between(6, 3), 4)
        with self.assertRaises(IndexError):
            self.stats.between(LIMIT_MAX + 1, LIMIT_MIN - 1)
        with self.assertRaises(IndexError):
            self.stats.between(LIMIT_MIN - 1, LIMIT_MAX + 1)
        with self.assertRaises(IndexError):
            self.stats.between(LIMIT_MIN, LIMIT_MAX + 1)
        with self.assertRaises(IndexError):
            self.stats.between(LIMIT_MIN - 1, LIMIT_MAX)

    def test_add(self):
        """test add method"""
        capture = DataCapture()
        with self.assertRaises(IndexError):
            capture.add(LIMIT_MAX + 1)
        with self.assertRaises(IndexError):
            capture.add(LIMIT_MIN - 1)


if __name__ == "__main__":
    unittest.main()
