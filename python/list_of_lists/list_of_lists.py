def list_of_lists(matrix):
    """
    Takes in a 2D list and prints the sum of each inner list
    :param matrix: list of list - 2D list of int

    :return: None
    """

    for m in range(len(matrix)):
        print("List ", m + 1)
        print(sum(matrix[m]))
