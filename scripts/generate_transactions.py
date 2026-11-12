import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

players = pd.read_csv("data/raw/players.csv", parse_dates=["registration_date"])

# 1. Скільки депозитів зробить кожен гравець
n_deposits = rng.poisson(lam=4, size=len(players))
no_deposit = rng.random(len(players)) < 0.6
n_deposits[no_deposit] = 0

# 2. Один рядок = один депозит
deposits = pd.DataFrame({
    "player_id": np.repeat(players["player_id"].to_numpy(), n_deposits),
})
deposits["amount"] = rng.integers(10, 500, len(deposits))
# 3. Дата депозиту = дата реєстрації + 0..44 днів
deposits = deposits.merge(players[["player_id", "registration_date"]],
                          on="player_id", how="left")
deposits["created_at"] = deposits["registration_date"] + pd.to_timedelta(
    rng.integers(0, 45, len(deposits)), unit="D")
deposits["status"] = rng.choice(["approved", "declined"], len(deposits), p=[0.9, 0.1])
deposits["payment_method"] = rng.choice(["card", "e-wallet", "crypto"], len(deposits), p=[0.6, 0.3, 0.1])

# 4. Виводи: 40% успішних депозитів закінчуються виводом
approved = deposits[deposits["status"] == "approved"]
withdrawals = approved.sample(frac=0.4, random_state=42)
withdrawals = withdrawals[["player_id", "created_at", "payment_method"]].copy()
withdrawals["amount"] = rng.integers(20, 1000, len(withdrawals))

withdrawals = withdrawals.merge(players[["player_id", "kyc_status"]],
                                on="player_id", how="left")
withdrawals["status"] = np.where(withdrawals["kyc_status"] == "approved",
                                 "approved", "pending")
withdrawals["created_at"] = withdrawals["created_at"] + pd.to_timedelta(
    rng.integers(1, 4, len(withdrawals)), unit="D")

# 5. Збираємо все в одну таблицю
deposits["type"] = "deposit"
deposits = deposits.drop(columns=["registration_date"])

withdrawals["type"] = "withdrawal"
withdrawals = withdrawals.drop(columns=["kyc_status"])

transactions = pd.concat([deposits, withdrawals], ignore_index=True)
transactions = transactions.sort_values("created_at", kind="stable").reset_index(drop=True)
transactions.insert(0, "transaction_id", range(1, len(transactions) + 1))

transactions.to_csv("data/raw/transactions.csv", index=False)
print(transactions.head())
print(transactions["type"].value_counts())

