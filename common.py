import psycopg2


def menu():
    user_input = input("""1.) List all the mentors \n
2.) Nicknames of mentors in Miskolc \n
3.) Carol Smth left her hat here, what is her full name and phone number? \n
4.) Find the girl by her e-mail \n
5.) New applicant \n
6.) Jemima Foreman's number has changed \n
7.) Arsenio and friend want to cancel the process \n
8.) Exit \n
\n""")
    return int(user_input)


def make_connection():
    connect_str = "dbname = 'gina' user='gina' host='localhost' password ='thebest'"
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    return conn


def print_query(query, conn):
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return print(rows)


def cursor_execute(query, conn):
    cursor = conn.cursor()
    cursor.execute(query)


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
