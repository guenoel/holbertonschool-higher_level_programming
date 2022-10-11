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

    def test_1_1(self):
        """to json string with value 0 - id check"""
        b3 = Base.to_json_string(None)
        self.assertEqual(b3, "[]")
