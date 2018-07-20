from utils.extractor_utils import read_json
from utils.test_utils import *
import os


def test_headers(df_columns, header_path=os.getcwd()+'/headers.json'):
    """

    :param df_columns:
    :param header_path:
    :return:
    """
    begin_test_message("Test 1: Feature Test.")
    headers = read_json(header_path)
    expected = set(headers.keys())
    found = set(df_columns)
    missing_features(expected, found)
    additional_features(expected, found)
    end_test_message("Test 1: Feature Test.")


def missing_features(expected, found):
    """

    :param expected:
    :param found:
    :return:
    """
    header_test = expected.difference(found)
    if len(header_test) > 0:
        test_result_handler("Test 1A: Missing Columns", "Test Failed", "Missing Columns in Dataframe", header_test)
    test_result_handler("Test 1A: Missing Columns", "Test Passed")


def additional_features(expected, found):
    """

    :param expected:
    :param found:
    :return:
    """
    header_test = found.difference(expected)
    if len(header_test) > 0:
        test_result_handler("Test 1A: Additional Data Found", "Test Failed", "Additional Columns in Dataframe",
                            header_test)
    test_result_handler("Test 1A: Additional Column Check", "Test Passed", "No additional columns in Dataframe")
