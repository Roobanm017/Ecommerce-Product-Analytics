import pandas as pd

# Load Data
df = pd.read_csv("../data/raw_products.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Remove rows where product name is missing
df = df.dropna(subset=["product_name"])

# Convert prices to numeric
df["actual_price"] = pd.to_numeric(
    df["actual_price"],
    errors="coerce"
)

df["selling_price"] = pd.to_numeric(
    df["selling_price"],
    errors="coerce"
)

df["offer_percentage"] = pd.to_numeric(
    df["offer_percentage"],
    errors="coerce"
)

# Remove rows with invalid prices
df = df.dropna(
    subset=[
        "actual_price",
        "selling_price"
    ]
)

# Save cleaned file
df.to_csv(
    "../data/cleaned_products.csv",
    index=False
)

print("\nCleaning Completed Successfully")
print("Final Shape:", df.shape)