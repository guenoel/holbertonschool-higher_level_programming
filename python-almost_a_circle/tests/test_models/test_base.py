#!/usr/bin/python3
""" Tests for base class """

import unittest
from models.base import Base
import json
import sys


class TestBase(unittest.TestCase):
    """Test class for Base class"""

#    def setUp(self):
#        Base._Base__nb_objects = 0

    def test_1_0(self):
        """Create new instance - id check"""

        b0 = Base()
        self.assertEqual(b0.id, 1)

    def test_2_0(self):
        """Create 2nd new instance - id check"""
        b1 = Base()
        self.assertEqual(b1.id, 2)

    def test_3_0(self):
        """Create new instance with value - id check"""
        b2 = Base(89)
        self.assertEqual(b2.id, 89)

    def test_4_0(self):
        """Create new instance with value 0 - id check"""
        b3 = Base(0)
        self.assertEqual(b3.id, 0)

    def test_5_0(self):
        """Create new instance with number non-preallocated - id check"""
        b4 = Base(421)
        self.assertEqual(b4.id, 421)

    def test_6_0(self):
        """Create new instance with negative number - id check"""
        b5 = Base(-2)
        self.assertEqual(b5.id, -2)
