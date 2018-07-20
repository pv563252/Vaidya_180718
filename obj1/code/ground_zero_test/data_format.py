"""

"""


import pandas as pd
from utils.test_utils import *
from obj1.code.ground_zero_test.file_columns import test_headers


def data_format():
    """

    :return:
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


data_format()
