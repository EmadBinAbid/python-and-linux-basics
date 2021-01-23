import unittest

from python.dictionary_woes.fixup_case import fixup_case, to_upper_case


class FixupCaseShould(unittest.TestCase):
    def test_return_simple_dictionary_with_uppercase_keys_when_simple_dictionary_and_uppercase_callback_is_passed(self):
        actual_data = {
            "id": 1,
            "naMe": "John Doe",
            "Department_Name": "Product",
            "DESIGNATION": "Software Engineer"
        }

        expected_data = {
            "ID": 1,
            "NAME": "John Doe",
            "DEPARTMENT_NAME": "Product",
            "DESIGNATION": "Software Engineer"
        }

        self.assertEqual(fixup_case(actual_data, to_upper_case), expected_data)

    def test_return_nested_dictionary_with_uppercase_keys_when_nested_dictionary_and_uppercase_callback_is_passed(self):
        actual_data = {
            "id": 1,
            "naMe": "John Doe",
            "Department": {
                "iD": 1,
                "name": "Product"
            },
            "DESIGNATION": "Software Engineer"
        }

        expected_data = {
            "ID": 1,
            "NAME": "John Doe",
            "DEPARTMENT": {
                "ID": 1,
                "NAME": "Product"
            },
            "DESIGNATION": "Software Engineer"
        }

        self.assertEqual(fixup_case(actual_data, to_upper_case), expected_data)


class ToUpperCaseShould(unittest.TestCase):
    def test_return_uppercase_string_when_all_lowercase_passed(self):
        self.assertEqual(to_upper_case("test"), "TEST")

    def test_return_uppercase_string_when_mixcase_passed(self):
        self.assertEqual(to_upper_case("tEsT"), "TEST")

    def test_return_uppercase_string_when_all_uppercase_passed(self):
        self.assertEqual(to_upper_case("TEST"), "TEST")

    def test_return_uppercase_string_when_alphanumeric_string_passed(self):
        self.assertEqual(to_upper_case("tes2t12"), "TES2T12")
        self.assertEqual(to_upper_case("TES2T12"), "TES2T12")
        self.assertEqual(to_upper_case("tEs2T12"), "TES2T12")


if __name__ == '__main__':
    unittest.main()
