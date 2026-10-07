import pandas as pd
from config import RAW_FILE
df = pd.read_csv(RAW_FILE)
checks = {
    "row_count": len(df),
    "duplicate_order_ids": int(df["order_id"].duplicated().sum()),
    "missing_customer_names": int(df["customer_name"].isna().sum()),
    "negative_quantity": int((df["quantity"] < 0).sum()),
    "negative_unit_price": int((df["unit_price"] < 0).sum())
}
print("DATA QUALITY REPORT")
for k,v in checks.items():
    print(f"{k}: {v}")
failed = any(v > 0 for k,v in checks.items() if k != "row_count")
print("\nSTATUS:", "FAIL - cleaning required" if failed else "PASS")
