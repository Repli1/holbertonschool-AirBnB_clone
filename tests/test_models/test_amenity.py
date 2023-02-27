#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_amenity:
        am = Amenity()
        self.assertEqual(am.name, "")
