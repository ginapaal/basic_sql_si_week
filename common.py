import psycopg2


def make_connection():
    """It creates connection with the database, no argument needed"""

    connect_str = "dbname = 'gina' user='gina' host='localhost' password ='thebest'"
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    return conn


def ask_query(query, conn):
    """ Make querys from the database, needs two arguments: query and conn"""

    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows
