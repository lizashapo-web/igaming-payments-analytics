SELECT 
    CAST(DATE_TRUNC('month', created_at) AS DATE) AS month,
    SUM(signed_amount)                            AS net_deposits
FROM mart.fact_transactions
WHERE status = 'approved'
GROUP BY month 
ORDER BY month ASC;