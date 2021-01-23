def to_upper_case(string):
    return string.upper()


def fixup_case(data, conversion_scheme):
    """
    Takes in data in the form of dictionary and standardizes its keys according given conversion scheme

    :param data: dict - API data; supports nested dictionaries as well
    :param conversion_scheme: callback function - desired scheme to standardize the keys

    :return: dict - data dictionary with all keys standardized
    """

    data = {conversion_scheme(k): v for k, v in data.items()}
    processed_data = {}

    for k, v in data.items():
        if isinstance(v, dict):
            processed_data[conversion_scheme(k)] = fixup_case(v, conversion_scheme)
        else:
            processed_data[conversion_scheme(k)] = v

    return processed_data
