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