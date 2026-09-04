# Power BI Dashboard Implementation Guide

## Project: E-Commerce Sales Executive Performance Dashboard
**Canvas Dimensions:** Standard 16:9 (1280 x 720 px)  
**Theme / Color Palette:**
- Primary Navy: `#1E293B` (Headers, KPI text)
- Accent Blue: `#2563EB` (Sales bars & line trend)
- Positive Green: `#16A34A` (Profitable indicators)
- Alert Red: `#DC2626` (Loss indicators)
- Background: `#F8FAFC` (Clean light off-white)
- Card Containers: `#FFFFFF` (White cards with subtle drop shadows)

---

## 1. DAX Measures (Copy & Paste Ready)

Create a dedicated table named `_Measures` in Power BI (`Enter Data` -> Name it `_Measures`), then create the following measures:

### Measure 1: Total Sales
```dax
Total Sales = SUM(sales_orders[Sales])
```
*Format: Currency (`$`), 2 decimal places.*

### Measure 2: Total Profit
```dax
Total Profit = SUM(sales_orders[Profit])
```
*Format: Currency (`$`), 2 decimal places.*

### Measure 3: Total Orders
```dax
Total Orders = DISTINCTCOUNT(sales_orders[Order ID])
```
*Format: Whole number with thousand separator (`#,##0`).*

### Measure 4: Average Order Value (AOV)
```dax
Average Order Value = DIVIDE([Total Sales], [Total Orders], 0)
```
*Format: Currency (`$`), 2 decimal places.*

### Measure 5: Profit Margin %
```dax
Profit Margin % = DIVIDE([Total Profit], [Total Sales], 0)
```
*Format: Percentage (`0.0%`).*

---

## 2. Dashboard Layout Structure (One Page)

```
+-----------------------------------------------------------------------------------------+
| [Header] E-Commerce Sales & Profit Executive Dashboard    |  [Slicers: Date, Cat, Reg] |
+-----------------------------------------------------------------------------------------+
| [KPI 1: Total Sales] | [KPI 2: Total Profit] | [KPI 3: Total Orders] | [KPI 4: Avg Order]|
|     $748,701         |       $29,373         |         750           |      $998.27     |
+-----------------------------------------------------------------------------------------+
|  [Monthly Sales Trend - Line Chart]           |  [Sales & Profit by Category - Bar]     |
|  X: Month, Y: Total Sales                     |  Y: Category, X: Total Sales            |
+-----------------------------------------------------------------------------------------+
|  [Top 5 Products by Sales - Horizontal Bar]   |  [Sales & Profit by Region - Clustered] |
|  Y: Product Name, X: Total Sales              |  X: Region, Y: Sales & Profit           |
+-----------------------------------------------------------------------------------------+
```

---

## 3. Visuals Configuration & Field Mappings

### A. Top Slicer Bar (Top Right)
1. **Date Slicer:**
   - Field: `sales_orders[Order Date]`
   - Visual Type: Slicer -> Style: `Between` (Slider)
2. **Category Slicer:**
   - Field: `sales_orders[Category]`
   - Visual Type: Slicer -> Style: `Tile` or `Dropdown`
3. **Region Slicer:**
   - Field: `sales_orders[Region]`
   - Visual Type: Slicer -> Style: `Dropdown`

### B. KPI Cards (Row 1)
Place 4 **Card (New)** or classic **Card** visuals side-by-side:
- **Card 1:** Measure `[Total Sales]` | Title: "Total Revenue"
- **Card 2:** Measure `[Total Profit]` | Title: "Net Profit" (Add conditional formatting: Green if >= 0, Red if < 0)
- **Card 3:** Measure `[Total Orders]` | Title: "Total Orders"
- **Card 4:** Measure `[Average Order Value]` | Title: "Avg Order Value (AOV)"

### C. Visual 1: Monthly Sales Trend (Middle Left)
- **Visual Type:** Line Chart
- **X-Axis:** `sales_orders[Order Date]` (Hierarchy -> Month) or `[YearMonth]`
- **Y-Axis:** `[Total Sales]`
- **Tooltip:** `[Total Profit]`, `[Total Orders]`
- **Formatting:** Turn Data Labels ON, Stroke width: 3, Data color: `#2563EB`.

### D. Visual 2: Sales by Category (Middle Right)
- **Visual Type:** Clustered Column Chart (or Bar Chart)
- **X-Axis:** `sales_orders[Category]`
- **Y-Axis:** `[Total Sales]`
- **Tooltips:** `[Total Profit]`, `[Profit Margin %]`
- **Formatting:** Data Labels ON, display units: Thousands (`$K`).

### E. Visual 3: Top 5 Products by Sales (Bottom Left)
- **Visual Type:** Clustered Bar Chart (Horizontal)
- **Y-Axis:** `sales_orders[Product Name]`
- **X-Axis:** `[Total Sales]`
- **Filter (Filters Pane):** Filter on `Product Name` -> Filter Type: `Top N` -> Show top: `5` by value `[Total Sales]`.
- **Formatting:** Data Labels ON, Data color: `#1E293B`.

### F. Visual 4: Regional Performance (Bottom Right)
- **Visual Type:** Clustered Column Chart
- **X-Axis:** `sales_orders[Region]`
- **Y-Axis:** `[Total Sales]` and `[Total Profit]`
- **Formatting:** Sales bar in Blue (`#2563EB`), Profit bar in Green (`#16A34A`).

---

## 4. Pro Formatting Tips for Beginners
1. **Disable Gridlines:** Turn off heavy vertical and horizontal gridlines for a clean modern SaaS look.
2. **Standardize Font:** Use `Segoe UI` or `Segoe UI Semibold` across all labels and titles.
3. **Card Border & Rounded Corners:** Under `Format visual` -> `General` -> `Effects` -> set Background to White and Border with 8px rounded corners.