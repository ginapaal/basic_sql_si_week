from common import *
import sys


def main(user_input):
    conn = make_connection()
    try:
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
    except ValueError:
        print("You have to choose a number between 1-8. Try again!")
        input(": ")


if __name__ == "__main__":
    user_input = menu()
    main(user_input)
