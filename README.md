# India E-Commerce Sales & Profit Performance Analysis Dashboard

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c.svg)](https://matplotlib.org/)
[![SQL](https://img.shields.io/badge/SQL-Analytics%20Queries-orange.svg)](https://en.wikipedia.org/wiki/SQL)
[![Power BI](https://img.shields.io/badge/Power%20BI-Executive%20Dashboard-F2C811.svg)](https://powerbi.microsoft.com/)
[![Currency](https://img.shields.io/badge/Currency-INR%20(%E2%82%B9)-green.svg)](https://en.wikipedia.org/wiki/Indian_rupee)

---

## 📌 Project Overview
An end-to-end data analytics project focused on the **Indian e-commerce retail market**, analyzing **850+ transactional orders** across Tier-1 and Tier-2 Indian cities (Mumbai, Delhi, Bengaluru, Hyderabad, Kolkata, Pune, Ahmedabad, Lucknow, Patna, Jaipur, etc.).

The project simulates a complete business intelligence lifecycle:
1. **Excel:** Data cleaning, duplicate removal, format standardization, and pivot validation.
2. **SQL:** 13 structured queries evaluating revenue in Indian Rupees (₹), profit margins, regional penetration, payment method adoption (UPI, COD, Cards), and order fulfillment.
3. **Python (Pandas & Matplotlib):** Automated ETL, exploratory data analysis, and publication-ready charts exported in INR denominations.
4. **Power BI:** Interactive executive dashboard with dynamic slicers (Date, State, Region, Category, Payment Method) and custom DAX measures.

---

## 📊 Executive Summary & Key Performance Indicators (KPIs)

| Metric | Value (INR) | Business Interpretation |
| :--- | :--- | :--- |
| **Total Revenue** | **₹2,08,50,066.35** (~₹2.09 Crore) | Gross merchandise value generated across all product lines in 2023 |
| **Total Net Profit** | **₹6,75,411.54** (~₹6.75 Lakh) | Overall business net earnings after discounts, refunds, and logistics |
| **Overall Profit Margin** | **3.24%** | Net profit margin impacted by heavy logistics costs and clearance discounts |
| **Total Orders** | **850** | Valid commercial transactions processed |
| **Total Customers** | **25** | High-frequency retail & corporate buyer accounts |
| **Average Order Value (AOV)** | **₹24,529.49** | Average ticket size driven by high-value smartphone & laptop orders |

---

## 📁 Repository Structure

```
ecommerce-sales-analysis/
│
├── data/
│   ├── ecommerce_sales_raw.csv         # Raw Indian dataset with duplicate & blank rows for cleaning
│   └── ecommerce_sales_cleaned.csv     # Cleaned, analysis-ready dataset (850 records, 14 columns)
│
├── sql/
│   └── ecommerce_sales_analysis.sql    # 13 commented SQL queries (Aggregations, HAVING, CASE WHEN)
│
├── python/
│   └── ecommerce_sales_analysis.py     # Python script for ETL, metrics calculation, and chart exports
│
├── powerbi/
│   └── powerbi_dashboard_guide.md      # Field mapping, visual specs, and DAX measures
│
├── images/
│   ├── monthly_sales_trend.png         # Monthly revenue progression chart (Lakhs INR)
│   ├── sales_by_category.png          # Category revenue distribution
│   ├── sales_by_state.png             # Top Indian states by revenue
│   ├── profit_by_region.png           # Regional net profit comparison (North, South, East, West)
│   ├── top_5_products.png             # Top revenue drivers (Samsung S23, OnePlus 11R, HP Laptop)
│   └── order_status_distribution.png  # Fulfillment pie chart (Delivered, Returned, Cancelled)
│
└── README.md                           # Comprehensive documentation & business recommendations
```

---

## 🔍 Key Business Findings (Calculated Directly from Dataset)

### 1. Mobiles & Electronics Dominate Top-Line Revenue (86.3%)
* **Finding:** **Mobiles & Accessories (₹95,06,179.75)** and **Electronics (₹84,83,634.10)** together accounted for **₹1.80 Crore (86.3% of total revenue)**.
* **Impact:** High ticket items (Samsung Galaxy S23 5G at ₹47.6L and OnePlus 11R at ₹31.1L) generate healthy cash flow and the bulk of net profit (₹3.72L and ₹2.41L).

### 2. Home & Kitchen Incurs Net Losses Driven by Heavy Freight & Returns
* **Finding:** Home & Kitchen generated **₹18,48,285.90** in sales but produced a net **loss of -₹67,894.62** (-3.67% margin).
* **Impact:** High-weight products like the *Wakefit Orthopedic Mattress (-₹1,58,120.48 loss)* suffered from return logistics overhead and price discounts that eroded margins.

### 3. Beauty & Fashion Deliver the Highest Profit Margins
* **Finding:** **Beauty & Personal Care** achieved the company’s highest margin at **23.08%** (₹49,377.76 profit on ₹2.14L sales), followed by **Fashion** at **10.14%** (₹80,897.63 profit on ₹7.98L sales).
* **Impact:** While unit prices are lower, high gross margins make these categories ideal for cross-selling and margin expansion.

### 4. UPI is the Undisputed Payment Leader (38.5% Share)
* **Finding:** **UPI** led all payment modes with **₹80,28,686.75 across 360 orders (38.5% of sales)**, followed by Credit Cards (₹50.5L / 24.2%) and Cash on Delivery (₹42.9L / 20.6%).
* **Impact:** UPI provides the lowest payment gateway failure rate and eliminates COD handling friction.

### 5. Maharashtra and West Region Lead Sales & Profitability
* **Finding:** **Maharashtra** was the #1 state with **₹42,18,818.90 across 114 orders**, followed by Delhi (₹25.1L), Bihar (₹22.8L), and West Bengal (₹21.5L). The **West Region** delivered the highest regional profit of **₹3,20,958.13 (4.60% margin)**.
* **Impact:** Western tier-1 hubs (Mumbai, Pune, Ahmedabad) show the highest purchasing power and repeat order frequency.

### 6. Healthy Order Fulfillment with Manageable Return Rates
* **Finding:** **72.9% of orders (620 orders)** were successfully **Delivered**, 9.4% Shipped, and 7.1% Processing. Returns stood at **6.8% (58 orders)** and cancellations at **3.8% (32 orders)**.
* **Impact:** Return rates are aligned with Indian e-commerce benchmarks, though returns in bulky home goods need tighter pre-dispatch checks.

---

## 💡 Strategic Business Recommendations

1. **Implement Reverse Logistics Surcharge on Bulky Home Goods:** For heavy items like mattresses and furniture, require an upfront non-refundable freight deposit of ₹500–₹1,000 on COD orders to curb frivolous returns.
2. **Promote UPI Adoption with 2% Instant Cashback:** Convert remaining Cash on Delivery orders (20.6% share) to UPI at checkout to reduce RTO (Return to Origin) risks and courier cash-handling fees.
3. **Bundle High-Margin Beauty & Fashion with Tech Purchases:** Create automated "Add to Cart" recommendations offering skin care or casual apparel at special combo pricing during electronics checkouts.
4. **Target Tier-2 Hubs in West & Central Regions:** Scale regional inventory nodes in Pune, Ahmedabad, and Indore to reduce transit times and shipping overhead.

---

## 🚀 How to Run this Project Locally

### 1. Clone the Repository
```bash
git clone https://github.com/Massivefahim/ecommerce-sales-analysis.git
cd ecommerce-sales-analysis
```

### 2. Run Python Script (Generates All Visualizations)
```bash
pip install pandas matplotlib
python python/ecommerce_sales_analysis.py
```

### 3. Run SQL Queries
Load `data/ecommerce_sales_cleaned.csv` into MySQL, PostgreSQL, SQLite, or DBeaver and run `sql/ecommerce_sales_analysis.sql`.

### 4. Build Power BI Dashboard
Open Power BI Desktop, import `data/ecommerce_sales_cleaned.csv`, and follow the field mapping and DAX measures outlined in [`powerbi/powerbi_dashboard_guide.md`](powerbi/powerbi_dashboard_guide.md).

---

## 👤 Author & Contact
- **Analyst:** [Your Name]
- **Role:** Aspiring Data Analyst
- **LinkedIn:** [Your LinkedIn Profile URL]
- **GitHub:** [https://github.com/Massivefahim](https://github.com/Massivefahim)