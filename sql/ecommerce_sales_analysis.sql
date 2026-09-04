-- ===============================================================
-- Project: India E-Commerce Sales Analysis
-- Database: Standard SQL (Compatible with MySQL, PostgreSQL, SQLite, SQL Server)
-- Table: sales_orders
-- Currency: Indian Rupees (INR / ₹)
-- Description: Beginner-friendly SQL queries to extract key sales,
--              profit, category, state, and payment insights in India.
-- ===============================================================

-- ---------------------------------------------------------------
-- 0. Table Schema Definition (For Reference)
-- ---------------------------------------------------------------
-- CREATE TABLE sales_orders (
--     Order_ID VARCHAR(20) PRIMARY KEY,
--     Order_Date DATE,
--     Customer_ID VARCHAR(20),
--     Customer_Name VARCHAR(100),
--     City VARCHAR(50),
--     State VARCHAR(50),
--     Region VARCHAR(50),
--     Product_Name VARCHAR(150),
--     Category VARCHAR(50),
--     Sales DECIMAL(12, 2),
--     Quantity INT,
--     Profit DECIMAL(12, 2),
--     Payment_Method VARCHAR(50),
--     Order_Status VARCHAR(50)
-- );

-- ---------------------------------------------------------------
-- 1. Total Sales (Revenue in INR)
-- What is the total gross revenue generated across all orders?
-- ---------------------------------------------------------------
SELECT 
    ROUND(SUM(Sales), 2) AS Total_Sales_INR
FROM sales_orders;

-- ---------------------------------------------------------------
-- 2. Total Profit (INR)
-- What is the total net profit earned across all orders?
-- ---------------------------------------------------------------
SELECT 
    ROUND(SUM(Profit), 2) AS Total_Profit_INR
FROM sales_orders;

-- ---------------------------------------------------------------
-- 3. Total Orders, Total Customers & Average Order Value (AOV)
-- How many orders and customers, and what is the average basket size?
-- ---------------------------------------------------------------
SELECT 
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    COUNT(DISTINCT Customer_ID) AS Total_Customers,
    ROUND(SUM(Sales), 2) AS Total_Sales_INR,
    ROUND(SUM(Sales) / COUNT(DISTINCT Order_ID), 2) AS Avg_Order_Value_INR
FROM sales_orders;

-- ---------------------------------------------------------------
-- 4. Sales & Profit Performance by Category
-- Which category generates the highest sales and highest profit margin?
-- ---------------------------------------------------------------
SELECT 
    Category,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(SUM(Sales), 2) AS Total_Sales_INR,
    ROUND(SUM(Profit), 2) AS Total_Profit_INR,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin_Pct
FROM sales_orders
GROUP BY Category
ORDER BY Total_Sales_INR DESC;

-- ---------------------------------------------------------------
-- 5. Top 5 Products by Sales Revenue
-- Which specific items generate the highest top-line revenue?
-- ---------------------------------------------------------------
SELECT 
    Product_Name,
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales_INR
FROM sales_orders
GROUP BY Product_Name, Category
ORDER BY Total_Sales_INR DESC
LIMIT 5;

-- ---------------------------------------------------------------
-- 6. Top 5 Products by Net Profit
-- Which products contribute the most to the company's bottom line?
-- ---------------------------------------------------------------
SELECT 
    Product_Name,
    Category,
    ROUND(SUM(Profit), 2) AS Total_Profit_INR
FROM sales_orders
GROUP BY Product_Name, Category
ORDER BY Total_Profit_INR DESC
LIMIT 5;

-- ---------------------------------------------------------------
-- 7. Unprofitable Products (Loss Makers using HAVING)
-- Which products are causing financial losses due to discounts/returns?
-- ---------------------------------------------------------------
SELECT 
    Product_Name,
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales_INR,
    ROUND(SUM(Profit), 2) AS Net_Loss_INR
FROM sales_orders
GROUP BY Product_Name, Category
HAVING SUM(Profit) < 0
ORDER BY Net_Loss_INR ASC;

-- ---------------------------------------------------------------
-- 8. Sales & Profit by Indian Region
-- How does performance vary across West, North, East, and South India?
-- ---------------------------------------------------------------
SELECT 
    Region,
    COUNT(DISTINCT Order_ID) AS Orders_Count,
    ROUND(SUM(Sales), 2) AS Total_Sales_INR,
    ROUND(SUM(Profit), 2) AS Total_Profit_INR,
    ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin_Pct
FROM sales_orders
GROUP BY Region
ORDER BY Total_Sales_INR DESC;

-- ---------------------------------------------------------------
-- 9. Top 7 Indian States by Revenue
-- Which states are the primary geographic markets?
-- ---------------------------------------------------------------
SELECT 
    State,
    Region,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(SUM(Sales), 2) AS Total_Sales_INR
FROM sales_orders
GROUP BY State, Region
ORDER BY Total_Sales_INR DESC
LIMIT 7;

-- ---------------------------------------------------------------
-- 10. Payment Method Share in India
-- How do Indian consumers pay (UPI vs Cards vs Cash on Delivery)?
-- ---------------------------------------------------------------
SELECT 
    Payment_Method,
    COUNT(DISTINCT Order_ID) AS Orders_Count,
    ROUND(SUM(Sales), 2) AS Total_Sales_INR,
    ROUND((COUNT(DISTINCT Order_ID) * 100.0 / (SELECT COUNT(*) FROM sales_orders)), 2) AS Order_Share_Pct
FROM sales_orders
GROUP BY Payment_Method
ORDER BY Orders_Count DESC;

-- ---------------------------------------------------------------
-- 11. Order Fulfillment Status Breakdown
-- What percentage of orders are Delivered vs Returned or Cancelled?
-- ---------------------------------------------------------------
SELECT 
    Order_Status,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND((COUNT(DISTINCT Order_ID) * 100.0 / (SELECT COUNT(*) FROM sales_orders)), 2) AS Status_Share_Pct
FROM sales_orders
GROUP BY Order_Status
ORDER BY Total_Orders DESC;

-- ---------------------------------------------------------------
-- 12. Monthly Sales Trend (Seasonality)
-- How do sales progress month over month?
-- ---------------------------------------------------------------
SELECT 
    SUBSTR(Order_Date, 1, 7) AS Order_Month,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    ROUND(SUM(Sales), 2) AS Monthly_Sales_INR,
    ROUND(SUM(Profit), 2) AS Monthly_Profit_INR
FROM sales_orders
GROUP BY SUBSTR(Order_Date, 1, 7)
ORDER BY Order_Month ASC;

-- ---------------------------------------------------------------
-- 13. Top 5 Spenders with Customer Tiering (Using CASE WHEN)
-- Segmenting top Indian customers into Platinum, Gold, and Silver tiers
-- ---------------------------------------------------------------
SELECT 
    Customer_Name,
    COUNT(DISTINCT Order_ID) AS Orders_Count,
    ROUND(SUM(Sales), 2) AS Total_Spent_INR,
    CASE 
        WHEN SUM(Sales) >= 1200000 THEN 'Platinum VIP (Above ₹12L)'
        WHEN SUM(Sales) >= 800000 THEN 'Gold Tier (₹8L - ₹12L)'
        ELSE 'Silver Tier (Under ₹8L)'
    END AS Customer_Tier
FROM sales_orders
GROUP BY Customer_Name
ORDER BY Total_Spent_INR DESC
LIMIT 5;