#Runtime: 282 ms, faster than 95.28% of MySQL online submissions for Employees Earning More Than Their Managers.
#Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees Earning More Than Their Managers.

# Write your MySQL query statement below
SELECT a.Name AS Employee 
FROM Employee AS a, Employee AS b
WHERE a.ManagerId = b.Id 
    AND a.Salary > b.Salary;
