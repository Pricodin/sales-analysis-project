"""Generate a SYNTHETIC retail sales dataset with deliberate data-quality problems.
This is practice data, not real business data."""
import numpy as np, pandas as pd
rng = np.random.default_rng(42)
N = 1000
products = {
    "Electronics": {"Headphones": 80, "Smartwatch": 150, "Speaker": 60},
    "Clothing": {"T-Shirt": 15, "Jeans": 40, "Jacket": 90},
    "Home": {"Lamp": 25, "Cushion": 12, "Kettle": 30},
    "Grocery": {"Coffee": 9, "Snacks Box": 14, "Olive Oil": 11},
}
dates = pd.date_range("2025-01-01", "2025-12-31")
w = np.array([1.6 if d.month in (11, 12) else 1.0 for d in dates]); w /= w.sum()
rows = []
for i in range(N):
    cat = rng.choice(list(products))
    prod = rng.choice(list(products[cat]))
    price = round(products[cat][prod] * rng.uniform(0.9, 1.1), 2)
    rows.append({
        "order_id": 10000 + i,
        "order_date": rng.choice(dates, p=w).strftime("%Y-%m-%d") if False else pd.Timestamp(rng.choice(dates, p=w)).strftime("%Y-%m-%d"),
        "customer_id": f"C{rng.integers(1, 301):04d}",
        "region": str(rng.choice(["North", "South", "East", "West"], p=[.3, .25, .25, .2])),
        "category": str(cat), "product": str(prod),
        "quantity": int(rng.integers(1, 6)),
        "unit_price": price,
        "discount": float(rng.choice([0, 0, 0, 0.05, 0.1, 0.2])),
        "payment_method": str(rng.choice(["Card", "UPI", "Cash", "Wallet"], p=[.4, .35, .15, .1])),
    })
df = pd.DataFrame(rows)
# ---- inject problems ----
idx = rng.choice(df.index, 30, replace=False); df.loc[idx, "region"] = np.nan
idx = rng.choice(df.index, 40, replace=False); df.loc[idx, "discount"] = np.nan
idx = rng.choice(df.index, 40, replace=False)
df.loc[idx, "region"] = df.loc[idx, "region"].map(lambda x: x.lower() if isinstance(x, str) else x)
idx = rng.choice(df.index, 20, replace=False)
df.loc[idx, "region"] = df.loc[idx, "region"].map(lambda x: f"  {x} " if isinstance(x, str) else x)
df.loc[rng.choice(df.index, 5, replace=False), "quantity"] = 500      # outliers
df.loc[rng.choice(df.index, 3, replace=False), "unit_price"] = -10    # invalid
df = pd.concat([df, df.sample(25, random_state=1)], ignore_index=True)  # duplicates
df = df.sample(frac=1, random_state=7).reset_index(drop=True)
df.to_csv("data/raw/sales_raw.csv", index=False)
print("Saved data/raw/sales_raw.csv", df.shape)
