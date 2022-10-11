#!/usr/bin/python3
""" Tests for base class """

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test class for Base class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_1_0(self):
        """Create new instances - id check"""

        b0 = Base()
        self.assertEqual(b0.id, 1)

    def test_2_0(self):
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base(89)
        self.assertEqual(b2.id, 89)
        b3 = Base(0)
        self.assertEqual(b3.id, 0)
        b4 = Base(421)
        self.assertEqual(b4.id, 421)
        b5 = Base(-2)
        self.assertEqual(b5.id, -2)
        b6 = Base(8)
        self.assertEqual(b6.id, 8)