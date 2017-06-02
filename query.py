import psycopg2
from common import *


def mentors(conn):
    rows = ask_query("""SELECT mentors.first_name, mentors.last_name, schools.name, schools.country FROM mentors
                    LEFT JOIN schools ON mentors.city = schools.city;""", conn)
    return rows
