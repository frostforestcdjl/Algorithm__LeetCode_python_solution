#Runtime: 254 ms, faster than 99.29% of MySQL online submissions for Duplicate Emails.
#Memory Usage: 0B, less than 100.00% of MySQL online submissions for Duplicate Emails.

# Write your MySQL query statement below
SELECT Email FROM Person
GROUP BY Email
HAVING COUNT(Email) > 1;
