-- Load data/processed/sales_clean.csv into a table named sales, then try these.
-- 1. Revenue by category
SELECT category, ROUND(SUM(revenue),2) AS total_revenue
FROM sales GROUP BY category ORDER BY total_revenue DESC;

-- 2. Monthly revenue trend
SELECT month, ROUND(SUM(revenue),2) AS total_revenue
FROM sales GROUP BY month ORDER BY month;

-- 3. Top 5 customers
SELECT customer_id, ROUND(SUM(revenue),2) AS total_revenue
FROM sales GROUP BY customer_id ORDER BY total_revenue DESC LIMIT 5;

-- 4. Average order value by region
SELECT region, ROUND(AVG(revenue),2) AS avg_order_value
FROM sales GROUP BY region ORDER BY avg_order_value DESC;
