-- Total sales
SELECT ROUND(SUM(net_sales), 2) AS total_sales
FROM fact_orders
WHERE order_status = 'Completed';

-- Sales by region
SELECT region, ROUND(SUM(net_sales), 2) AS sales
FROM fact_orders
WHERE order_status = 'Completed'
GROUP BY region
ORDER BY sales DESC;

-- Top products
SELECT product_name, ROUND(SUM(net_sales), 2) AS sales
FROM fact_orders
WHERE order_status = 'Completed'
GROUP BY product_name
ORDER BY sales DESC
LIMIT 10;

-- Monthly sales
SELECT substr(order_date,1,7) AS month,
       ROUND(SUM(net_sales),2) AS sales
FROM fact_orders
WHERE order_status = 'Completed'
GROUP BY month
ORDER BY month;

-- Average order value
SELECT ROUND(SUM(net_sales)/COUNT(DISTINCT order_id),2) AS avg_order_value
FROM fact_orders
WHERE order_status = 'Completed';

SELECT
    SUM(net_sales) AS total_sales
FROM fact_orders;