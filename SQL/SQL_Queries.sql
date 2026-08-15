-- Select Database
USE sales_db;

-- Show Available Tables
SHOW TABLES;

-- Display First 10 Records
SELECT *
FROM apexplanet_dataanalytics_dataset
LIMIT 10;

-- Total Number of Orders
SELECT COUNT(*) AS Total_Orders
FROM apexplanet_dataanalytics_dataset;

-- Total Revenue
SELECT SUM(Total_Sales) AS Total_Revenue
FROM apexplanet_dataanalytics_dataset;

-- Average Order Value
SELECT ROUND(AVG(Total_Sales), 2) AS Average_Order_Value
FROM apexplanet_dataanalytics_dataset;

-- Top 5 Products by Revenue
SELECT Product,
       ROUND(SUM(Total_Sales), 2) AS Revenue
FROM apexplanet_dataanalytics_dataset
GROUP BY Product
ORDER BY Revenue DESC
LIMIT 5;

-- Total Sales by Category
SELECT Category,
       ROUND(SUM(Total_Sales), 2) AS Total_Sales
FROM apexplanet_dataanalytics_dataset
GROUP BY Category
ORDER BY Total_Sales DESC;

-- Top 5 Cities by Total Sales
SELECT City,
       ROUND(SUM(Total_Sales), 2) AS Total_Sales
FROM apexplanet_dataanalytics_dataset
GROUP BY City
ORDER BY Total_Sales DESC
LIMIT 5;

-- Total Sales by Gender
SELECT Gender,
       ROUND(SUM(Total_Sales), 2) AS Total_Sales
FROM apexplanet_dataanalytics_dataset
GROUP BY Gender;

-- Average Customer Age
SELECT ROUND(AVG(Age), 2) AS Average_Age
FROM apexplanet_dataanalytics_dataset;