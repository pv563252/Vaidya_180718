from pyspark.ml.clustering import KMeans
import pandas as pd
from utils import spark_utils
from pyspark.ml.stat import Correlation
from pyspark.ml.clustering import GaussianMixture
from pyspark.ml.linalg import Vectors
from pyspark.sql.types import *
import functools
import io


spark = spark_utils.SparkUtils()
sql = spark.sqlContext

df = pd.read_excel('/Users/pv/Desktop/jpmc_rse_assignment/jpmc_rse_assignment_data.xlsx')


def clean_dataframe(df):
    """

    :param df:
    :return:
    """
    for each in list(df.columns):
        try:
            df[each] = df[each].apply(lambda x: convert_to_float(x, each))
            df['features'] = df[each]
            data = df['features']
            # floatRDD = spark.sparkContext.parallelize(data)
            df = spark.sqlContext.createDataFrame(data, FloatType())
            df.schema
            kmeans = KMeans(k=2, seed=1)
            model = kmeans.fit(df)
            centers = model.clusterCenters()
            model.computeCost(df)
            transformed = model.transform(df)
            rows = transformed.collect()
            print(rows)
        except Exception as e:
            print(e)
            print(each)
    return df


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


# def create_vectors(df):
#     data = []
#     for index, row in df.iterrows():
#         data.append(Vectors.dense(list(row)))
#     return data


#
df = clean_dataframe(df)
# spark_df = sql.createDataFrame(df)
# rdd = spark_df.rdd
# kmeans = KMeans(k=2, seed=1)
# model = kmeans.fit(rdd)

# data = create_vectors(df)
# df = sql.createDataFrame(data, ["features"])
# kmeans = KMeans(k=2, seed=1)
# model = kmeans.fit(df)
# centers = model.clusterCenters()
# model.computeCost(df)
#
#
# transformed = model.transform(df).select("features", "prediction")
# rows = transformed.collect()
# print(rows)


# rdd = spark_df.rdd
# model = GaussianMixture.train(rdd, 3, convergenceTol=0.0001, maxIterations=50, seed=10)
# labels = model.predict(rdd).collect()
# print(labels)


