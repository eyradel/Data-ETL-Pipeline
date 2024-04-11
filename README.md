---

# Data Integration with Pandas and PySpark

This repository contains Python code for integrating data from multiple sources using the Pandas library for data manipulation and PySpark for distributed processing.

## Getting Started

To run the code in this repository, you'll need to have Python installed on your system. Additionally, make sure to install the required libraries by running:

```bash
pip install pandas pyspark
```

## Usage

The code provided in `data_integration.py` demonstrates how to integrate data from various sources using Pandas and PySpark. Here's an overview of the steps performed:

1. **Importing Libraries:**
   - `import pandas as pd`: Importing the Pandas library as `pd`.
   - `from pyspark.sql import SparkSession`: Importing the `SparkSession` class from PySpark.

2. **Reading Data:**
   - `market1customers = pd.read_json(r"Market 1 Customers.json")`: Reading data from a JSON file using Pandas.
   - `market1deliveries = pd.read_csv(r"Market 1 Deliveries.csv")`: Reading data from a CSV file using Pandas.
   - Similar operations for other market data.

3. **Merging Data:**
   - Merging customer data from market 1 and market 2 using `pd.merge()` based on the 'Customer ID'.
   - Merging order data from market 1 and market 2 using `pd.merge()` based on the 'Order ID'.
   - Merging delivery data from market 1 and market 2 using `pd.merge()` based on the 'Task_ID'.

4. **Initializing SparkSession:**
   - Creating a SparkSession using `SparkSession.builder.getOrCreate()`.

