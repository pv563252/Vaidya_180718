import os
from utils.test_utils import *
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import VectorAssembler


def bucketing_for_variable(df, columns):
    """
    KMeans Clustering Based Test for testing the Anomalies in the data.
    :param df: SparkDf object
    :param columns: list of columns
    :return:  Runs successfully for correct config of dataset, console outputs errors otherwise.
    """
    error_columns = []
    begin_test_message("Test 1: Bucket Test.")
    for each in columns:
        test, result = kmeans(df, each)
        if result:
            print(test)
            root_cause_analysis(result, each)
            error_columns.append(each)
    if len(error_columns) > 0:
        test_result_handler("Test 1: Feature Bucket Test", False,
                            "Some columns had anomalies in values.", set(error_columns))
    else:
        test_result_handler("Test 1: Feature Bucket Test", True)


def kmeans(df, column):
    """
    Code to implement the clustering and assign data points to clusters
    :param df: Sparkdf
    :param column: Column Under Evaluation
    :return: SparkDf from anomalous values.
    """
    filtered = df.select(column)
    vectorAss = VectorAssembler(inputCols=filtered.columns, outputCol="features")
    vdf = vectorAss.transform(filtered)
    kmeans = KMeans(k=3, maxIter=10, seed=1)
    model = kmeans.fit(vdf)
    print(model)
    wssse = model.computeCost(vdf)
    print("Within Set Sum of Squared Errors = " + str(wssse))
    return one_simple_test(model.transform(vdf), model.clusterCenters())


def one_simple_test(transformed, centers):
    """
    Simple test to evaluate the ability of Kmeans clustering to detect anomalies in the given dataset.
    :param transformed: Fitted SparkDf with predicted cluster values.
    :param centers: Cluster centers after Kmeans
    :return: True if test fails, False otherwise
    """
    count = 0
    for each in centers:
        if int(each[0]) == 0:
            transformed = transformed.filter(transformed["prediction"] == count)
            return True, transformed.groupby("features", "prediction").count()
        count += 1
    return False, False


def root_cause_analysis(anomaly_frame, each):
    """
    Function to save the output for root cause analysis.
    :param anomaly_frame: SparkDf object
    :param each: Column Name
    :return: write data to output.
    """
    path = os.getcwd().split('code')[0] + 'out/data_anomaly_detection/bucket_test/'
    if not(os.path.exists(path)):
        os.mkdir(path)
    anomaly_frame.toPandas().to_csv(path + each + "_root_cause.csv", index=False)
