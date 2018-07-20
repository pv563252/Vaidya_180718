# Data Integrity

Using a modified version of the Panel Study of Income Dynamics, produced by the University of Michigan - the code provided in the /code directory establishes multiple tests for Data Integrity Checks.


## Ground Zero Test

Given the dataset, this test deals with simple issues in the dataset that could lead to potential problems in the future analysis. These issues can arise from the file being handled by multiple users in the value stream, consequently passing the data through multiple systems. Typically the errors introduced in this process include rounding off errors (float to integer) or sorting one column only without sorting the entire dataset.

The problem can be solved by standardization practices. Common problems include:


1.  File Format Issue:
    1. Given file format does not match the expected/agreed upon format.
    2. A simple test for these issues is to try loading the data into the analytics stack.

2. Column Mapping Issues _Implemented_:
    1. Given dataset, and expected columns, the columns interpreted by the reader are different from expected.
    2. This could happen for a variety of reasons including missing features, as well as file format issues (expected comma as delimiter but got tabs, etc.).


Tracking the issues also allows to add these issues into an ongoing test framework, to avoid future issues of similar types.


## Data Integrity and Data Readiness

Given the dataset, the most important data integrity questions to ask the dataset are:

* _Is the Dataset Complete? Is the Dataset missing values or features? How were the missing values dealt with?_
* _Are there outliers in the data?_
* _Is the Dataset Randomized, or is it Biased in a particular Way?_

These questions are directly tied to the outcomes of the research, thereby indicating Research Readiness of the dataset. Since, these tests are closer to the analytics or modelling itself, they require a deep understanding of the problem, as well as the Data Source.


## Test Definition: Data Hygiene

* _Missing Feature Values due to Errors_:
        - Statistical Analysis of missing values, as well as range analysis, using the Dataset information provided in the document.
        - Building a threshold to understand if these errors are statistically significant to call out, and if they would impact the final analysis.
* _Missing Feature Values to Data Collection Errors_:
        - The test is designed to address the question _How were the missing values dealt with?_
        - The Data Dictionary Document provides an overview of how the missing values are dealt with. For eg. Code '0' for no response in some cases.
        - The test checks for these missing values, and summarizes them to be able to assess what part of the data is actually usable.
* _Upstream Data Wrangling Errors_:
        - Data could have been corrupted due to manual data entry errors in the upstream process during De-Identification, or other tasks.
        - Some algorithms exist to test this, but a better understanding of the upstream process would allow for a better test suite recommendation.


## Test Definition: Anomaly Detection

The test included are conducted on a multivariate level, as well as assessing each feature individually.

* _Statistical Anomaly Detection for Features_:
        - Outcomes include stats such as Mean, Median, Highest, Lowest Values.
        - Visualizations like Box-Plot can be used to analyze the data for the outliers in the dataset feature, as well as compare multiple feature sets.
* _Anomaly Detections using Unsupervised Learning: Principal Component Analysis_:
        - Given that we have no understanding of the truth-set or training data, we can use Principal Component Analysis.
        - PCA allows us to define the normal patterns, and these normal patterns can be used to identify outliers.
* _Anomaly Detections using Unsupervised Learning: Clustering *Implmented*:
        - Given that we have no understanding of the truth-set or training data, we can use K-Means clustering, and Hierarchical K-Means clustering to fit the data.
        - Visually look at the data for outliers.


## Test Definition: Dataset Bias Checks

The test included are conducted on a mulitvariate level, assessing each feature with respect to other features.

*
*
*


## Other important considerations not covered in the tests above:

* _Ability to fuse data with other Datasets_:
        - This could include availability of join keys or mapping tables that join this dataset to other internal and external datasets.
        - In the absence of these join keys, or where a join is not possible, computing clusters and cluster distance to get a _close match_ can be used.
* _Custom Anomaly Detection *Future Scope*_:
        - Given Unsupervised Anomaly Detection methods in place, over time, we would have enough data to build a balanced training set, and use it for supervised Anomaly Detection.


## References:

The key references used in formulating the tests are recorded here:

* [PSID Documentation](https://psidonline.isr.umich.edu/Guide/default.aspx)
* [Data Readiness Levels](https://arxiv.org/pdf/1705.02245.pdf)
