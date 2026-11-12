CREATE SCHEMA IF NOT EXISTS staging;

CREATE OR REPLACE VIEW staging.stg_players AS
SELECT
    player_id,
    registration_date,
    UPPER(TRIM(country))    AS country,
    LOWER(TRIM(kyc_status)) AS kyc_status
FROM raw.players;

CREATE OR REPLACE VIEW staging.stg_transactions AS
SELECT
    transaction_id,
    player_id,
    amount,
    created_at,
    LOWER(TRIM(status))    AS status,
    LOWER(TRIM(payment_method)) AS payment_method,
    LOWER(TRIM(type)) AS type
FROM raw.transactions;