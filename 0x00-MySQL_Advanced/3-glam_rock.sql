--
SELECT
    band_name,
    ABS(EXTRACT(YEAR FROM split) - EXTRACT(YEAR FROM formed)) as lifespan
FROM
    metal_bands
Where
    style = 'Glam rock'
ORDER BY
    lifespan DESC;