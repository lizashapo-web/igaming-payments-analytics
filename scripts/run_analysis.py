import duckdb
from pathlib import Path

con = duckdb.connect("igaming.duckdb", read_only=True)

for sql_file in sorted(Path("sql/analysis").glob("*.sql")):
    print(f"\n=== {sql_file.stem} ===")
    con.sql(sql_file.read_text(encoding="utf-8")).show()

con.close()