-- Task 2

-- Ranks country origins of bands, ordered by the number of (non-unique) fans
SELECT origin, COUNT(fans) AS nb_fans FROM metal_bands WHERE nb_fans > 1 GROUP BY origin ORDER BY COUNT(fans) DESC;
