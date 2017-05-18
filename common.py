import psycopg2


def menu():
    user_input = input("""1.) List all the mentors \n
2.) Nicknames of mentors in Miskolc \n
3.) Carol Smth left her hat here, what is her full name and phone number? \n
4.) Find the girl by her e-mail \n
5.) New applicant \n
6.) Jemima Foreman's number has changed \n
7.) Arsenio and friend want to cancel the process \n
0.) Exit \n
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
