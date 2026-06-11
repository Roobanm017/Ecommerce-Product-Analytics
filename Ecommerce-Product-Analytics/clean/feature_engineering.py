import pandas as pd

# Load cleaned data
df = pd.read_csv("../data/cleaned_products.csv")

# Savings
df["savings"] = df["actual_price"] - df["selling_price"]

# Discount Category
def discount_category(x):
    if x <= 10:
        return "Low"
    elif x <= 25:
        return "Medium"
    else:
        return "High"

df["discount_category"] = df["offer_percentage"].apply(discount_category)

# Price Segment
def price_segment(x):
    if x <= 100:
        return "Budget"
    elif x <= 300:
        return "Mid Range"
    else:
        return "Premium"

df["price_segment"] = df["selling_price"].apply(price_segment)

# Delivery Category
def delivery_category(x):
    if pd.isna(x):
        return "Unknown"

    x = str(x)

    if "9" in x:
        return "Fast"
    elif "15" in x:
        return "Medium"
    else:
        return "Slow"

df["delivery_category"] = df["delivery_time"].apply(
    delivery_category
)

# Save file
df.to_csv(
    "../data/cleaned_products.csv",
    index=False
)

print("Feature Engineering Completed Successfully")

print("\nNew Columns Added:")
print([
    "savings",
    "discount_category",
    "price_segment",
    "delivery_category"
])

print("\nDataset Shape:")
print(df.shape)