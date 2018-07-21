"""
Assumption:

All features are integers (categorical variables) or float values.
The test assumes all values are Numbers.
"""

from utils.test_utils import *
import os


def feature_type_test(df):
    """

    :param df:
    :return:
    """
    columns = list(df.columns)
    missing_feature_types = []
    for each in columns:
        try:
            df[each].sum()
        except Exception as e:
            missing_feature_types.append(each)
    if len(missing_feature_types) > 0:
        feature_type_test_root_cause(df, missing_feature_types)
        test_result_handler("Test 1A: Feature Type", False,
                            "Some columns had non Numerical Values in columns.", missing_feature_types)
    else:
        test_result_handler("Test 1A: Feature Type Test", True)



def feature_type_test_root_cause(df, columns):
    """

    :param df:
    :param columns:
    :return:
    """
    for each in columns:
        df[each] = df[each].apply(lambda x: convert_to_float(x, each))


def convert_to_float(x, each):
    """

    :param x:
    :param each:
    :return:
    """
    try:
        return float(x)
    except Exception as e:
        print(e)
        print(each)
        print(x)
        print(type(x))
        return 0