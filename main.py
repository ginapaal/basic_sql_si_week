import sys
from common import *


def main(user_input):
    user_input = menu()
    conn = make_connection()
    if user_input == 1:
        list_mentor_names(conn)
    elif user_input == 2:
        nicknames(conn)
    elif user_input == 3:
        carol(conn)
    elif user_input == 4:
        other_girl(conn)
    elif user_input == 5:
        new_applicant(conn)
    elif user_input == 6:
        jemima_number_update(conn)
    elif user_input == 7:
        cancel_process(conn)
    elif user_input == 8:
        sys.exit()


if __name__ == "__main__":
    main(user_input)
