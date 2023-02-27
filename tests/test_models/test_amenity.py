#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_amenity(self):
        am = Amenity()
        self.assertEqual(am.name, "")
