from flask import Flask
import os

MESSAGE = os.environ.get('MESSAGE')

app = Flask(__name__)


@app.route('/')
def index():
    return f'{MESSAGE}'


app.run(host='0.0.0.0', port=81, debug=True)
