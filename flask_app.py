from flask_cors import CORS
from flask import Flask
from util import finance

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello!'

@app.route('/finance/<code>', methods=['GET'])
def getFinance(code):
    return finance.fetchData(code)

if __name__ == '__main__': #pythonanywhere not use custon port
    app.run()