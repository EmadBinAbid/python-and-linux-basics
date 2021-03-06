"""
Implement a python3 code snippet that iterates a list of lists. For each inner list encountered, print a header that
says “List X” where X is the number of the inner list (i.e. “List 1”… “List 5”). After the “List X” header, print the
sum of all items in the inner list. Do this for all inner lists contained in the outer list.
"""

from python.list_of_lists.list_of_lists import list_of_lists


def main():
    matrix = [[]]   # TODO: define your 2D list here
    list_of_lists(matrix)


if __name__ == '__main__':
    main()
