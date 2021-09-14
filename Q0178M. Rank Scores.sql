#Runtime: 265 ms, faster than 58.25% of MySQL online submissions for Rank Scores.
#Memory Usage: 0B, less than 100.00% of MySQL online submissions for Rank Scores.

# Write your MySQL query statement below
SELECT Score, DENSE_RANK()
OVER (ORDER BY Score DESC)
`Rank`
FROM Scores
