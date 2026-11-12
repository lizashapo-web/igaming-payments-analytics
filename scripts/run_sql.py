import duckdb
from pathlib import Path

con = duckdb.connect("igaming.duckdb")

for sql_file in sorted(Path("sql").glob("*.sql")):
    print(f"Running {sql_file.name}...")
    con.execute(sql_file.read_text(encoding="utf-8"))

con.sql("SELECT * FROM staging.stg_players LIMIT 5").show()
con.sql("SELECT * FROM staging.stg_transactions LIMIT 5").show()

con.close()