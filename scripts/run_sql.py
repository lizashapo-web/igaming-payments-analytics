import duckdb
from pathlib import Path

con = duckdb.connect("igaming.duckdb")

for sql_file in sorted(Path("sql").glob("*.sql")):
    print(f"Running {sql_file.name}...")
    con.execute(sql_file.read_text(encoding="utf-8"))

con.sql("SELECT * FROM mart.dim_players WHERE player_id IN (1, 5)").show()
con.sql("SELECT * FROM mart.fact_transactions WHERE type = 'withdrawal' LIMIT 5").show()
con.sql("SELECT COUNT(*) AS total_players, COUNT(first_deposit_date) AS players_with_ftd FROM mart.dim_players").show()

con.close()