"""

"""

import pandas as pd
from utils.test_utils import *
from obj1.code.data_hygiene.feature_range import feature_range_test
from obj1.code.data_hygiene.feature_type import feature_type_test


def feature_values():
    """

    :return:
    """
    try:
        begin_test_message("Data Hygiene: Feature Test Suite")
        df = pd.read_excel('/Users/pv/Desktop/jpmc_rse_assignment/jpmc_rse_assignment_data.xlsx')
        feature_type_test(df)
        feature_range_test(df)
    except Exception as e:
        print('################################################################################')
        print("An Error happened during Data Hygiene: Feature Test Suite Execution")
        print(e)
        print('################################################################################')
    finally:
        end_test_message("Data Hygiene: Feature Test Suite")


feature_values()