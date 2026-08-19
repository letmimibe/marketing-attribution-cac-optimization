import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

dates = [datetime(2026, 1, 1) + timedelta(days=i) for i in range(180)]
channels = ['Meta Ads', 'Google Ads', 'TikTok Ads', 'Organic Search', 'Direct']

# Generate ad spend dataset
spend_data = []
for d in dates:
    for ch in ['Meta Ads', 'Google Ads', 'TikTok Ads']:
        spend = np.random.uniform(50, 300)
        impressions = int(spend * np.random.uniform(80, 120))
        clicks = int(impressions * np.random.uniform(0.015, 0.04))
        spend_data.append([d.strftime('%Y-%m-%d'), ch, round(spend, 2), impressions, clicks])

df_spend = pd.DataFrame(spend_data, columns=['date', 'channel', 'spend_usd', 'impressions', 'clicks'])
df_spend.to_csv('ad_spend.csv', index=False)

# Generate e-commerce transaction dataset
orders = []
for i in range(3500):
    date = np.random.choice(dates)
    ch = np.random.choice(channels, p=[0.35, 0.25, 0.20, 0.12, 0.08])
    user_id = f"USR-{np.random.randint(1000, 2500)}"
    order_val = round(np.random.uniform(15, 120), 2)
    orders.append([f"ORD-{10000+i}", user_id, date.strftime('%Y-%m-%d'), ch, order_val])

df_orders = pd.DataFrame(orders, columns=['order_id', 'user_id', 'order_date', 'channel', 'order_value_usd'])
df_orders.to_csv('transactions.csv', index=False)

print("Successfully generated 'ad_spend.csv' and 'transactions.csv'.")