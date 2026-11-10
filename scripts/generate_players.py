import numpy as np
import pandas as pd

rng = np.random.default_rng(42)   # генератор випадкових чисел з "зерном" 42

N_PLAYERS = 1000

players = pd.DataFrame({
    "player_id": range(1, N_PLAYERS + 1),
    "registration_date": pd.to_datetime("2026-01-01")
        + pd.to_timedelta(rng.integers(0, 270, N_PLAYERS), unit="D"),
    "country": rng.choice(["UA", "PL", "DE", "CA", "BR"], N_PLAYERS,
                          p=[0.35, 0.25, 0.15, 0.15, 0.10]),
    "kyc_status": rng.choice(["approved", "pending", "rejected"], N_PLAYERS,
                             p=[0.70, 0.20, 0.10]),
})

players.to_csv("data/raw/players.csv", index=False)
print(players.head())
print(f"Saved {len(players)} players")