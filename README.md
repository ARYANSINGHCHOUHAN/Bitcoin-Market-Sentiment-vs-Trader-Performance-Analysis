# 📊 Bitcoin Market Sentiment vs Trader Performance Analysis

## 🚀 Overview

This project explores the relationship between **Bitcoin market sentiment (Fear & Greed Index)** and **trader performance** using real trading data.

The goal is to uncover whether market sentiment can be used as a signal for improving trading strategies. Due to Data Contraints for Historical Data I've only uploaded Fear Index and Historical Data's CSV link is Added

---

## 📂 Datasets Used

### 1. Bitcoin Market Sentiment Dataset

* Columns:

  * `Date`
  * `Classification` (Fear, Greed, etc.)

### 2. Hyperliquid Trader Dataset

* Columns include:

  * `Timestamp`
  * `Coin`
  * `Side`
  * `Size USD`
  * `Closed PnL`
  * (and more)

---

## 🧠 Problem Statement

Most traders assume:

> “Market sentiment directly predicts profitability.”

This project tests that assumption using real trading data.

---

## ⚙️ Methodology

1. **Data Cleaning**

   * Standardized column names
   * Handled missing values
   * Converted timestamps (Unix → datetime)

2. **Data Alignment**

   * Extracted date from trading data
   * Merged datasets on daily level

3. **Feature Engineering**

   * Created `sentiment_score` (numeric encoding)
   * Created `win` variable (profit vs loss)

4. **Aggregation**

   * Daily PnL and trading volume
   * Sentiment-wise performance
   * Buy vs Sell breakdown

5. **Analysis**

   * Correlation between sentiment and PnL
   * Efficiency (PnL per volume)
   * Win rate across sentiment categories

6. **Visualization**

   * PnL vs Sentiment
   * Buy vs Sell performance
   * Daily PnL trends
   * Win rate comparison

---

## 📊 Key Insights

* Sentiment has **weak correlation** with profitability
* **Extreme Fear** → highest absolute profits (high volatility)
* **Extreme Greed** → better capital efficiency
* **Sell trades outperform Buy trades**
* Volatility matters more than sentiment

---

## 📈 Charts Included

* Total PnL by Sentiment
* Buy vs Sell Performance
* Daily PnL Trend
* Win Rate by Sentiment

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib

---

## 💡 Conclusion

Market sentiment alone is **not a reliable predictor** of trading success.

> The real edge lies in volatility and execution strategy.

---

## 🔥 Future Improvements

* Add volatility indicators (ATR, VIX-style metrics)
* Analyze leverage impact
* Identify top-performing traders
* Build predictive models

---

## 👤 Author

Aryan Singh Chouhan

