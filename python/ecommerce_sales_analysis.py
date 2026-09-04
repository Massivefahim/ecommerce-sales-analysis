# ===============================================================
# Project: India E-Commerce Sales Analysis
# Tools: Python (Pandas, Matplotlib)
# Currency: Indian Rupees (INR / ₹)
# Description: Beginner-friendly data analytics script to inspect,
#              clean, aggregate, and visualize Indian e-commerce sales.
# ===============================================================

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

# Ensure UTF-8 support for console output in Windows
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def main():
    # -----------------------------------------------------------
    # Step 1: Set Paths & Load Dataset
    # -----------------------------------------------------------
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'ecommerce_sales_cleaned.csv')
    images_dir = os.path.join(base_dir, 'images')
    os.makedirs(images_dir, exist_ok=True)

    print('=' * 65)
    print('1. LOADING INDIA E-COMMERCE DATASET')
    print('=' * 65)
    df = pd.read_csv(data_path)
    print(f'Successfully loaded dataset: {df.shape[0]} rows, {df.shape[1]} columns.\n')

    # -----------------------------------------------------------
    # Step 2: Overview & Summary Info
    # -----------------------------------------------------------
    print('=' * 65)
    print('2. DATASET OVERVIEW & STRUCTURE')
    print('=' * 65)
    print('First 5 records:')
    print(df[['Order ID', 'Customer Name', 'City', 'State', 'Category', 'Sales', 'Profit', 'Payment Method', 'Order Status']].head(), '\n')

    print('Missing values count per column:')
    print(df.isnull().sum(), '\n')

    # -----------------------------------------------------------
    # Step 3: Date Preprocessing
    # -----------------------------------------------------------
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['YearMonth'] = df['Order Date'].dt.to_period('M').astype(str)

    # -----------------------------------------------------------
    # Step 4: Core Business KPIs (in INR ₹)
    # -----------------------------------------------------------
    total_sales = df['Sales'].sum()
    total_profit = df['Profit'].sum()
    total_orders = df['Order ID'].nunique()
    total_customers = df['Customer ID'].nunique()
    avg_order_val = total_sales / total_orders
    profit_margin = (total_profit / total_sales) * 100

    print('=' * 65)
    print('3. EXECUTIVE BUSINESS KPIS (INDIA)')
    print('=' * 65)
    print(f'Total Sales Revenue:     Rs. {total_sales:,.2f}')
    print(f'Total Net Profit:        Rs. {total_profit:,.2f}')
    print(f'Overall Profit Margin:   {profit_margin:.2f}%')
    print(f'Total Orders Placed:     {total_orders:,}')
    print(f'Total Unique Customers:  {total_customers:,}')
    print(f'Average Order Value:     Rs. {avg_order_val:,.2f}\n')

    # -----------------------------------------------------------
    # Step 5: Category Performance
    # -----------------------------------------------------------
    print('=' * 65)
    print('4. SALES & PROFIT BY CATEGORY')
    print('=' * 65)
    cat_summary = df.groupby('Category').agg(
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum'),
        Order_Count=('Order ID', 'count')
    ).reset_index()
    cat_summary['Profit_Margin_%'] = (cat_summary['Total_Profit'] / cat_summary['Total_Sales']) * 100
    cat_summary = cat_summary.sort_values(by='Total_Sales', ascending=False)
    print(cat_summary.to_string(index=False), '\n')

    # -----------------------------------------------------------
    # Step 6: Payment Method Breakdown
    # -----------------------------------------------------------
    print('=' * 65)
    print('5. PAYMENT METHOD SHARE')
    print('=' * 65)
    pm_summary = df.groupby('Payment Method').agg(
        Total_Sales=('Sales', 'sum'),
        Order_Count=('Order ID', 'count')
    ).reset_index().sort_values(by='Total_Sales', ascending=False)
    pm_summary['Sales_Share_%'] = (pm_summary['Total_Sales'] / total_sales) * 100
    print(pm_summary.to_string(index=False), '\n')

    # -----------------------------------------------------------
    # Step 7: Visualizations with Matplotlib
    # -----------------------------------------------------------
    print('=' * 65)
    print('6. GENERATING CHARTS (INDIA E-COMMERCE)')
    print('=' * 65)

    # Chart 1: Monthly Sales Trend
    monthly = df.groupby('YearMonth')['Sales'].sum().reset_index()
    plt.figure(figsize=(10, 5))
    plt.plot(monthly['YearMonth'], monthly['Sales'] / 100000, marker='o', color='#2563EB', linewidth=2.5, markersize=6)
    plt.title('Monthly Sales Trend (2023)', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Month', fontsize=11)
    plt.ylabel('Sales (INR in Lakhs)', fontsize=11)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(images_dir, 'monthly_sales_trend.png'), dpi=300)
    plt.close()

    # Chart 2: Sales by Category
    plt.figure(figsize=(9, 5))
    bars = plt.bar(cat_summary['Category'], cat_summary['Total_Sales'] / 100000, color='#0D9488', width=0.55)
    plt.title('Sales by Category', fontsize=14, fontweight='bold', pad=15)
    plt.ylabel('Sales (INR in Lakhs)', fontsize=11)
    plt.xticks(rotation=15)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 1.2, f'{yval:.1f}L', ha='center', va='bottom', fontsize=9, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(images_dir, 'sales_by_category.png'), dpi=300)
    plt.close()

    # Chart 3: Sales by State (Top 7)
    top_states = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(7)
    plt.figure(figsize=(9, 5))
    bars = plt.bar(top_states.index, top_states.values / 100000, color='#6366F1', width=0.55)
    plt.title('Top 7 Indian States by Sales Revenue', fontsize=14, fontweight='bold', pad=15)
    plt.ylabel('Sales (INR in Lakhs)', fontsize=11)
    plt.xticks(rotation=20)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.6, f'{yval:.1f}L', ha='center', va='bottom', fontsize=9, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(images_dir, 'sales_by_state.png'), dpi=300)
    plt.close()

    # Chart 4: Profit by Region
    reg_profit = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
    plt.figure(figsize=(8, 5))
    bars = plt.bar(reg_profit.index, reg_profit.values / 1000, color=['#10B981', '#3B82F6', '#F59E0B', '#8B5CF6'], width=0.5)
    plt.title('Net Profit by Region', fontsize=14, fontweight='bold', pad=15)
    plt.ylabel('Profit (INR in Thousands)', fontsize=11)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 4, f'{yval:.0f}K', ha='center', va='bottom', fontsize=9, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(images_dir, 'profit_by_region.png'), dpi=300)
    plt.close()

    # Chart 5: Top 5 Products by Sales
    top5_prod = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=True).tail(5)
    plt.figure(figsize=(10, 5.5))
    plt.barh(top5_prod.index, top5_prod.values / 100000, color='#F97316')
    plt.title('Top 5 Products by Revenue (India)', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Sales (INR in Lakhs)', fontsize=11)
    plt.tight_layout()
    plt.savefig(os.path.join(images_dir, 'top_5_products.png'), dpi=300)
    plt.close()

    # Chart 6: Order Status Distribution
    status_counts = df['Order Status'].value_counts()
    plt.figure(figsize=(8, 5))
    plt.pie(status_counts.values, labels=status_counts.index, autopct='%1.1f%%', colors=['#10B981', '#3B82F6', '#FBBF24', '#EF4444', '#6B7280'], startangle=140)
    plt.title('Order Fulfillment Status Distribution', fontsize=14, fontweight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(os.path.join(images_dir, 'order_status_distribution.png'), dpi=300)
    plt.close()

    print('All charts successfully updated and saved to images/!')

if __name__ == '__main__':
    main()