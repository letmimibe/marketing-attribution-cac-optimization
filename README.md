# Multi-Channel Marketing Attribution & CAC Optimization

## Executive Summary
This project evaluates multi-channel marketing performance for an e-commerce enterprise to optimize Customer Acquisition Cost (CAC) and Return on Ad Spend (ROAS). Leveraging Python for data pipeline design, SQLite for analytical processing and attribution logic, and Looker Studio for executive visualization, this analysis provides data-driven strategies for cross-channel capital allocation.

## Architecture & Tech Stack
* **Data Ingestion & Simulation:** Python (`pandas`, `numpy`, `datetime`)
* **Data Processing & SQL Analytics:** SQLite, Python (`sqlite3`)
* **Business Intelligence & Visualization:** Looker Studio

## Business Problem & Strategic Objectives
* **Core Problem:** Suboptimal marketing budget distribution across acquisition channels, driving elevated Customer Acquisition Costs (CAC) and margin compression.
* **Primary Objective:** Quantify multi-channel attribution metrics, isolate underperforming acquisition channels, and establish data-backed budget reallocation strategies to maximize total marketing return.

## Key Analytical Insights
1. **Primary Revenue Driver:** Meta Ads generated the highest top-line revenue, though sustained scaling requires continuous ad spend commitment.
2. **Organic Efficiency:** Organic Search and Direct traffic operate with zero direct acquisition cost, significantly blunting aggregate acquisition expenses.
3. **CAC Threshold Variance:** Specific paid channels exceeded the targeted CAC baseline of $15.00, highlighting immediate opportunities for spend re-allocation.

## Dashboard Preview
<img width="1512" height="982" alt="Screenshot 2026-08-19 at 19 02 22" src="https://github.com/user-attachments/assets/1e2ecd98-2e37-45e1-95f5-9f0d2c9a98f1" />


## Execution Instructions
1. Execute `python generate_data.py` to synthesize the raw transaction and ad spend datasets.
2. Execute `python run_analysis.py` to trigger the SQL attribution pipeline and output `attribution_result.csv`.
