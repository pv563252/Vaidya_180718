"""

"""

import os
from utils.test_utils import *


def response_classification(df):
    """

    :param df:
    :return:
    """
    begin_test_message("Test 1: Response Classification.")
    column_level_1 = 'ER34111'
    column_level_2 = ['ER34112', 'ER34113', 'ER34114']
    for each in column_level_2:
        df_1 = respondent_level_test_1(df, column_level_1, each)
        df_2 = respondent_level_test_2(df, column_level_1, each)
        output = df_1.join(df_2, [column_level_1, each], "inner")
        root_cause_analysis(output, each)
    end_test_message("Test 1: Response Classification.")


def respondent_level_test_1(df, column_1, column_2):
    """

    :param df:
    :param column_1:
    :param column_2:
    :return:
    """
    df = df.select(column_1, column_2, 'zeros', 'non_zeros')
    return df.groupby(column_1, column_2).avg().select(column_1, column_2, 'avg(zeros)', 'avg(non_zeros)')


def respondent_level_test_2(df, column_1, column_2):
    """

    :param df:
    :param column_1:
    :param column_2:
    :return:
    """
    df = df.select(column_1, column_2)
    return df.groupby(column_1, column_2).count()


def root_cause_analysis(quality_frame, each):
    """

    :param quality_frame:
    :param each:
    :return:
    """
    path = os.getcwd().split('code')[0] + 'out/data_quality/respondent_test/'
    if not(os.path.exists(path)):
        os.mkdir(path)
    quality_frame.toPandas().to_csv(path + each + "_root_cause.csv", index=False)
