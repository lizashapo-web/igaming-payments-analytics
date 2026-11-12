import duckdb
from pathlib import Path

Path("data/marts").mkdir(parents=True, exist_ok=True)

con = duckdb.connect("igaming.duckdb", read_only=True)

for table in ["dim_players", "fact_transactions"]:
    con.execute(f"COPY mart.{table} TO 'data/marts/{table}.csv' (HEADER)")
    print(f"Exported {table}")

con.close()