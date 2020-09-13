import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from flask_app import app 
api = app.test_client()

def test_hello():
    response = api.get('/')

    assert response.status_code == 200
    assert response.data == b'Hello from Flask!'