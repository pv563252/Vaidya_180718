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
    begin_test_message("Test 1: Range Test.")
    range = read_json(range_path)
    headers = range.keys()
    spark_df = load_data_to_spark(df)
    # for each in headers:
    #
    #
    # found = set(df_columns)
    # missing_features(expected, found)
    # additional_features(expected, found)
    # end_test_message("Test 1: Feature Test.")


def load_data_to_spark(df):
    sql = SparkUtils().sqlContext
    spark_df = sql.createDataFrame(df)
    spark_df.show()
    return spark_df
