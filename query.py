import psycopg2
from common import *


def mentors(conn):
    rows = ask_query("""SELECT mentors.id, mentors.first_name, mentors.last_name, schools.name, schools.country FROM mentors
                    LEFT JOIN schools ON mentors.city = schools.city 
                    ORDER BY mentors.id ASC;""", conn)
    return rows


def all_school(conn):
    rows = ask_query("""SELECT mentors.id, mentors.first_name, mentors.last_name, schools.name, schools.country FROM mentors
                        RIGHT JOIN schools ON mentors.city = schools.city 
                        ORDER BY mentors.id ASC;""", conn)
    return rows


def mentors_by_country(conn):
    rows = ask_query("""SELECT COUNT(mentors.id), schools.country FROM mentors
                        FULL JOIN schools ON mentors.city = schools.city
                        GROUP BY schools.country 
                        ORDER BY schools.country ASC;""", conn)
    return rows


def contacts(conn):
    rows = ask_query("""SELECT schools.name, CONCAT(mentors.first_name,' ',mentors.last_name)
                        FROM mentors 
                        INNER JOIN schools ON mentors.id = schools.contact_person 
                        ORDER BY schools.name;""", conn)
    return rows
