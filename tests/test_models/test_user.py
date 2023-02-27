#!/usr/bin/python3
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_email:
        user = User()
        self.assertEqual(user.email, "")

    def test_password:
        user = User()
        self.assertEqual(user.password, "")

    def test_first_name:
        user = User()
        self.assertEqual(user.first_name, "")

    def test_last_name:
        user = User()
        self.assertEqual(user.last_name, "")
