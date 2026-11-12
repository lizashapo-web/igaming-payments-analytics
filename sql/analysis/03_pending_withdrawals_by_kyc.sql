SELECT
    d.kyc_status,
    COUNT(*) AS pending_withdrawals,
    COUNT(DISTINCT f.player_id) AS players,
    SUM(f.amount) AS stuck_amount
FROM mart.fact_transactions f
INNER JOIN mart.dim_players d
ON f.player_id = d.player_id
WHERE f.type = 'withdrawal'
    AND f.status = 'pending'
GROUP BY d.kyc_status;