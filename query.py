"""In this module i created the querys sticked to the requirements"""


import psycopg2
import common


def mentors(conn):
    rows = common.ask_query("""SELECT mentors.id, mentors.first_name, mentors.last_name, schools.name, schools.country FROM mentors
                    LEFT JOIN schools ON mentors.city = schools.city 
                    ORDER BY mentors.id ASC;""", conn)
    return rows


def all_school(conn):
    rows = common.ask_query("""SELECT mentors.id, mentors.first_name, mentors.last_name, schools.name, schools.country FROM mentors
                        RIGHT JOIN schools ON mentors.city = schools.city 
                        ORDER BY mentors.id ASC;""", conn)
    return rows


def mentors_by_country(conn):
    rows = common.ask_query("""SELECT COUNT(mentors.id), schools.country FROM mentors
                        FULL JOIN schools ON mentors.city = schools.city
                        GROUP BY schools.country 
                        ORDER BY schools.country ASC;""", conn)
    return rows


def contacts(conn):
    rows = common.ask_query("""SELECT schools.name, CONCAT(mentors.first_name,' ',mentors.last_name)
                        FROM mentors 
                        INNER JOIN schools ON mentors.id = schools.contact_person
                        ORDER BY schools.name;""", conn)
    return rows


def applicants(conn):
    rows = common.ask_query("""SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date FROM applicants
                        JOIN applicants_mentors ON applicants.id = applicants_mentors.applicant_id
                        WHERE applicants_mentors.creation_date > '2016-01-01'
                        ORDER BY applicants_mentors.creation_date DESC;""", conn)
    return rows


def applicants_and_mentors(conn):
    rows = common.ask_query("""SELECT applicants.first_name, applicants.application_code, CONCAT(mentors.first_name,' ',mentors.last_name)
                        FROM applicants
                        FULL JOIN applicants_mentors ON applicants.id = applicants_mentors.applicant_id
                        LEFT JOIN mentors ON mentors.id = applicants_mentors.mentor_id
                        ORDER BY applicants.id ASC;""", conn)
    return rows
