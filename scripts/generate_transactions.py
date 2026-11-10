import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

players = pd.read_csv("data/raw/players.csv")

# 1. Скільки депозитів зробить кожен гравець
n_deposits = rng.poisson(lam=4, size=len(players))
print(n_deposits[:10])

# 2. Один рядок = один депозит
deposits = pd.DataFrame({
    "player_id": np.repeat(players["player_id"].to_numpy(), n_deposits),
})
deposits["amount"] = rng.integers(10, 500, len(deposits))
print(deposits.head(10))
print(f"Total deposits: {len(deposits)}")