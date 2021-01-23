def to_upper_case(string):
    return string.upper()


def fixup_case(data, conversion_scheme):
    """
    Takes in data in the form of dictionary and standardizes its keys according given conversion scheme

    :param data: dict - API data in the form of simple dictionary (no nesting) - use case assumption
    :param conversion_scheme: callback function - desired scheme to standardize the keys

    :return: dict - data dictionary with all keys standardized
    """

    data = {conversion_scheme(k): v for k, v in data.items()}

    return data
