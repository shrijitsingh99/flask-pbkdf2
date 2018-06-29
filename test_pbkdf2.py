import unittest
import flask
from flask_pbkdf2 import PBKDF2, check_password_hash, generate_password_hash


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        app = flask.Flask(__name__)
        self.pbkdf2 = PBKDF2(app)

    def test_check_hash(self):
        # Generate password hash
        password_hash = self.pbkdf2.generate_password_hash("password")
        # Check correct password
        self.assertTrue(self.pbkdf2.check_password_hash(password_hash, "password"))
        # Check incorrect password
        self.assertFalse(self.pbkdf2.check_password_hash(password_hash, "hunter2"))


if __name__ == '__main__':
    unittest.main()
