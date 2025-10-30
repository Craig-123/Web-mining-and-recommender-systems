# Pattern Mining with Association Rules

## Overview
This Jupyter notebook demonstrates Market Basket Analysis (MBA) and association rule mining using transactional data. It walks through the steps of loading, preprocessing, and mining association rules with the Apriori algorithm, culminating in insights about frequently co-occurring items.

## Objectives
- Load and preprocess transactional dataset
- Apply the Apriori algorithm for mining frequent itemsets
- Generate and interpret association rules using support, confidence, and lift metrics
- Explore, sort, and visualize association rules for actionable patterns

## Dataset
- **Source:** `storedata.csv` (contains transaction data, each row is a transaction listing purchased items)
- **Format:** Items are tabular and organized so that each transaction may have multiple items, some fields may be NaN if the transaction is shorter than max width.

## Workflow

### 1. Initialization
- Imports essential libraries: `numpy`, `pandas`, `matplotlib`, and `apyori` for rule mining

### 2. Data Loading & Exploration
- Reads the transactions from `storedata.csv` into a pandas DataFrame and inspects data shape and contents

### 3. Data Preprocessing
- Converts the DataFrame into a list of lists, where each sublist contains the items of one transaction (excluding NaN)

### 4. Association Rule Mining
- Runs the Apriori algorithm with user-defined thresholds (e.g., minimum support, confidence, lift, and itemset length)
- Generates association rules and stores them in a result list

### 5. Results Analysis
- Prints sample rules along with their support, confidence, and lift
- Converts mined rules into a structured pandas DataFrame for sorting and inspection
- Sorts and displays rules by various metrics: length of antecedent, confidence, support

### 6. Application Example
- Repeats rule mining on an additional `"transactions.txt"` dataset (steps for other datasets included as a use case)

## Outputs
- Frequent itemsets and association rules in DataFrame form
- Detailed statistics about support, confidence, and lift for each rule
- Lists and tables of sorted and filtered rules for further insight

