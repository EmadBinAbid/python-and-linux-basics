"""
A proprietary API for querying a remote data service returns data rows in key/value dictionaries, but the key name
case is unreliable. They are always well formed in regard to using underscore for spaces, but the case tends to be
unreliable. For example: CuStoMer_NAMe, CUSTOMER_name, Customer_Name, customer_name. We need to standardize the
dictionary key case on all records before inserting the dictionary into mongodb. Define and implement a python3
function named “fixup_case” that takes a dictionary as an argument and returns a dictionary with its key names
standardized. Explain the method of standardization you picked and why.
"""

from python.dictionary_woes.fixup_case import fixup_case, to_upper_case


def main():
    api_data = {}   # TODO: define your data here
    fixup_case(api_data, to_upper_case)


if __name__ == '__main__':
    main()