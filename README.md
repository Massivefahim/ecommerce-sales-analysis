# E-Commerce Sales & Profit Performance Analysis Dashboard

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c.svg)](https://matplotlib.org/)
[![SQL](https://img.shields.io/badge/SQL-Analytics%20Queries-orange.svg)](https://en.wikipedia.org/wiki/SQL)
[![Power BI](https://img.shields.io/badge/Power%20BI-Executive%20Dashboard-F2C811.svg)](https://powerbi.microsoft.com/)

---

## 📌 Project Overview
An end-to-end data analytics project designed to evaluate sales revenue, profit margins, product category dynamics, regional performance, and customer purchasing patterns for a multi-category e-commerce business.

This project simulates a complete real-world business intelligence workflow:
1. **Excel:** Data profiling, quality assurance, duplicate handling, and initial pivot summaries.
2. **SQL:** Structured queries aggregating revenue, profit, average order value (AOV), and customer segmentation.
3. **Python (Pandas & Matplotlib):** Automated data validation, statistical distribution, and visual trend discovery.
4. **Power BI:** Interactive executive dashboard with dynamic slicers and DAX KPIs for business decision-makers.

---

## 📊 Executive Summary & Key Performance Indicators (KPIs)

| Metric | Value | Business Interpretation |
| :--- | :--- | :--- |
| **Total Revenue** | **$748,700.68** | Total gross merchandise sales generated in 2023 |
| **Total Net Profit** | **$29,373.48** | Overall business profit after discounts and product costs |
| **Overall Profit Margin** | **3.92%** | Slim operational margin driven down by furniture losses |
| **Total Orders** | **750** | Unique sales orders processed |
| **Total Items Sold** | **2,666** | Units moved across all categories |
| **Average Order Value (AOV)** | **$998.27** | Average revenue generated per customer transaction |

---

## 📁 Repository Structure

```
ecommerce-sales-analysis/
│
├── data/
│   ├── ecommerce_sales_raw.csv         # Raw transactional dataset with real-world flaws
│   └── ecommerce_sales_cleaned.csv     # Cleaned, standardized, analysis-ready dataset
│
├── sql/
│   └── ecommerce_sales_analysis.sql    # 11 commented SQL queries (Aggregations, GROUP BY, CASE WHEN)
│
├── python/
│   └── ecommerce_sales_analysis.py     # Python script for ETL, metrics calculation, and charts
│
├── powerbi/
│   └── powerbi_dashboard_guide.md      # Visual layouts, field mappings, and DAX measures
│
├── images/
│   ├── monthly_sales_trend.png         # Monthly revenue progression chart
│   ├── sales_by_category.png          # Category sales comparison
│   ├── profit_by_category.png         # Category profit margin comparison
│   ├── top_10_products.png            # High revenue product rankings
│   └── sales_by_region.png            # Geographic revenue distribution
│
└── README.md                           # Project documentation and business insights
```

---

## 🔍 Key Business Findings

### 1. Technology is the Primary Growth Engine
* **Finding:** Technology generated **$430,320.28 (57.5% of total sales)** and delivered **$46,560.23 in profit** with an average profit margin of **10.82%**.
* **Impact:** High consumer demand for items such as the *Dell XPS 15 Laptop ($144,353.70)* and *Apple iPhone 14 ($65,199.00)* creates healthy cash flow and strong margins.

### 2. Furniture Category Is Incurring Severe Losses
* **Finding:** While Furniture generated substantial sales (**$301,419.50, 40.3% of total**), it produced a net **loss of -$20,994.20** (-6.97% margin).
* **Impact:** Bulky items (such as the *Modern Leather Recliner* and *Executive Wooden Desk*) suffered from aggressive promotional discounts (up to 30%) combined with high fulfillment costs.

### 3. Office Supplies Offers High Margins with Low Ticket Size
* **Finding:** Office Supplies accounted for only **$16,960.90 (2.3% of sales)**, but achieved the company’s highest margin at **22.45% ($3,807.45 profit)**.
* **Impact:** Consumable items like copy paper and gel pens have reliable repeat purchase frequency with virtually zero discount erosion.

### 4. Central & South Regions Lead in Revenue
* **Finding:** Central ($239,530.16) and South ($226,217.96) together drove **62.2% of all revenue**. West region had the smallest volume ($94,207.54) but maintained the highest regional margin (**6.60%**).
* **Impact:** Central and South volume is healthy, but discounting policies need regional alignment to match Western profitability.

### 5. High-Value Customer Concentration
* **Finding:** The top 5 customers accounted for over **$223,898 (29.9% of company revenue)**, led by *Christopher Young ($50,164.97)* and *Andrew Scott ($50,108.64)*.
* **Impact:** The business benefits from strong B2B/bulk buyers; retaining these key accounts is critical to overall sales stability.

---

## 💡 Strategic Business Recommendations

1. **Cap Furniture Discounts:** Eliminate discounts exceeding 10% on bulky furniture and institute a freight shipping surcharge on items exceeding 50 lbs.
2. **Bundle Office Supplies with Technology:** Leverage high-volume tech purchases to cross-sell high-margin office supplies (e.g., bundle laptops with desk organizers and laptop stands).
3. **VIP Loyalty Program for Top 20% Accounts:** Introduce dedicated account managers and volume rebate tiers for corporate buyers spending over $25,000 annually.
4. **Expand West Region Marketing:** Allocate 15% more digital ad spend to the West region, which yields the best return per dollar sold (6.60% net margin).

---

## 🚀 How to Run this Project Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ecommerce-sales-analysis.git
cd ecommerce-sales-analysis
```

### 2. Run Python Analysis & Visualizations
Make sure Python 3.9+ is installed, then run:
```bash
pip install pandas matplotlib
python python/ecommerce_sales_analysis.py
```

### 3. Run SQL Queries
Open your preferred SQL client (MySQL Workbench, DBeaver, pgAdmin, or SQLite Studio), import `data/ecommerce_sales_cleaned.csv`, and execute `sql/ecommerce_sales_analysis.sql`.

### 4. Build the Power BI Dashboard
Follow the exact visual layout and DAX formulas outlined in [`powerbi/powerbi_dashboard_guide.md`](powerbi/powerbi_dashboard_guide.md).

---

## 👤 Author & Contact
- **Analyst:** [Your Name]
- **Role:** Aspiring Data Analyst
- **LinkedIn:** [Your LinkedIn Profile URL]
- **Portfolio:** [Your GitHub Profile URL]