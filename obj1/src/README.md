# Data Integrity

Using a modified version of the Panel Study of Income Dynamics, produced by the University of Michigan - the code provided in the /code directory establishes multiple tests for Data Integrity Checks.


## Ground Zero Test

Given the dataset, this test deals with simple issues in the dataset that could lead to potential problems in the future analysis. These issues can arise from the file being handled by multiple users in the value stream, consequently passing the data through multiple systems. Typically the errors introduced in this process include rounding off errors (float to integer) or sorting one column only without sorting the entire dataset.

The problem can be solved by standardization practices. Common problems include:

* File Format Issue: Given file format does not match the expected/agreed upon format.
* Column Name Mapping Issues: Given dataset has missing columns.
* Column Type Mapping Issues: Given dataset, and expected column types, the column types interpreted by the reader are different from expected. This could happen for a variety of reasons including missing values.

A simple test for these issues is to try loading the data into the analytics stack, and track the issues. Tracking the issues also allows to add these issues into an ongoing test framework, to avoid future issues of similar types.


## Data Integrity

Given the dataset, the most important data integrity questions to ask the dataset are:

* _Is the Dataset missing values? How were the missing values dealt with? Are there outliers in the data?_
* _Is the Dataset Randomized, or is it Biased in a particular Way?_
* _Are the features in the dataset independent of each other, or what part of the dataset is useful for the analysis?_

These questions are directly tied to the outcomes of the research, thereby indicating Research Readiness of the dataset. Since, these tests are closer to the analytics or modelling itself, they require a deep understanding of the problem, as well as the Data Source.


## Test Definition: Missing Value Checks

* Summary Statistics for Features
*
*


## Test Definition: Dataset Bias Checks

*
*
*


## Test Definition: Dataset Feature Checks

*
*
*


## References:

The key references used in formulating the tests are recorded here:

* [PSID Documentation](https://psidonline.isr.umich.edu/Guide/default.aspx)
* [Data Readiness Levels](https://arxiv.org/pdf/1705.02245.pdf)
