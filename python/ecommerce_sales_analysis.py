# ===============================================================
# Project: E-Commerce Sales Analysis
# Tools: Python (Pandas, Matplotlib)
# Description: Beginner-friendly data analytics workflow to clean,
#              explore, aggregate, and visualize e-commerce sales.
# ===============================================================

import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    # -----------------------------------------------------------
    # Step 1: Set File Paths & Load Dataset
    # -----------------------------------------------------------
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'ecommerce_sales_cleaned.csv')
    images_dir = os.path.join(base_dir, 'images')
    os.makedirs(images_dir, exist_ok=True)

    print('=' * 60)
    print('1. LOADING DATASET')
    print('=' * 60)
    df = pd.read_csv(data_path)
    print(f'Successfully loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.\n')

    # -----------------------------------------------------------
    # Step 2: Inspecting Dataset Structure & Missing Values
    # -----------------------------------------------------------
    print('=' * 60)
    print('2. DATASET OVERVIEW & SUMMARY INFO')
    print('=' * 60)
    print('First 5 rows:')
    print(df.head(), '\n')
    
    print('Data Types and Non-Null Counts:')
    print(df.info(), '\n')
    
    print('Missing values per column:')
    print(df.isnull().sum(), '\n')

    # -----------------------------------------------------------
    # Step 3: Data Type Conversion & Feature Engineering
    # -----------------------------------------------------------
    print('=' * 60)
    print('3. DATA PREPARATION')
    print('=' * 60)
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['YearMonth'] = df['Order Date'].dt.to_period('M').astype(str)
    print("Converted 'Order Date' to datetime and extracted 'YearMonth'.\n")

    # -----------------------------------------------------------
    # Step 4: Core Key Performance Indicators (KPIs)
    # -----------------------------------------------------------
    total_sales = df['Sales'].sum()
    total_profit = df['Profit'].sum()
    total_orders = df['Order ID'].nunique()
    total_qty = df['Quantity'].sum()
    avg_order_val = total_sales / total_orders
    profit_margin = (total_profit / total_sales) * 100

    print('=' * 60)
    print('4. OVERALL BUSINESS KPIS')
    print('=' * 60)
    print(f'Total Sales Revenue:     ${total_sales:,.2f}')
    print(f'Total Net Profit:        ${total_profit:,.2f}')
    print(f'Overall Profit Margin:   {profit_margin:.2f}%')
    print(f'Total Orders Placed:     {total_orders:,}')
    print(f'Total Items Sold:        {total_qty:,}')
    print(f'Average Order Value:     ${avg_order_val:,.2f}\n')

    # -----------------------------------------------------------
    # Step 5: Category Performance
    # -----------------------------------------------------------
    print('=' * 60)
    print('5. SALES & PROFIT BY CATEGORY')
    print('=' * 60)
    cat_summary = df.groupby('Category').agg(
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum'),
        Total_Quantity=('Quantity', 'sum')
    ).reset_index()
    cat_summary['Profit_Margin_%'] = (cat_summary['Total_Profit'] / cat_summary['Total_Sales']) * 100
    cat_summary = cat_summary.sort_values(by='Total_Sales', ascending=False)
    print(cat_summary.to_string(index=False), '\n')

    # -----------------------------------------------------------
    # Step 6: Regional Performance
    # -----------------------------------------------------------
    print('=' * 60)
    print('6. SALES & PROFIT BY REGION')
    print('=' * 60)
    reg_summary = df.groupby('Region').agg(
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum'),
        Order_Count=('Order ID', 'nunique')
    ).reset_index().sort_values(by='Total_Sales', ascending=False)
    reg_summary['Profit_Margin_%'] = (reg_summary['Total_Profit'] / reg_summary['Total_Sales']) * 100
    print(reg_summary.to_string(index=False), '\n')

    # -----------------------------------------------------------
    # Step 7: Top Products
    # -----------------------------------------------------------
    print('=' * 60)
    print('7. TOP 5 PRODUCTS BY SALES')
    print('=' * 60)
    top5_sales = df.groupby('Product Name')['Sales'].sum().reset_index().sort_values(by='Sales', ascending=False).head(5)
    print(top5_sales.to_string(index=False), '\n')

    print('TOP 5 PRODUCTS BY PROFIT:')
    top5_profit = df.groupby('Product Name')['Profit'].sum().reset_index().sort_values(by='Profit', ascending=False).head(5)
    print(top5_profit.to_string(index=False), '\n')

    # -----------------------------------------------------------
    # Step 8: Visualizations with Matplotlib
    # -----------------------------------------------------------
    print('=' * 60)
    print('8. GENERATING CHARTS & VISUALIZATIONS')
    print('=' * 60)

    # Chart 1: Monthly Sales Trend
    monthly = df.groupby('YearMonth')['Sales'].sum().reset_index()
    plt.figure(figsize=(10, 5))
    plt.plot(monthly['YearMonth'], monthly['Sales'], marker='o', color='#1f77b4', linewidth=2.5, markersize=6)
    plt.title('Monthly Sales Trend (2023)', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Month', fontsize=11)
    plt.ylabel('Total Sales ($)', fontsize=11)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    chart1_path = os.path.join(images_dir, 'monthly_sales_trend.png')
    plt.savefig(chart1_path, dpi=300)
    plt.close()
    print(f'Saved: {chart1_path}')

    # Chart 2: Sales by Category
    plt.figure(figsize=(8, 5))
    bars = plt.bar(cat_summary['Category'], cat_summary['Total_Sales'], color=['#2ca02c', '#ff7f0e', '#1f77b4'], width=0.55)
    plt.title('Total Sales by Category', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Category', fontsize=11)
    plt.ylabel('Total Sales ($)', fontsize=11)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 5000, f'${yval:,.0f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
    plt.tight_layout()
    chart2_path = os.path.join(images_dir, 'sales_by_category.png')
    plt.savefig(chart2_path, dpi=300)
    plt.close()
    print(f'Saved: {chart2_path}')

    # Chart 3: Profit by Category
    colors = ['#2ca02c' if x > 0 else '#d62728' for x in cat_summary['Total_Profit']]
    plt.figure(figsize=(8, 5))
    bars = plt.bar(cat_summary['Category'], cat_summary['Total_Profit'], color=colors, width=0.55)
    plt.title('Total Profit by Category', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Category', fontsize=11)
    plt.ylabel('Total Profit ($)', fontsize=11)
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    for bar in bars:
        yval = bar.get_height()
        offset = 1200 if yval >= 0 else -3000
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + offset, f'${yval:,.0f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
    plt.tight_layout()
    chart3_path = os.path.join(images_dir, 'profit_by_category.png')
    plt.savefig(chart3_path, dpi=300)
    plt.close()
    print(f'Saved: {chart3_path}')

    # Chart 4: Top 10 Products
    top10_prod = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=True).tail(10)
    plt.figure(figsize=(10, 6))
    plt.barh(top10_prod.index, top10_prod.values, color='#4B8BBE')
    plt.title('Top 10 Products by Sales Revenue', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Sales ($)', fontsize=11)
    plt.tight_layout()
    chart4_path = os.path.join(images_dir, 'top_10_products.png')
    plt.savefig(chart4_path, dpi=300)
    plt.close()
    print(f'Saved: {chart4_path}')

    # Chart 5: Sales by Region
    plt.figure(figsize=(8, 5))
    bars = plt.bar(reg_summary['Region'], reg_summary['Total_Sales'], color='#9467bd', width=0.55)
    plt.title('Total Sales by Region', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Region', fontsize=11)
    plt.ylabel('Total Sales ($)', fontsize=11)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 3000, f'${yval:,.0f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
    plt.tight_layout()
    chart5_path = os.path.join(images_dir, 'sales_by_region.png')
    plt.savefig(chart5_path, dpi=300)
    plt.close()
    print(f'Saved: {chart5_path}')

    print('\nAll analyses completed and visualizations exported successfully!')

if __name__ == '__main__':
    main()