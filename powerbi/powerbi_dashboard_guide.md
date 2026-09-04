# Power BI Dashboard Implementation Guide: India E-Commerce Sales Analysis

## 📌 Project Overview
**Dashboard Title:** India E-Commerce Sales Analysis  
**Canvas Dimensions:** Standard 16:9 (1280 x 720 px)  
**Currency:** Indian Rupee (INR / ₹)  
**Theme & Color Palette:**
- Primary Header/Nav: `#0F172A` (Slate Navy)
- Primary Sales Accent: `#2563EB` (Royal Blue)
- Indian Teal Accent: `#0D9488` (Category bars)
- Positive Profit: `#10B981` (Emerald Green)
- Negative Alert: `#EF4444` (Loss / Returns)
- Card Containers: `#FFFFFF` with 8px rounded corners and subtle drop shadows

---

## 1. DAX Measures (Copy & Paste Ready)

In Power BI, click **"New Measure"** on the Home tab and paste these measures:

### Measure 1: Total Sales (₹)
```dax
Total Sales = SUM(ecommerce_sales_cleaned[Sales])
```
*Format: Currency (`₹ English (India)` or custom format `₹#,##,##0.00`).*

### Measure 2: Total Profit (₹)
```dax
Total Profit = SUM(ecommerce_sales_cleaned[Profit])
```
*Format: Currency (`₹ English (India)` or custom format `₹#,##,##0.00`).*

### Measure 3: Total Orders
```dax
Total Orders = DISTINCTCOUNT(ecommerce_sales_cleaned[Order ID])
```
*Format: Whole number with comma separator (`#,##0`).*

### Measure 4: Total Customers
```dax
Total Customers = DISTINCTCOUNT(ecommerce_sales_cleaned[Customer ID])
```
*Format: Whole number (`#,##0`).*

### Measure 5: Average Order Value (AOV ₹)
```dax
Average Order Value = DIVIDE([Total Sales], [Total Orders], 0)
```
*Format: Currency (`₹#,##,##0.00`).*

### Measure 6: Profit Margin %
```dax
Profit Margin % = DIVIDE([Total Profit], [Total Sales], 0)
```
*Format: Percentage (`0.0%`).*

---

## 2. Dashboard Layout Structure (One Page)

```
+-----------------------------------------------------------------------------------------------+
|  🇮🇳 India E-Commerce Sales Analysis          [Slicers: Date | State | Region | Cat | PayMethod] |
+-----------------------------------------------------------------------------------------------+
| [Total Sales]    | [Total Profit]   | [Total Orders] | [Total Customers] | [Avg Order Value]  |
|  ₹2.09 Cr        |  ₹6.75 Lakh      |   850 Orders   |   25 VIP Accounts |  ₹24,529           |
+-----------------------------------------------------------------------------------------------+
|  [Monthly Sales Trend - Line Chart]           |  [Sales by Category - Column Chart]           |
|  X: Month, Y: Total Sales                     |  X: Category, Y: Total Sales                  |
+-----------------------------------------------------------------------------------------------+
|  [Sales by State - Bar Chart]                 |  [Profit by Region - Bar] | [Order Status]    |
|  Y: State, X: Total Sales                     |  X: Region, Y: Profit     | Donut: Delivered% |
+-----------------------------------------------------------------------------------------------+
```

---

## 3. Visuals Configuration & Field Mappings

### A. Top Slicer Bar
1. **Date Slicer:** Field: `Order Date` -> Style: `Between` (Slider)
2. **State Slicer:** Field: `State` -> Style: `Dropdown`
3. **Region Slicer:** Field: `Region` -> Style: `Dropdown`
4. **Category Slicer:** Field: `Category` -> Style: `Dropdown` or `Tile`
5. **Payment Method Slicer:** Field: `Payment Method` -> Style: `Dropdown` (UPI, COD, Cards)

### B. Top KPI Cards Row
Add 5 **Card** visuals side by side:
- **Card 1:** Field: `[Total Sales]` (Title: Total Revenue)
- **Card 2:** Field: `[Total Profit]` (Title: Net Profit)
- **Card 3:** Field: `[Total Orders]` (Title: Total Orders)
- **Card 4:** Field: `[Total Customers]` (Title: Active Customers)
- **Card 5:** Field: `[Average Order Value]` (Title: AOV)

### C. Visual 1: Monthly Sales Trend (Middle Left)
- **Visual Type:** Line Chart
- **X-Axis:** `Order Date` (Hierarchy: Month) or `YearMonth`
- **Y-Axis:** `[Total Sales]`
- **Tooltips:** `[Total Profit]`, `[Total Orders]`
- **Formatting:** Turn Data Labels ON, Line color `#2563EB`.

### D. Visual 2: Sales by Category (Middle Right)
- **Visual Type:** Clustered Column Chart
- **X-Axis:** `Category`
- **Y-Axis:** `[Total Sales]`
- **Tooltips:** `[Total Profit]`, `[Profit Margin %]`
- **Formatting:** Data Labels ON, display units: Lakhs / Millions.

### E. Visual 3: Sales by State (Bottom Left)
- **Visual Type:** Clustered Bar Chart (Horizontal)
- **Y-Axis:** `State`
- **X-Axis:** `[Total Sales]`
- **Formatting:** Data color `#6366F1`, Data labels ON.

### F. Visual 4: Profit by Region (Bottom Center)
- **Visual Type:** Clustered Column Chart
- **X-Axis:** `Region`
- **Y-Axis:** `[Total Profit]`
- **Formatting:** Data color `#10B981`.

### G. Visual 5: Order Status (Bottom Right)
- **Visual Type:** Donut Chart
- **Legend:** `Order Status`
- **Values:** `[Total Orders]`
- **Formatting:** Legend position: Right, Detail labels: Category + Percent of total.