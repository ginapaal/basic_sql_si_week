import psycopg2
from common import *


def list_mentor_names(conn):
    print_query("""SELECT first_name, last_name FROM mentors;""", conn)


def nicknames(conn):
    print_query("""SELECT nick_name FROM mentors WHERE city='Miskolc';""", conn)


def carol(conn):
    print_query("""SELECT concat(first_name,' ',last_name), phone_number FROM applicants WHERE first_name='Carol';""", conn)


def other_girl(conn):
    print_query("""SELECT concat(first_name,' ',last_name), phone_number FROM applicants WHERE email LIKE '%adipiscingenimmi.edu';""", conn)


def new_applicant(conn):
    print_query("""SELECT * FROM applicants WHERE id=11;""", conn)


def jemima_number_update(conn):
    cursor_execute(
        """UPDATE applicants SET phone_number = '003670/223-7459' WHERE application_code = 58324;""", conn)
    print_query("""SELECT first_name, last_name, phone_number FROM applicants WHERE application_code = 58324;""", conn)


def cancel_process(conn):
    cursor_execute("""DELETE FROM applicants WHERE email LIKE '%mauriseu.net';""", conn)
