SELECT
    country,
    COUNT(*)                  AS registrations,
    COUNT(first_deposit_date) AS ftd_players,
    ROUND(100.0 * COUNT(first_deposit_date) / COUNT(*), 1) AS ftd_conversion_pct
FROM mart.dim_players
GROUP BY country
ORDER BY ftd_conversion_pct DESC;