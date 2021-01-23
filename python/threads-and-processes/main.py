"""
Without using 3rd party libraries (only things included in python3+), create a python program that starts 4 additional
processes, each of which start 10 threads. Each thread waits for strings to be sent via a thread and processor safe
Queue.  When any thread receives a string, it prints out its thread id as well as the string. Each thread monitors a
thread and processor safe Event and when the event is set, each thread should print an exit message and terminate,
but only if there is no more data to be read on the Queue. The mainline of the program (which spawned the processes)
should send 100 different strings to the Queue, causing strings to be available for receiving by the 40 threads. When
the mainline is done, set the exit Event to trigger the 40 threads to gracefully exit.

Hint: Compare multiprocess and threading modules and decide which to use when utilizing processes. One can be used in
both situations, the other cannot.
"""

def main():
    pass

if __name__ == '__main__':
    main()