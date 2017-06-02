import common
import query
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main_page():
    return render_template('main_page.html')


@app.route('/mentors', methods=['GET', 'POST'])
def mentors_and_schools():
    conn = common.make_connection()
    rows = query.mentors(conn)
    conn.close()
    return render_template('mentors.html', rows=rows)


@app.route('/all-school', methods=['GET', 'POST'])
def all_shool():
    conn = common.make_connection()
    rows = query.all_school(conn)
    conn.close()
    return render_template('all_school.html', rows=rows)


@app.route('/mentors-by-country', methods=['GET', 'POST'])
def mentors_by_country():
    conn = common.make_connection()
    rows = query.mentors_by_country(conn)
    conn.close()
    return render_template('mentors_by_country.html', rows=rows)


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    conn = common. make_connection()
    rows = query.contacts(conn)
    conn.close()
    return render_template('contacts.html', rows=rows)


if __name__ == "__main__":
    app.run()
