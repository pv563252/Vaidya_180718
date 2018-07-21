# Vaidya\_180718

The repository houses Data Integrity Checks using Spark and Python.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Additional technical details supporting this document are housed [HERE](https://www.gitbook.com/invite/vaidya-180718?invite=-LHk597zA10a1moBaC12)

### Prerequisites

In order to run this code, your system must have the Spark already installed.

```text
Spark Version 2.2.0
Python 3.6.5
```

### Installing

A step by step series of examples that tell you how to get a development env running.

After cloning the repository, run the following command in you shell in the root directopry of the project to download all packages required to run the code.

```text
pip install -r requirements.txt
```

## Running the Environment Test

To make sure that your environment is running correctly run the test housed in /src/test.py

### Test Run

The test reads a file from the [README](https://raw.githubusercontent.com/ToJen/Quorum-Enterprise-Blockchain/master/README.md), and counts the number of words in the file.

### Validating The Test

The test creates output files, and console output. A successful test run with no error messages indicates that the environment has been setup correctly.

```text
###########################################################
Test Ran Successfully!
###########################################################
```

