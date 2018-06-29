from __future__ import absolute_import
from __future__ import print_function

from werkzeug.security import safe_str_cmp
from secrets import token_hex


try:
    import pbkdf2
except ImportError as e:
    print('pbkdf2 is required to use Flask-PBKDF2')
    raise e

def generate_password_hash(password,  salt=None, iterations=None):
    return PBKDF2().generate_password_hash(password, salt=None, iterations=None)

def check_password_hash(password_hash, password):
    return PBKDF2().check_password_hash(password_hash, password)

class PBKDF2(object):

    _iterations = 400

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        pass

    def generate_password_hash(self, password, salt=None, iterations=None):

        if iterations is None:
            iterations = self._iterations
        if salt is None:
            salt = token_hex()

        return pbkdf2.crypt(password, salt=salt, iterations=iterations)

    def check_password_hash(self, password_hash, password):
        return safe_str_cmp(pbkdf2.crypt(password, password_hash), password_hash)

