"""

"""
from utils.extractor_utils import read_json
from utils.test_utils import *
from utils.spark_utils import SparkUtils
import os


def feature_range_test(df, range_path=os.getcwd()+'/range.json'):
    """

    :param df:
    :param range_path:
    :return:
    """
    begin_test_message("Test 2: Range Test.")
    range = read_json(range_path)
    spark = SparkUtils()
    spark_df = load_data_to_spark(df, spark)
    columns = []
    for each in range.keys():
        anomalies_high = spark_df.filter(spark_df[each] > range[each]['high'])
        if bool(anomalies_high.head(1)):
            root_cause_analysis(anomalies_high, each, high=True)
            columns.append(each)
        anomalies_low = spark_df.filter(spark_df[each] < range[each]['low'])
        if bool(anomalies_low.head(1)):
            root_cause_analysis(anomalies_low, each)
            columns.append(each)
    if len(columns) > 0:
        test_result_handler("Test 2: Feature Range Test", False,
                            "Some columns had values outside of expected values", set(columns))
    else:
        test_result_handler("Test 2: Feature Range Test", True)
    spark.close_spark()


def root_cause_analysis(anomaly_frame, each, high=False):
    """

    :param anomaly_frame:
    :param each:
    :param high:
    :return:
    """
    path = os.getcwd().split('code')[0] + 'out/data_hygiene/range_test/' + each
    if not(os.path.exists(path)):
        os.mkdir(path)
    if high:
        path += '/high_anomalies.csv'
    else:
        path += '/low_anomalies.csv'
    anomaly_frame.toPandas().to_csv(path, index=False)


def load_data_to_spark(df, spark):
    """

    :param df:
    :return:
    """
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
    return df


def convert_to_float(x):
    """

    :param x:
    :return:
    """
    try:
        return float(x)
    except Exception as e:
        return 0
