import sqlite3
import pandas as pd

# Load input CSV datasets
df_spend = pd.read_csv("ad_spend.csv")
df_orders = pd.read_csv("transactions.csv")

# Initialize in-memory SQLite database
conn = sqlite3.connect(":memory:")
df_spend.to_sql("ad_spend", conn, index=False, if_exists="replace")
df_orders.to_sql("transactions", conn, index=False, if_exists="replace")

# Query marketing attribution metrics: Spend, Revenue, CAC, and ROAS by channel
sql_query = """
WITH SpendSummary AS (
    SELECT 
        channel,
        SUM(spend_usd) AS total_spend,
        SUM(clicks) AS total_clicks
    FROM ad_spend
    GROUP BY channel
),
RevenueSummary AS (
    SELECT 
        channel,
        COUNT(DISTINCT order_id) AS total_orders,
        COUNT(DISTINCT user_id) AS total_customers,
        SUM(order_value_usd) AS total_revenue
    FROM transactions
    GROUP BY channel
)
SELECT 
    r.channel,
    COALESCE(s.total_spend, 0) AS spend_usd,
    ROUND(r.total_revenue, 2) AS revenue_usd,
    r.total_orders,
    r.total_customers,
    ROUND(s.total_spend / NULLIF(r.total_customers, 0), 2) AS cac_usd,
    ROUND(r.total_revenue / NULLIF(s.total_spend, 0), 2) AS roas
FROM RevenueSummary r
LEFT JOIN SpendSummary s ON r.channel = s.channel
ORDER BY revenue_usd DESC;
"""

# Execute SQL query and fetch results
df_result = pd.read_sql_query(sql_query, conn)
print("\n=== MARKETING ATTRIBUTION ANALYSIS RESULTS ===")
print(df_result.to_string(index=False))

# Export aggregated metrics for downstream visualization
df_result.to_csv("attribution_result.csv", index=False)
print("\nAnalysis results successfully exported to 'attribution_result.csv'.")