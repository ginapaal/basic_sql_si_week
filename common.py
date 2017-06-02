import psycopg2


def make_connection():
    connect_str = "dbname = 'gina' user='gina' host='localhost' password ='thebest'"
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    return conn


def ask_query(query, conn):
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows
