import pandas as pd
from config import RAW_FILE
df = pd.read_csv(RAW_FILE)
print(f"Ingested {len(df):,} records")
print(df.head())
print(df.dtypes)
