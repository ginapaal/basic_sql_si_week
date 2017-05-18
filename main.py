from common import *
import sys


def main():
    conn = make_connection()
    list_mentor_names(conn)
    nicknames(conn)
    carol(conn)
    other_girl(conn)
    new_applicant(conn)
    jemima_number_update(conn)
    cancel_process(conn)


if __name__ == "__main__":
    main()
