"""A wonderful, simple database app
by Georgina Paál"""

import common
import query
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main_page():
    """ Lists all functions on the main page"""

    return render_template('main_page.html')


@app.route('/mentors', methods=['GET', 'POST'])
def mentors_and_schools():
    " Lists all mentors with thair school's name and country ordered by mentor id"

    conn = common.make_connection()
    rows = query.mentors(conn)
    conn.close()
    return render_template('mentors.html', rows=rows)


@app.route('/all-school', methods=['GET', 'POST'])
def all_school():
    """Lists all schools with their mentors - even if there's no mentor in specified school"""

    conn = common.make_connection()
    rows = query.all_school(conn)
    conn.close()
    return render_template('all_school.html', rows=rows)


@app.route('/mentors-by-country', methods=['GET', 'POST'])
def mentors_by_country():
    """ Shows us the number of mentors by country"""

    conn = common.make_connection()
    rows = query.mentors_by_country(conn)
    conn.close()
    return render_template('mentors_by_country.html', rows=rows)


@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    """Shows us the contact person in specified school"""

    conn = common.make_connection()
    rows = query.contacts(conn)
    conn.close()
    return render_template('contacts.html', rows=rows)


@app.route('/applicants', methods=['GET', 'POST'])
def applicants():
    """Lists the applicants name, code and the application's date if it was greater than 2016-01-01"""

    conn = common.make_connection()
    rows = query.applicants(conn)
    conn.close()
    return render_template('applicants.html', rows=rows)


@app.route('/applicants-and-mentors', methods=['GET', 'POST'])
def applicants_and_mentors():
    """Shows us applicants name, code and mentor's name"""

    conn = common.make_connection()
    rows = query.applicants_and_mentors(conn)
    conn.close()
    return render_template("applicants_and_mentors.html", rows=rows)


if __name__ == "__main__":
    app.run()
