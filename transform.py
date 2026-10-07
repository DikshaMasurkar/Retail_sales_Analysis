import pandas as pd
from config import RAW_FILE, PROCESSED_FILE

df = pd.read_csv(RAW_FILE)
df = df.drop_duplicates(subset=["order_id"], keep="first")

for col in ["customer_name","product_name","category","region","city","order_status"]:
    df[col] = df[col].fillna("Unknown").astype(str).str.strip()

df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").fillna(0)
df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce").fillna(0)
df["discount_pct"] = pd.to_numeric(df["discount_pct"], errors="coerce").fillna(0)

df.loc[df["quantity"] < 0, "quantity"] = 0
df.loc[df["unit_price"] < 0, "unit_price"] = 0
df["discount_pct"] = df["discount_pct"].clip(0, 1)

df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df["gross_sales"] = df["quantity"] * df["unit_price"]
df["discount_amount"] = df["gross_sales"] * df["discount_pct"]
df["net_sales"] = df["gross_sales"] - df["discount_amount"]

df = df.dropna(subset=["order_id","order_date","product_id","customer_id"])
df.to_csv(PROCESSED_FILE, index=False)
print(f"Saved {len(df):,} cleaned records to {PROCESSED_FILE}")
