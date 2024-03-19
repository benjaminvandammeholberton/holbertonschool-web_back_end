-- Task 3

-- lists all band with 'Glam rock' as their main style, ranked by their longevity
SELECT band_name, (IFNULL(split, YEAR(CURDATE())) - formed) as lifespan FROM metal_bands WHERE INSTR(style, 'Glam rock') > 0 ORDER BY lifespan DESC