"""
Write a python3 function called “increment_count” that takes one argument names “by”. Whatever value is passed in via
the “by” argument should be added to a global variable “the_count”. Before exiting, a global variable named “last_by”
should be updated with with the value that was passed in via the “by” argument. This function should be THREAD SAFE
and utilize a global Lock variable defined outside the function to isolate the update of both “the_count” and “last_by”
in the same exclusive access block. Extra credit for utilizing python3 context management protocol, which is supported
by Locks in this scenario.
"""


from threading import Lock

lock = Lock()

the_count = 0
last_by = 0


def increment_count(by):
    with lock:
        global the_count
        global last_by

        the_count += by
        last_by = by


def main():
    by = 0  # TODO: define your own value of 'by' here 
    increment_count(by)


if __name__ == '__main__':
    main()
