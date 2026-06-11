-- Total Products

SELECT COUNT(*) AS total_products
FROM products;

------------------------------------------------

-- Average Selling Price

SELECT AVG(selling_price)
AS avg_price
FROM products;

------------------------------------------------

-- Average Discount

SELECT AVG(offer_percentage)
AS avg_discount
FROM products;

------------------------------------------------

-- Top 10 Expensive Products

SELECT
product_name,
selling_price

FROM products

ORDER BY selling_price DESC

LIMIT 10;

------------------------------------------------

-- Top 10 Savings Products

SELECT
product_name,
savings

FROM products

ORDER BY savings DESC

LIMIT 10;

------------------------------------------------

-- Product Count By City

SELECT
city,
COUNT(*) AS total_products

FROM products

GROUP BY city

ORDER BY total_products DESC;

------------------------------------------------

-- Price Segment Analysis

SELECT
price_segment,
COUNT(*) AS total_products

FROM products

GROUP BY price_segment;

------------------------------------------------

-- Discount Category Analysis

SELECT
discount_category,
COUNT(*) AS total_products

FROM products

GROUP BY discount_category;