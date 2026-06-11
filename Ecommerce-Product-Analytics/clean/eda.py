import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("../data/cleaned_products.csv")

# =====================
# 1. Top Cities
# =====================

plt.figure(figsize=(10,5))

df["city"].value_counts().plot(
    kind="bar"
)

plt.title("Products by City")
plt.xlabel("City")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

# =====================
# 2. Price Distribution
# =====================

plt.figure(figsize=(10,5))

plt.hist(
    df["selling_price"],
    bins=30
)

plt.title("Selling Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

# =====================
# 3. Discount Category
# =====================

plt.figure(figsize=(8,5))

df["discount_category"].value_counts().plot(
    kind="bar"
)

plt.title("Discount Categories")
plt.xlabel("Category")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

# =====================
# 4. Price Segment
# =====================

plt.figure(figsize=(8,5))

df["price_segment"].value_counts().plot(
    kind="bar"
)

plt.title("Price Segments")
plt.xlabel("Segment")
plt.ylabel("Count")

plt.tight_layout()
plt.show()

# =====================
# 5. Top Savings Products
# =====================

top_savings = df.sort_values(
    by="savings",
    ascending=False
).head(10)

print("\nTop 10 Savings Products")
print(
    top_savings[
        [
            "product_name",
            "savings"
        ]
    ]
)

print("\nEDA Completed Successfully")