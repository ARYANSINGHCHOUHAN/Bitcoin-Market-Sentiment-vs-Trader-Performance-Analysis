# =========================================
# STEP 1: Import libraries
# =========================================
import pandas as pd
import numpy as np

# =========================================
# STEP 2: Load datasets
# =========================================
sentiment_df = pd.read_csv(r"D:\fear_greed_index.csv")
trader_df = pd.read_csv(r"D:\historical_data.csv")

# =========================================
# STEP 3: Clean column names
# =========================================
sentiment_df.columns = sentiment_df.columns.str.strip().str.lower()
trader_df.columns = trader_df.columns.str.strip().str.lower()

# =========================================
# STEP 4: Fix sentiment data
# =========================================

# Convert date
sentiment_df['date'] = pd.to_datetime(sentiment_df['date'])

# Rename classification → sentiment
sentiment_df.rename(columns={'classification': 'sentiment'}, inplace=True)

# Keep only needed columns
sentiment_df = sentiment_df[['date', 'sentiment']]

# =========================================
# STEP 5: Fix trader data (IMPORTANT)
# =========================================

# Use Timestamp column (this is your actual time column)
trader_df['timestamp'] = pd.to_datetime(trader_df['timestamp'], unit='ms', errors='coerce')

# Extract date
trader_df['date'] = trader_df['timestamp'].dt.date
trader_df['date'] = pd.to_datetime(trader_df['date'])

# =========================================
# STEP 6: Rename important columns
# =========================================

trader_df.rename(columns={
    'coin': 'symbol',
    'size usd': 'size',
    'closed pnl': 'closedpnl',
    'side': 'side'
}, inplace=True)

# =========================================
# STEP 7: Select required columns
# =========================================
trader_df = trader_df[['date', 'symbol', 'side', 'size', 'closedpnl']]

# Fill missing values
trader_df['closedpnl'] = trader_df['closedpnl'].fillna(0)
trader_df['size'] = trader_df['size'].fillna(0)

# =========================================
# STEP 8: Merge datasets
# =========================================
merged_df = pd.merge(trader_df, sentiment_df, on='date', how='inner')

print("\nMerged Data:")
print(merged_df.head())

# =========================================
# STEP 9: Daily aggregation
# =========================================
daily_df = merged_df.groupby('date').agg({
    'closedpnl': 'sum',
    'size': 'sum'
}).reset_index()

# Add sentiment
daily_df = pd.merge(daily_df, sentiment_df, on='date', how='left')

# =========================================
# STEP 10: Sentiment mapping
# =========================================
sentiment_map = {
    'Extreme Fear': 0,
    'Fear': 1,
    'Neutral': 2,
    'Greed': 3,
    'Extreme Greed': 4
}

daily_df['sentiment_score'] = daily_df['sentiment'].map(sentiment_map)

# =========================================
# STEP 11: Correlation
# =========================================
correlation = daily_df['sentiment_score'].corr(daily_df['closedpnl'])

print("\nCorrelation:", correlation)

# =========================================
# STEP 12: Sentiment analysis
# =========================================
sentiment_summary = merged_df.groupby('sentiment').agg({
    'closedpnl': 'sum',
    'size': 'sum'
}).reset_index()

sentiment_summary['pnl_per_size'] = sentiment_summary['closedpnl'] / sentiment_summary['size']

print("\nSentiment Summary:")
print(sentiment_summary)

# =========================================
# STEP 13: Buy vs Sell
# =========================================
side_summary = merged_df.groupby(['sentiment', 'side']).agg({
    'closedpnl': 'sum',
    'size': 'sum'
}).reset_index()

print("\nSide Summary:")
print(side_summary)

# =========================================
# STEP 14: Win rate
# =========================================
merged_df['win'] = np.where(merged_df['closedpnl'] > 0, 1, 0)

win_rate = merged_df.groupby('sentiment')['win'].mean().reset_index()

print("\nWin Rate:")
print(win_rate)

# =========================================
# DONE
# =========================================
print("\n✅ Analysis Complete")


#Sentiment vs Total PnL (Most Important Chart)
import matplotlib.pyplot as plt

# Group by sentiment
sentiment_summary = merged_df.groupby('sentiment')['closedpnl'].sum()

plt.figure()
sentiment_summary.plot(kind='bar')

plt.title("Total PnL by Sentiment")
plt.xlabel("Market Sentiment")
plt.ylabel("Total Profit/Loss")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

#Buy vs Sell Performance

side_summary = merged_df.groupby(['sentiment', 'side'])['closedpnl'].sum().unstack()

plt.figure()
side_summary.plot(kind='bar')

plt.title("Buy vs Sell PnL by Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Total PnL")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Daily PnL Trend (Shows Volatility Impact)
daily_df = merged_df.groupby('date')['closedpnl'].sum().reset_index()

plt.figure()
plt.plot(daily_df['date'], daily_df['closedpnl'])

plt.title("Daily PnL Trend")
plt.xlabel("Date")
plt.ylabel("PnL")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Win Rate by Sentiment
merged_df['win'] = (merged_df['closedpnl'] > 0).astype(int)

win_rate = merged_df.groupby('sentiment')['win'].mean()

plt.figure()
win_rate.plot(kind='bar')

plt.title("Win Rate by Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Win Rate")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
