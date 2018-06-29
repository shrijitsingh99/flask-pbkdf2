# Flask-Pbkdf2
---
Flask-PBKDF2 is a Flask extension that provides PBKDF2 hashing utilities for your application

## Installation
---
This extension require ``python-3.6`` or greater
Clone the repository
``
$ git clone https://github.com/shrijitsingh99/flask-pbkdf2.git | cd flask-pbkdf2
``
Install the extension
``
$ python3 setup.py install
``

## Usage
---
```python
from flask_pbkdf2 import PBKDF
app = Flask(__name__)
pbkdf2 = PBKDF2(app)
```

You can use the hashing methods using the pbkdf2 object like this:
```python
password_hash = pbkdf2.generate_password_hash("password")
pbkdf2.check_password_hash(password_hash, "password")
```
