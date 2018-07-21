import pandas as pd
from utils.test_utils import *
from utils.spark_utils import SparkUtils
from obj1.code.data_anomaly_detection.bucketing_for_variables import bucketing_for_variable


def data_anomalies():
    """

    :return:
    """
    try:
        begin_test_message("Starting Anomaly Test Suite")
        df = pd.read_excel('/Users/pv/Desktop/jpmc_rse_assignment/jpmc_rse_assignment_data.xlsx')
        columns = list(df.columns)
        df = load_data_to_spark(df)
        bucketing_for_variable(df, columns)
    except Exception as e:
        print('###########################################################')
        print("An Error happened during Anomaly Test Suite Execution")
        print(e)
        print('###########################################################')


def load_data_to_spark(df):
    """

    :param df:
    :return:
    """
    spark = SparkUtils()
    df = clean_df(df, list(df.columns))
    sql = spark.sqlContext
    spark_df = sql.createDataFrame(df)
    return spark_df


def clean_df(df, columns):
    """

    :param df:
    :param columns:
    :return:
    """
    for each in columns:
        df[each] = df[each].apply(lambda x: convert_to_float(x))
    return df.fillna(0)


def convert_to_float(x):
    """

    :param x:
    :return:
    """
    try:
        return float(x)
    except Exception as e:
        return 0


data_anomalies()
