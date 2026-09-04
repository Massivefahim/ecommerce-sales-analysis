-- ===============================================================
-- Project: E-Commerce Sales Analysis
-- Database: Standard SQL (Compatible with MySQL, PostgreSQL, SQLite, SQL Server)
-- Table: sales_orders
-- Description: Beginner-friendly SQL queries to extract key sales,
--              profit, customer, and regional business insights.
-- ===============================================================

-- ---------------------------------------------------------------
-- 0. Table Schema Definition (For Reference)
-- ---------------------------------------------------------------
-- CREATE TABLE sales_orders (
--     Order_ID VARCHAR(20) PRIMARY KEY,
--     Order_Date DATE,
--     Customer_ID VARCHAR(20),
--     Customer_Name VARCHAR(100),
--     Product_Name VARCHAR(150),
--     Category VARCHAR(50),
--     Sales DECIMAL(10, 2),
--     Quantity INT,
--     Profit DECIMAL(10, 2),
--     Region VARCHAR(50),
--     State VARCHAR(50)
-- );

-- ---------------------------------------------------------------
-- 1. Total Sales
-- What is the total revenue generated across all orders?
-- ---------------------------------------------------------------
SELECT 
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM sales_orders;

-- ---------------------------------------------------------------
-- 2. Total Profit
-- What is the total net profit earned across all orders?
-- ---------------------------------------------------------------
SELECT 
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales_orders;

-- ---------------------------------------------------------------
-- 3. Total Orders and Average Sales Per Order (AOV)
-- How many distinct orders were placed, and what is the average value?
-- ---------------------------------------------------------------
SELECT 
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Sales) / COUNT(DISTINCT Order_ID), 2) AS Avg_Order_Value
FROM sales_orders;

-- ---------------------------------------------------------------
-- 4. Sales and Profit by Category
-- Which category generates the highest sales and profit?
-- ---------------------------------------------------------------
SELECT 
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin_Pct
FROM sales_orders
GROUP BY Category
ORDER BY Total_Sales DESC;

-- ---------------------------------------------------------------
-- 5. Top 5 Products by Sales
-- Which products drive the highest revenue?
-- ---------------------------------------------------------------
SELECT 
    Product_Name,
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM sales_orders
GROUP BY Product_Name, Category
ORDER BY Total_Sales DESC
LIMIT 5;

-- ---------------------------------------------------------------
-- 6. Top 5 Products by Profit
-- Which products are the most profitable?
-- ---------------------------------------------------------------
SELECT 
    Product_Name,
    Category,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales_orders
GROUP BY Product_Name, Category
ORDER BY Total_Profit DESC
LIMIT 5;

-- ---------------------------------------------------------------
-- 7. Unprofitable Products (Loss Makers)
-- Which products are generating negative profit (losses)?
-- ---------------------------------------------------------------
SELECT 
    Product_Name,
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Loss
FROM sales_orders
GROUP BY Product_Name, Category
HAVING SUM(Profit) < 0
ORDER BY Total_Loss ASC;

-- ---------------------------------------------------------------
-- 8. Sales and Profit by Region
-- Which region generates the most revenue and profit?
-- ---------------------------------------------------------------
SELECT 
    Region,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(SUM(Sales), 2) AS Total_Revenue,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin_Pct
FROM sales_orders
GROUP BY Region
ORDER BY Total_Revenue DESC;

-- ---------------------------------------------------------------
-- 9. Monthly Sales Trend
-- How do sales and order volume trend month over month?
-- ---------------------------------------------------------------
SELECT 
    SUBSTR(Order_Date, 1, 7) AS Order_Month,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(SUM(Sales), 2) AS Monthly_Sales,
    ROUND(SUM(Profit), 2) AS Monthly_Profit
FROM sales_orders
GROUP BY SUBSTR(Order_Date, 1, 7)
ORDER BY Order_Month ASC;

-- ---------------------------------------------------------------
-- 10. Top 5 Customers by Sales
-- Who are our highest-spending customers?
-- ---------------------------------------------------------------
SELECT 
    Customer_ID,
    Customer_Name,
    COUNT(DISTINCT Order_ID) AS Orders_Count,
    ROUND(SUM(Sales), 2) AS Total_Spent
FROM sales_orders
GROUP BY Customer_ID, Customer_Name
ORDER BY Total_Spent DESC
LIMIT 5;

-- ---------------------------------------------------------------
-- 11. Customer Segmentation by Spending (Using CASE WHEN)
-- Segmenting customers into High, Medium, and Low value tiers
-- ---------------------------------------------------------------
SELECT 
    Customer_Name,
    ROUND(SUM(Sales), 2) AS Total_Spent,
    CASE 
        WHEN SUM(Sales) >= 40000 THEN 'High Value Tier'
        WHEN SUM(Sales) >= 20000 THEN 'Medium Value Tier'
        ELSE 'Standard Tier'
    END AS Customer_Segment
FROM sales_orders
GROUP BY Customer_Name
ORDER BY Total_Spent DESC;
