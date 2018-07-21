from utils.extractor_utils import read_json
from utils.test_utils import *
import os


def test_headers(df_columns, header_path=os.getcwd()+'/headers.json'):
    """
    Test 1: Tests the presence of all Expected Features in the Dataset.
    :param df_columns: Observed Features in the dataset.
    :param header_path: path to header file that maintains the Expected Features in the dataset.
    :return: Runs successfully for correct config of dataset, console outputs errors and root cause otherwise.
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
    Test to detect any missing features from expected dataset.
    :param expected: list of Expected Features.
    :param found: list of Observed Features.
    :return: Runs successfully for correct config of dataset, console outputs errors and root cause otherwise.
    """
    header_test = expected.difference(found)
    if len(header_test) > 0:
        test_result_handler("Test 1A: Missing Columns", "Test Failed", "Missing Columns in Dataframe", header_test)
    test_result_handler("Test 1A: Missing Columns", "Test Passed")


def additional_features(expected, found):
    """
    Test to detect any additional features from expected dataset.
    :param expected: list of Expected Features.
    :param found: list of Observed Features.
    :return: Runs successfully for correct config of dataset, console outputs errors and root cause otherwise.
    """
    header_test = found.difference(expected)
    if len(header_test) > 0:
        test_result_handler("Test 1A: Additional Data Found", "Test Failed", "Additional Columns in Dataframe",
                            header_test)
    test_result_handler("Test 1A: Additional Column Check", "Test Passed", "No additional columns in Dataframe")
