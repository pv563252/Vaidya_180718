# Vaidya_180718

The repository houses Data Integrity Checks using Spark and Python.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

In order to run this code, your system must have the Spark already installed.

```
Spark Version 2.2.0
Python 3.6.5
```

### Installing

A step by step series of examples that tell you how to get a development env running.

After cloning the repository, run the following command in you shell in the root directopry of the project to download all packages required to run the code.

```
pip install -r requirements.txt
```


## Running the Environment Test

To make sure that your environment is running correctly run the test housed in /src/test.py


### Test Run

The test reads a file from the [README](https://raw.githubusercontent.com/ToJen/Quorum-Enterprise-Blockchain/master/README.md), and counts the number of words in the file.


### Validating The Test

The test creates output files, and console output. A successful test run with no error messages indicates that the environment has been setup correctly.

```
###########################################################
Test Ran Successfully!
###########################################################
```
