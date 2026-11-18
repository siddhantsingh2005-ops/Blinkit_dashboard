import pandas as pd

data = {
    
    "Customer": ["Amit", "Ravi", "Priya", "Neha", "Rahul", "Siddhant", "Abuzer", "khabib", "Asadulla", "Johnson", "Aslamjon", "Rodtang", "Carlos", "Islam"],
    "Order_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114],
    "Item_type": ["Medicine", "Groceries", "Stationary", "Groceries", "Snacks", "Drinks", "Accessories", "Decoratives", "Wraps", "Gloves", "Clothes", "Stationary",
     "Snacks", "Medicine"],
    "Address": [
    "House No. 12, Boring Road, Patna",
    "Flat 203, Kankarbagh, Patna",
    "House No. 45, Rajendra Nagar, Patna",
    "Flat 101, Bailey Road, Patna",
    "House No. 88, Danapur, Patna",
    "Flat 304, Patliputra Colony, Patna",
    "House No. 22, Ashok Rajpath, Patna",
    "Flat 210, Fraser Road, Patna",
    "House No. 56, Kurji, Patna",
    "Flat 105, Airport Road, Patna",
    "House No. 72, Gola Road, Patna",
    "Flat 402, Anisabad, Patna",
    "House No. 11, Saguna More, Patna",
    "Flat 307, Mithapur, Patna"
],
    
    "Bill": [2500, 3000, 1180, 4950, 3420, 4009, 2026, 3999, 2733, 3389, 10000, 23339, 666, 2767,],
    "Payment_method": ["Online", "Online", "Cash", "Card", "Online", "Cash", "Card", "Online", "Cash", "Card", "Online", "Cash", "Card", "Online"],
    "Status": ["Completed", "Cancelled", "Completed", "Completed", "Cancelled", "Completed", "Completed", "Not delivered", "Completed", "Cancelled", "Completed",
    "Completed", "Completed", "Cancelled"]
   
}

df = pd.DataFrame(data)

pd.set_option('display.max_columns', None)

print(df)

# --------------------------
# DATA CLEANING
# --------------------------

# Check missing values
print("Missing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicates if any
df.drop_duplicates(inplace=True)

# Standardize text columns
df["Customer"] = df["Customer"].str.title()
df["Item_type"] = df["Item_type"].str.title()
df["Payment_method"] = df["Payment_method"].str.title()
df["Status"] = df["Status"].str.title()

print("\nDataset Shape:", df.shape)

# --------------------------
# IQR OUTLIER DETECTION
# --------------------------

Q1 = df["Bill"].quantile(0.25)
Q3 = df["Bill"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

outliers = df[
    (df["Bill"] < lower_bound) |
    (df["Bill"] > upper_bound)
]

print("\nOutliers:")
print(outliers)

# Add Outlier Column

df["Outlier"] = (
    (df["Bill"] < lower_bound) |
    (df["Bill"] > upper_bound)
)

# --------------------------
# KPI CALCULATIONS
# --------------------------

total_orders = len(df)

total_revenue = df["Bill"].sum()

average_order_value = df["Bill"].mean()

highest_bill = df["Bill"].max()

lowest_bill = df["Bill"].min()

completed_orders = len(
    df[df["Status"] == "Completed"]
)

cancelled_orders = len(
    df[df["Status"] == "Cancelled"]
)

not_delivered = len(
    df[df["Status"] == "Not Delivered"]
)

completion_rate = (
    completed_orders / total_orders
) * 100

cancellation_rate = (
    cancelled_orders / total_orders
) * 100

online_payments = len(
    df[df["Payment_method"] == "Online"]
)

cash_payments = len(
    df[df["Payment_method"] == "Cash"]
)

card_payments = len(
    df[df["Payment_method"] == "Card"]
)

unique_customers = \
df["Customer"].nunique()

unique_categories = \
df["Item_type"].nunique()

outlier_count = \
df["Outlier"].sum()


print("\n------------- KPIs -------------")

print("Total Orders =", total_orders)

print("Total Revenue =", total_revenue)

print("Average Order Value =", average_order_value)

print("Highest Bill =", highest_bill)

print("Lowest Bill =", lowest_bill)

print("Completed Orders =", completed_orders)

print("Cancelled Orders =", cancelled_orders)

print("Not Delivered =", not_delivered)

print("Completion Rate =", completion_rate)

print("Cancellation Rate =", cancellation_rate)

print("Online Payments =", online_payments)

print("Cash Payments =", cash_payments)

print("Card Payments =", card_payments)

print("Unique Customers =", unique_customers)

print("Unique Categories =", unique_categories)

print("Outliers =", outlier_count)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(7,5))

sns.histplot(df["Bill"], bins=8)

plt.title("Bill Distribution")

plt.show()

plt.figure(figsize=(6,4))

sns.countplot(
    x="Payment_method",
    data=df
)

plt.title("Payment Methods")

plt.show()

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Blinkit Dashboard",
    layout="wide"
)

st.title("Blinkit Analytics Dashboard")

df = pd.DataFrame(data)

# KPIs

st.subheader("KPIs")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Orders",
    len(df)
)

col2.metric(
    "Revenue",
    f"₹{df['Bill'].sum():,.0f}"
)

col3.metric(
    "Average Bill",
    f"₹{df['Bill'].mean():.2f}"
)

col4.metric(
    "Highest Bill",
    f"₹{df['Bill'].max()}"
)

# Dataset

st.subheader("Dataset")

st.dataframe(df)

# Payment Method

st.subheader("Payment Method Count")

st.bar_chart(
    df["Payment_method"]
    .value_counts()
)

# Status

st.subheader("Order Status")

st.bar_chart(
    df["Status"]
    .value_counts()
)

# Category

st.subheader("Item Type")

st.bar_chart(
    df["Item_type"]
    .value_counts()
)