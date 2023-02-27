#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_city:
        ct = City()
        self.assert(ct.name, "")
