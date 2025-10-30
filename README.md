# Data Mining & Text Mining Project Suite

This repository contains analytic and mining projects spanning web usage analysis, pattern mining, and a full-scale newspaper text mining and recommendation platform.

---

## Projects Overview

### 1. Newspaper Text Mining and Recommendation Platform

**Description:**  
End-to-end NLP and web mining solution for extracting, classifying, and recommending news content from multiple online sources. The system simulates conversational information extraction as well as enhancement, leveraging an automated Python spider to gather articles from major news outlets and categorize them into Business, Politics, Arts/Culture/Celebrities, and Sports. It converts raw content into structured CSV datasets for downstream analysis.

**Techniques & Tools:**
- Python, web scraping, NLP
- Unsupervised learning (clustering)
- Data engineering (CSV pipelines)
- Web platform deployment (Streamlit)

**Features:**
- Conversational intent classification and news clustering
- Structured CSV output for scalable analytics
- Web interface for exploring topic clusters and related stories

**Deployed Application:**  
[News Text Mining App (Streamlit)](https://web-mining-and-recommender-systems-puf6ohwp.ydd3upj4emcmmn.streamlit.app/)  

---

### 2. Pattern Mining

**Description:**  
A Jupyter notebook implementing Market Basket Analysis (MBA) with the Apriori algorithm for association rule mining. Uses transactional data to identify frequently co-occurring items and actionable association patterns for recommendation or inventory optimization.

**Techniques & Tools:**
- Apriori algorithm (apyori), pandas, numpy
- Data preprocessing and cleaning
- Frequent itemset and association rule generation
- DataFrame-based exploratory analysis and visualization

---

### 3. Web Usage Mining

**Description:**  
A notebook for analyzing web usage patterns from Apache server logs. It parses log entries, reconstructs user sessions, and mines referrer and access statistics. Further applies association rule mining to page visit sequences for behavioral insights.

**Techniques & Tools:**
- Python, pandas, regex, apyori, urllib
- Web log string/date parsing and cleansing
- Sessionization and page path analysis
- Mining and visualizing frequent navigation patterns

---
