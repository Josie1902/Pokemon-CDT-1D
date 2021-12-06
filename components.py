# import time

# # https://www.programiz.com/python-programming/examples/countdown-timer
# def countdown(time_sec):
#     while time_sec:

#         mins, secs = divmod(time_sec, 60)
#         timeformat = "{:02d}:{:02d}".format(mins, secs)
#         print(timeformat, end="\r")
#         time.sleep(1)
#         time_sec -= 1
#         if hello == "hello":
#             break

#     print("stop")


# countdown(5)

# hello

import threading
import time
import os


def countdown():
    time_sec = 5
    while time_sec:

        mins, secs = divmod(time_sec, 60)
        timeformat = "{:02d}:{:02d}".format(mins, secs)
        print(timeformat, end="\r")
        time.sleep(1)
        time_sec -= 1


def question():
    """
    Simple function where you ask him his name, if he answers
    you print message and exit
    """
    answer = input("Tell me your answer, you have 5 seconds: ")
    exit_message = f"Wohoho you did it. Answer is {answer}"
    exit(exit_message)


def exit(msg):
    """
    Exit function, prints something and then exits using OS
    Please note you cannot use sys.exit when threading..
    You need to use os._exit instead
    """
    print(msg)
    os._exit(1)


def close_if_time_pass(seconds):
    """
    Threading function, after N seconds print something and exit program
    """
    time.sleep(seconds)
    exit("Time passed, you've not found the correct answer")


def main():
    # define close_if_time_pass as a threading function, 5 as an argument
    t = threading.Thread(target=close_if_time_pass, args=(5,))
    # counter
    # countdown()
    # start threading
    t.start()
    # ask him his name
    question()


if __name__ == "__main__":
    main()

