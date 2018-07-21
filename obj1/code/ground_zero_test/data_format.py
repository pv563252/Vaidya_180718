import pandas as pd
from utils.test_utils import *
from obj1.code.ground_zero_test.file_columns import test_headers


def data_format():
    """
    Test Suite for Errors due to the dataset format provided.
    :return: Runs successfully for correct config of dataset, console outputs errors otherwise.
    """
    try:
        begin_test_message("Starting Ground Zero Test Suite")
        df = pd.read_excel('/Users/pv/Desktop/jpmc_rse_assignment/jpmc_rse_assignment_data.xlsx')
        test_headers(list(df.columns))
    except Exception as e:
        print('###########################################################')
        print("An Error happened during Ground Zero Test Suite Execution")
        print(e)
        print('###########################################################')
    finally:
        end_test_message("Ground Zero Test Suite")


data_format()
