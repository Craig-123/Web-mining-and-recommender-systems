# Web Usage Mining Analytics

## Overview
This Jupyter notebook analyzes and mines patterns from Apache web server logs. It demonstrates how to parse, process, and extract insights such as session statistics, referrer analysis, frequent visitors, and page association patterns.

## Objectives
- Parse and preprocess raw web log data
- Extract sessions and user access patterns
- Analyze page view trends and referrer sources
- Perform association rule mining to discover frequent page combinations

## Dataset
- **Input file:** `apachelogs.txt` (Apache HTTP access log)
- **Parsed fields:** IP address, timestamp, requested resource, referrer, user agent, status code, object size

## Workflow

### 1. Data Parsing & Preprocessing
- Defines Python functions for extracting strings, integers, and datetime values with timezones
- Loads log entries into Pandas DataFrame
- Cleans and casts data types for analysis

### 2. Exploratory Analysis
- Identifies unique and frequent IP + device pairs
- Samples log entries for overview
- Separates sessions and page activities

### 3. Session & Page View Stats
- Tracks sessions and pageview counts per session/user
- Summarizes session-wise activity

### 4. Referrer Analysis
- Parses and counts referrers to highlight top referral sources

### 5. Frequent Pattern Mining
- Aggregates visited pages by session/client
- Applies the Apriori algorithm (`apyori`) to discover common sets of pages accessed together
- Outputs itemsets with support, confidence, and lift metrics

## Outputs
- Top visitor/client pairs
- Leading referrer domains
- Frequent page combinations and association rules

## Notes
- Modular functions for parsing and preprocessing
- Results may vary with different web log inputs
- Apriori rule thresholds can be tuned


