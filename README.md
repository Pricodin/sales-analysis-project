# Simple Data Analyst Project: Retail Sales Analysis

A beginner-friendly end-to-end project: understand, clean, explore, visualize, report.
The data is SYNTHETIC (made up for practice) and contains deliberate errors to clean.

## Structure
- data/raw/sales_raw.csv          original messy data (never edited)
- data/processed/sales_clean.csv  cleaned data
- src/generate_data.py            creates the practice dataset
- src/analysis.py                 cleaning + EDA + charts + report
- sql/queries.sql                 SQL practice queries
- outputs/report.md               final report; outputs/charts/ has 6 charts

## Run
    pip install -r requirements.txt tabulate
    python src/generate_data.py
    python src/analysis.py

## Use your own data
Put your CSV in data/raw/ and adjust column names in src/analysis.py.
