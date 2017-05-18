import sys
from common import *
from query import *


def main(user_input):
    user_input = 8
    while user_input > 0 and user_input <= 8:
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
        elif user_input == 0:
            sys.exit()


if __name__ == "__main__":
    user_input = menu()
    main(user_input)
