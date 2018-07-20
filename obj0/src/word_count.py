"""

"""

from utils.spark_utils import SparkUtils
from utils.extractor_utils import url_text_reader, writer
import os
import re


def word_count():
    """

    :return:
    """
    spark = SparkUtils()
    path = pre_processing()
    try:
        input = spark.sparkContext.textFile(path)
        words_rdd = input.flatMap(normalize_words).filter(lambda x: len(x) > 0)
        words_rdd_counts = words_rdd.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
        word_rdd_counts_sorted = words_rdd_counts.map(lambda x: (x[1], x[0])).sortByKey(ascending= False)
        word_rdd_counts_sorted_df = spark.sqlContext.createDataFrame(word_rdd_counts_sorted, ["Count", "Word"])
        write_results(word_rdd_counts_sorted_df, spark)
    except Exception as e:
        print('###########################################################')
        print("An Error happened during computation of Word Counts:")
        print(e)
        print('###########################################################')
    finally:
        os.remove(path)
        spark.close_spark()



def write_results(spark_df, spark):
    """

    :param spark_df:
    :param spark:
    :return:
    """
    spark.write_spark_df_to_csv(spark_df)
    spark.write_spark_df_to_pandas_to_csv(spark_df)
    return True


def normalize_words(text):
    """

    :param text:
    :return:
    """
    return re.compile(r'\W+', re.UNICODE).split(text.lower())


def pre_processing():
    """

    :return:
    """
    filepath = os.getcwd() + "/testfile.txt"
    text = url_text_reader(url="https://raw.githubusercontent.com/ToJen/Quorum-Enterprise-Blockchain/master/README.md")
    writer(text, filepath)
    return filepath


word_count()
