#Runtime: 380 ms, faster than 93.24% of MySQL online submissions for Customers Who Never Order.
#Memory Usage: 0B, less than 100.00% of MySQL online submissions for Customers Who Never Order.

# Write your MySQL query statement below
SELECT Name AS Customers FROM Customers
LEFT JOIN Orders
ON Customers.Id = Orders.CustomerId
WHERE Orders.CustomerId IS Null
