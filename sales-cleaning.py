import pandas as pd
from pathlib import Path

IN_FILE  = "Sales_Product_Combined.csv"
OUT_FILE = "Sales_Cleaned_Dates_Dupes.csv"

df = pd.read_csv(IN_FILE)
orig_rows = len(df)

# remove trailing/before spaces and join only on simple space " "
obj_cols = df.select_dtypes(include="object").columns
for col in obj_cols:
    s = df[col].astype(str)
    s = s.str.strip().str.split().str.join(" ")
    df[col] = s

# parse and keep dates as datetime for future checks
if "Order Date" in df.columns:
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce", dayfirst=True)
    bad_order_dates = df["Order Date"].isna().sum()
    df = df.dropna(subset=["Order Date"])
else:
    bad_order_dates = 0


# check numeric columns are numeric
num_cols = [c for c in ["Price", "Quantity", "Sales", "Profit", "Discount"] if c in df.columns]
for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# remove negatives prices
neg_price = 0
if "Price" in df.columns:
    neg_price = int((df["Price"] < 0).sum())
    df = df[(df["Price"].isna()) | (df["Price"] >= 0)]

# remove duplicates
keys = [c for c in ["Order ID", "Product", "Order Date", "Price"] if c in df.columns]
before_dupes = len(df)
df = df.drop_duplicates(subset=keys if keys else None, keep="first")
dupes_removed = before_dupes - len(df)

# use title for customer name
if "Customer Name" in df.columns:
    df["Customer Name"] = df["Customer Name"].str.title()

# format dates as yyyy-mm-dd
if "Order Date" in df.columns:
    df["Order Date"] = df["Order Date"].dt.strftime("%Y-%m-%d")


df.to_csv(OUT_FILE, index=False, encoding="utf-8")


print(f"Input rows:               {orig_rows}")
print(f"Dropped bad order dates:  {bad_order_dates}")
print(f"Removed negative price:   {neg_price}")
print(f"Duplicates removed:       {dupes_removed}")
print(f"Output rows:              {len(df)}")
print(f"Saved -> {Path(OUT_FILE).resolve()}")