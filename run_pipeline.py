import subprocess
import sys

STEPS = [
    "scripts/generate_players.py",
    "scripts/generate_transactions.py",
    "scripts/load_to_duckdb.py",
    "scripts/run_sql.py",
    "scripts/export_marts.py",
    "scripts/run_analysis.py"
]

for step in STEPS:
    print(f"\n>> Running {step}")
    subprocess.run([sys.executable, step], check=True)

print("\nPipeline finished successfully")