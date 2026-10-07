# Retail Data Pipeline

An end-to-end retail data engineering project that demonstrates data ingestion, data quality validation, transformation, SQL analytics, database loading, and Power BI visualization.

The project takes raw retail order data through an ETL pipeline and converts it into clean, analysis-ready data for business insights.

---

## Project Overview

This project simulates a real-world retail data engineering workflow.

The pipeline:

1. Ingests raw retail order data from CSV
2. Performs data quality checks
3. Cleans and transforms the data
4. Creates calculated sales metrics
5. Loads the processed data into a SQLite database
6. Performs SQL-based business analysis
7. Visualizes the results using Power BI

The project was designed to demonstrate practical skills in **Python, SQL, ETL, data cleaning, data quality, database management, and data visualization**.

---

## Architecture

```text
Raw CSV Data
     |
     v
Data Ingestion
     |
     v
Data Quality Checks
     |
     v
Data Cleaning & Transformation
     |
     v
Processed CSV
     |
     v
SQLite Database
     |
     v
SQL Analytics
     |
     v
Power BI Dashboard
