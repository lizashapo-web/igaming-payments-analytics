CREATE SCHEMA IF NOT EXISTS mart;

CREATE OR REPLACE TABLE mart.dim_players AS
SELECT
    p.player_id,
    p.registration_date,
    p.country,
    p.kyc_status,
    MIN(t.created_at) AS first_deposit_date
FROM staging.stg_players p
LEFT JOIN staging.stg_transactions t
    ON  p.player_id = t.player_id
    AND t.type = 'deposit'
    AND t.status = 'approved'
GROUP BY p.player_id, p.registration_date, p.country, p.kyc_status;

CREATE OR REPLACE TABLE mart.fact_transactions AS
SELECT
    t.transaction_id,
    t.player_id,
    t.amount,
    t.created_at,
    t.status,
    t.payment_method,
    t.type,
    CASE WHEN t.type = 'deposit' THEN t.amount ELSE -t.amount END AS signed_amount
FROM staging.stg_transactions t;