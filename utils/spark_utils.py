"""

"""

import findspark
import pyspark
import os


class SparkUtils:
    def __init__(self):
        """

        """
        findspark.init()
        self.sparkContext = pyspark.SparkContext(appName="test")
        self.sqlContext = pyspark.SQLContext(self.sparkContext)

    def write_spark_df_to_csv(self, spark_df):
        """
        Function to write Spark Dataframe to CSV in /out
        :param spark_df: Spark Dataframe
        :return: True, if process is successful
        """
        cwd = os.getcwd()
        cwd = cwd.split('src')[0] + 'out'
        spark_df.write.csv(cwd + "/wordcounts_spark.csv")

    def write_spark_df_to_pandas_to_csv(self, spark_df):
        """

        :param spark_df:
        :return:
        """
        cwd = os.getcwd()
        cwd = cwd.split('src')[0] + 'out'
        spark_df.toPandas().to_csv(cwd + "/wordcounts_pandas.csv", index=False)

    def close_spark(self):
        del self.sqlContext
        del self.sparkContext
