# Data Integrity

Using a modified version of the Panel Study of Income Dynamics, produced by the University of Michigan - the code provided in the /code directory establishes multiple tests for Data Integrity Checks.



{% tabs %}
{% tab title="First Tab" %}
blah blah 
{% endtab %}

{% tab title="blah blah" %}

{% endtab %}
{% endtabs %}

## Ground Zero Test

Given the dataset, this test deals with simple issues in the dataset that could lead to potential problems in the future analysis. These issues can arise from the file being handled by multiple users in the value stream, consequently passing the data through multiple systems. Typically the errors introduced in this process include rounding off errors \(float to integer\) or sorting one column only without sorting the entire dataset.

The problem can be solved by standardization practices. Common problems include:

1. File Format Issue _Implemented_ 1. Given file format does not match the expected/agreed upon format. 2. A simple test for these issues is to try loading the data into the analytics stack.
2. Column Mapping Issues _Implemented_: 1. Given dataset, and expected columns, the columns interpreted by the reader are different from expected. 2. Given dataset, and expected column types, the columns interpreted by the reader are different from expected. 3. This could happen for a variety of reasons including missing features, as well as file format issues \(expected comma as delimiter but got tabs, etc.\).

Tracking the issues also allows to add these issues into an ongoing test framework, to avoid future issues of similar types.

## Data Integrity and Data Readiness

Given the dataset, the most important data integrity questions to ask the dataset are:

1. Data Hygiene: 1. Is the Dataset _Complete_? 2. Is the Dataset incomplete values or features? 3. How were the missing values dealt with?
2. Data Outliers: 1. Are there outliers in the data?
3. Dataset Quality: 1. Studying the responded, and missing values. 2. Is the Dataset Randomized, or is it Biased in a particular Way?

These questions are directly tied to the outcomes of the research, thereby indicating Research Readiness of the dataset. Since, these tests are closer to the analytics or modelling itself, they require a deep understanding of the problem, as well as the Data Source.

## Test Definition: Data Hygiene

1. Missing Feature Values due to Errors _Implemented_ 1. Statistical Analysis of missing values, as well as range analysis, using the Dataset information provided in the document. 2. Building a threshold to understand if these errors are statistically significant to call out, and if they would impact the final analysis.
2. Missing Feature Values due to Data Collection Errors 1. The test is designed to address the question _How were the missing values dealt with?_ 2. The Data Dictionary Document provides an overview of how the missing values are dealt with. For eg. Code '0' for no response in some cases. 3. The test checks for these missing values, and summarizes them to be able to assess what part of the data is actually usable.
3. Upstream Data Wrangling Errors _Implemented_ 1. Data could have been corrupted due to manual data entry errors in the upstream process during De-Identification, or other tasks. 2. Loss of Information during Upstream automated analysis could also happen based on treatment of feature data types. For example: conversion of base float values to integers, etc. 3. Some algorithms exist to test this, but a better understanding of the upstream process would allow for a better test suite recommendation.

## Test Definition: Anomaly Detection

1. Statistical Anomaly Detection for Categorical Features _Implemented_ 1. Bucketing the data into different groups, and analyzing the buckets. 2. Each of the bucket corresponding to the feature must only have the categories
2. Anomaly Detections using Unsupervised Learning: Principal Component Analysis 1. Given that we have no understanding of the truth-set or training data, we can use Principal Component Analysis. 2. PCA allows us to define the normal patterns, and these normal patterns can be used to identify outliers.
3. Anomaly Detections using Unsupervised Learning: Clustering 1. Given that we have no understanding of the truth-set or training data, we can use K-Means clustering, and Hierarchical K-Means clustering to fit the data. 2. Build out the threshold with the distance metric to identify outliers.

## Test Definition: Dataset Quality Checks

1. Statistical Summary Data Quality Checks 1. The test pertains to stats such as Mean, Median, Highest, Lowest Values, percentiles. _Implemented_ 2. Visualizations such as histograms, box-plot analysis, density analysis can also be used in these tests.
2. Selection Bias _Implemented_ 1. In statistics, self-selection bias arises in any situation in which individuals select themselves into a group, causing a biased sample with nonprobability sampling. Makes causation more difficult. 2. It is commonly used to describe situations where the characteristics of the people which cause them to select themselves in the group create abnormal or undesirable conditions in the group. 3. It is closely related to the non-response bias, describing when the group of people responding has different responses than the group of people not responding. 4. In the implementation that I use, I am going to test the feature set to establish data quality.
3. Attrition 1. In order to have this view of the data, we would need to conduct year over year analysis, which would include fusing datasets together. 2. An attrition rate of under 5% is usually no concern \(Schulz and Grimes, 2002\), while rates in excess of 20% may be cause for concern. However, these aren’t steadfast rules — a study with a low attrition rate might be more susceptible to bias than a study with a higher attrition rate if the drop-outs have very unique characteristics.

## Other important considerations not covered in the tests above:

* _Ability to fuse data with other Datasets_:
  * This could include availability of join keys or mapping tables that join this dataset to other internal and external datasets.
  * In the absence of these join keys, or where a join is not possible, computing clusters and cluster distance to get a _close match_ can be used.
* _Custom Anomaly Detection_:
  * Given Unsupervised Anomaly Detection methods in place, over time, we would have enough data to build a balanced training set, and use it for supervised Anomaly Detection.

## References:

The key references used in formulating the tests are recorded here:

* [PSID Documentation](https://psidonline.isr.umich.edu/Guide/default.aspx)
* [Data Readiness Levels](https://arxiv.org/pdf/1705.02245.pdf)

