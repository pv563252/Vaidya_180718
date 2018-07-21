---
description: >-
  Using a modified version of the Panel Study of Income Dynamics, produced by
  the University of Michigan - the code provided in the /code directory
  establishes multiple tests for Data Integrity Checks.
---

# Objective 1: Data Integrity

### Data Integrity and Data Readiness Levels 

Given the dataset, the most important data integrity questions to ask the dataset are:

* Data Hygiene:

  1. Is the Dataset _Complete_?
  2. Is the Dataset incomplete values or features?
  3. How were the missing values dealt with?

* Data Outliers:

  1. Are there outliers in the data?

* Dataset Quality:

  1. Is the dataset have enough values to analyze with? 
  2. What part of the dataset is usable?
  3. Is the Dataset Randomized, or is it Biased in a particular Way?

* Research Readiness:
  1. Ability to Fuse with Other Datasets

### Issues in Dataset

#### Non Identifiable Issues

| Issue | Issue Tye |
| --- | --- | --- | --- | --- | --- | --- |
| Data Hygiene | Missing Feature Values due to Data Collection Errors |
| Data Hygiene | Loss of Data due to manual entry errors or System Errors Upstream |
| Outliers | Custom Anomaly Detection |
| Data Quality | Selection Bias |
| Data Quality  | Attrition |
| Research Readiness | Ability to Join with other datasets |



#### Missing Feature Values due to Data Collection Errors

1. The issue addresses the question _How were the missing values dealt with?_
2. The Data Dictionary Document provides an overview of how the missing values are dealt with. For eg. Code '0' for no response in some cases.
3. But even for Code '0', there are multiple reasons for the error, if it exists. There are also cases where represents valid values. 

#### Loss of Data due to Manual Entry Errors or System Errors Upstream

1. Data could have been corrupted due to manual data entry errors in the upstream process during De-Identification, or other tasks.
2. Loss of Information during Upstream automated analysis could also happen based on treatment of feature data types. For example: conversion of base float values to integers in different systems, etc.
3. Manual Errors such as opening the file in excel, sorting by one column, without sorting the entire dataset. 
4. Some algorithms exist to test this, but a better understanding of the upstream process would allow for a better test suite recommendation.

#### Custom Outlier Detection

1. In data mining, **anomaly detection** \(also outlier **detection**\) is the identification of items, events or observations which do not conform to an expected pattern or other items in a dataset.
2. Based on the use-case, custom anomaly detection logic can be achieved to analyze any new data for unsupported or anomalous values. 

#### Selection Bias

1. In statistics, self-selection bias arises in any situation in which individuals select themselves into a group, causing a biased sample with nonprobability sampling. Makes causation more difficult.
2. It is commonly used to describe situations where the characteristics of the people which cause them to select themselves in the group create abnormal or undesirable conditions in the group.
3. It is closely related to the non-response bias, describing when the group of people responding has different responses than the group of people not responding.
4. To test this, a truth or baseline test is needed. 

#### Attrition

1. In order to have this view of the data, we would need to conduct year over year analysis, which would include fusing datasets together.
2. An attrition rate of under 5% is usually no concern \(Schulz and Grimes, 2002\), while rates in excess of 20% may be cause for concern. However, these aren’t steadfast rules — a study with a low attrition rate might be more susceptible to bias than a study with a higher attrition rate if the drop-outs have very unique characteristics.

#### Ability to Fuse with Other Datasets

1. This could include availability of join keys or mapping tables that join this dataset to other internal and external datasets. 
2. In the absence of these join keys, or where a join is not possible, computing clusters and cluster distance to get a _close match_.



### Identifiable Issues

#### Ground Zero Test

Given the dataset, this test deals with simple issues in the dataset that could lead to potential problems in the future analysis. These issues can arise from the file being handled by multiple systems in the value stream:

File Format Issue:

* Given file format does not match the expected/agreed upon format.
* Given dataset, and expected columns, the columns interpreted by the reader are different from expected.
* This could happen for a variety of reasons including missing features, as well as file format issues \(expected comma as delimiter but got tabs, etc.\).
* File format issues can also arise due to system changes upstream. 

File Format Tests:

1. String Path Parsing:
   1. This test can be carried out to parse the file format from the location path of the string. 
   2. The test can detect the presence of an unexpected file format ahead of time, but adds maintenance overhead, with very little visibility into the underlying errors. 
2. Data Load Test: 
   1. This test can be carried out by defining the expected schema in a json format, and try to load data into Spark. 
   2. The error messages from the test do not capture the low level error details.
   3. At run time, the maintainer would spend more time trying to debug the error. 
3. Lower Level Tests: **Implemented**
   1. A simple Feature Presence was implemented in order to analyze the presence of all features.
   2. The implementation is designed to make sure that low-level error details are caught. 

#### Data Hygiene: Incorrect Features Values due to Data Errors

The test defined in this test suite pertain to understanding the underlying feature values in order to establish the correctness of feature values, as well as handle missing values. 

Data Errors:

1. The feature values do not match the values expected. This could happen because of incorrect handling of missing values, data entry errors, formatting errors, etc. 
2. The feature values are missing. This could happen due to data collection errors, and can be remedied by establishing business logic to deal with the errors. 

Data Error Tests:

1. Aggregate Statistical Analysis Tests: 
   1. Testing the dataset with summary statistics such as low, high values. 
   2. This test can be extended to test other details sum as checksums, expected sum, etc. for features, once expected values are established. 
   3. The test does not capture the low level details of the errors, and is not a robust test. 
2. Expected Datatype Tests: **Implemented**
   1. A low level assessment of every variable to check against the expected datatype. 
   2. Every value in the dataset was either of Datatype Float or Integer. Any deviation from that was considered an error, and recorded by the test. 
   3. The code was also reused for cleaning the dataset. At the moment the test handles missing values by substituting with 0. 
   4. The implementation is designed to make sure that low-level error details are caught. 
3. Range Test: **POC** **Implemented** 
   1. This test involves creating a record of the expected values, and the range of expected values. 
   2. The test filtering the column by checking with respect to the expected range. 
   3. The implementation is designed to make sure that low-level error details are caught. 

#### Data Outliers Test: Unexpected Feature Values or Anomalies 

In data mining, **anomaly detection** \(also outlier **detection**\) is the identification of items, events or observations which do not conform to an expected pattern or other items in a dataset.

1. Statistical Anomaly Detection for Categorical Features **POC**

   1. Statistical Summary of dataset features long with percentiles and IQR.
   2. Test the feature value distribution, and detect outliers wrt to Expected. 

2. Anomaly Detections using Unsupervised Learning: Principal Component Analysis

   1. Given that we have no understanding of the truth-set or training data, we can use Principal Component Analysis.
   2. PCA allows us to define the normal patterns, and these normal patterns can be used to identify outliers.
   3. Since PCA converts the feature space to another dimension feature space, makes the results difficult to communicate to stakeholders. 

3. Anomaly Detections using Unsupervised Learning: Clustering **Implemented**
   1. Given that we have no understanding of the truth-set or training data, we can use K-Means clustering, and Hierarchical K-Means clustering to fit the data.
   2. Build out the threshold with the cluster center to identify outliers.
   3. Easy to visualize and communicate. 

#### Data Quality Tests

Data Quality Tests have been carried out keeping in mind the 

#### 





