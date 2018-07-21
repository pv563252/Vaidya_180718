import pandas as pd
from utils.test_utils import *
from obj1.code.data_anomaly_detection import clustering


def data_anomalies():
    """

    :return:
    """
    try:
        begin_test_message("Starting Anomaly Test Suite")
        df = pd.read_excel('/Users/pv/Desktop/jpmc_rse_assignment/jpmc_rse_assignment_data.xlsx')

    except Exception as e:
        print('###########################################################')
        print("An Error happened during Anomaly Test Suite Execution")
        print(e)
        print('###########################################################')
