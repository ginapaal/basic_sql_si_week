from common import *
from query import *
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main_page():
    return render_template('main_page.html')


@app.route('/mentors', methods=['GET'])
def mentors_and_schools():
    pass


if __name__ == "__main__":
    app.run()
