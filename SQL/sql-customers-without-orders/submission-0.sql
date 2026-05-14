-- Write your query below
SELECT name from customers AS c
LEFT JOIN orders AS o ON o.customer_id = c.id
WHERE customer_id is NULL 