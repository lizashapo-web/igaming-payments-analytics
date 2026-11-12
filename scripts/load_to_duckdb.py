import duckdb

con = duckdb.connect("igaming.duckdb")

con.execute("CREATE SCHEMA IF NOT EXISTS raw")

con.execute("""
    CREATE OR REPLACE TABLE raw.players AS
    SELECT * FROM read_csv_auto('data/raw/players.csv')
""")

con.sql("SELECT COUNT(*) AS players FROM raw.players").show()
con.sql("DESCRIBE raw.players").show()

con.close()

import duckdb

con = duckdb.connect("igaming.duckdb")

con.execute("CREATE SCHEMA IF NOT EXISTS raw")

con.execute("""
    CREATE OR REPLACE TABLE raw.transactions AS
    SELECT * FROM read_csv_auto('data/raw/transactions.csv')
""")

con.sql("SELECT COUNT(*) AS transactions FROM raw.transactions").show()
con.sql("DESCRIBE raw.transactions").show()

con.close()