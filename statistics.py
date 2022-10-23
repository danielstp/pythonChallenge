#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""_summary_

    Returns:
        _type_: _description_
"""
import itertools
from array import array

LIMIT_MAX = 1000
LIMIT_MIN = 0

class DataCapture():
    """The DataCapture object accepts numbers and returns an object for querying
       statistics about the inputs. Specifically, the returned object supports
       querying how many numbers in the collection are less than a value, greater
       than a value, or within a range.
    """
    def __init__(self):
        """Initialize the arrays and matrix
        """
        self.data = []
        self.less_a = array('I', itertools.repeat(LIMIT_MIN, LIMIT_MAX + 1))
        self.between_m = [array('I', itertools.repeat(LIMIT_MIN, LIMIT_MAX + 1))
                         for x in range(LIMIT_MIN, LIMIT_MAX + 1)]
        self.greater_a = array('I', itertools.repeat(LIMIT_MIN, LIMIT_MAX + 1))

    def add(self, i : int):
        """Add values to data list
           have constant time O(1)

        Args:
            i (int): _description_
        """
        self.test_limits(i)
        self.data.append(i)
        self.between_m[i][i] += 1

    def less(self, i : int) -> int:
        """return the count of values in data less than i
           have constant time O(1)

        Args:
            i (int): value to compare

        Returns:
            int: count of values in data less than i
        """
        DataCapture.test_limits(i)
        return self.less_a[i]

    def greater(self, i : int) -> int:
        """return the count of values in data greater than i
           have constant time O(1)

        Args:
            i (int): value to compare

        Returns:
            int: return the count of values in data greater than i
        """
        DataCapture.test_limits(i)
        return self.greater_a[i]

    def between(self, i : int, j: int) -> int:
        """return the count of values between i and j inclusive
           have constant time O(1)
        Args:
            i (int): value to compare
            j (int): value to compare

        Returns:
            int: return the count of values between i and j inclusive
        """
        DataCapture.test_limits(i)
        DataCapture.test_limits(j)
        return self.between_m[i][j]

    @staticmethod
    def error_less(i : int):
        """validate i can't by less than LIMIT_MIN

        Args:
            i (int): value to compare
        """
        if i < LIMIT_MIN:
            print(f"Error the given number({i}) is less than {LIMIT_MIN}")
            raise IndexError

    @staticmethod
    def error_greater(i : int):
        """validate i can't by greater than LIMIT_MAX

        Args:
            i (int): value to compare
        """
        if i > LIMIT_MAX:
            print(f"Error the given number({i}) is greater than {LIMIT_MAX}")
            raise IndexError

    @staticmethod
    def test_limits(i : int):
        """validate i can't by greater than LIMIT_MAX and
           less than LIMIT_MIN

        Args:
            i (int): value to compare
        """
        DataCapture.error_greater(i)
        DataCapture.error_less(i)

    def build_stats(self):
        """fills the arrays less_a and greater_a also
           the matrix between_m

        Returns:
            None: None
        """
        less_sum = 0
        greater_sum = 0
        for i in range(0, LIMIT_MAX):
            self.less_a[i] = less_sum
            self.greater_a[LIMIT_MAX - i] = greater_sum

            less_sum += self.between_m[i][i]
            greater_sum += self.between_m[LIMIT_MAX - i][LIMIT_MAX - i]
            for j in range( i+1, LIMIT_MAX):
                self.between_m[j-i-1][j] = self.between_m[j-i-1][j-1]
                self.between_m[j-i-1][j] += self.between_m[j-i][j]
                self.between_m[j-i-1][j] -= self.between_m[j-i][j-1]
                self.between_m[j][j-i-1] = self.between_m[j-i-1][j]
        return self
