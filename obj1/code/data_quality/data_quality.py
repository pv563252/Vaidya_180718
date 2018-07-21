import pandas as pd
from utils.test_utils import *
from utils.spark_utils import SparkUtils
from obj1.code.data_quality.response_classification import response_classification


def data_anomalies():
    """

    :return:
    """
    try:
        begin_test_message("Starting Quality Test Suite")
        df = pd.read_excel('/Users/pv/Desktop/jpmc_rse_assignment/jpmc_rse_assignment_data.xlsx')
        df = preprocessing(df)
        df = load_data_to_spark(df)
        response_classification(df)
    except Exception as e:
        print('###########################################################')
        print("An Error happened during Quality Test Suite Execution")
        print(e)
        print('###########################################################')


def preprocessing(df):
    """

    :param df:
    :return:
    """
    remove_columns = ['ER34111', 'ER34112', 'ER34113', 'ER34114']
    columns = set(df.columns).difference(remove_columns)
    df['zeros'] = df.apply(lambda x: count_zeros(x, columns), axis=1)
    df['non_zeros'] = df.apply(lambda x: count_non_zeros(x, columns), axis=1)
    return df[['ER34111', 'ER34112', 'ER34113', 'ER34114', 'zeros', 'non_zeros']]


def count_zeros(x, columns):
    """

    :param x:
    :return:
    """
    count = 0
    for each in columns:
        if x[each] == 0:
            count += 1
    return count


def count_non_zeros(x, columns):
    """

    :param x:
    :return:
    """
    count = 0
    for each in columns:
        if x[each] != 0:
            count += 1
    return count


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
