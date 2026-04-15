import streamlit as st
import pandas as pd

# Title and description
st.title("📊 Sales Summary Dashboard")
st.subheader("Simple interactive app to filter sales data by category")

# Create hardcoded dataset
data = {
    "Product": ["Laptop", "Shirt", "Mobile", "Jeans", "Tablet"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics"],
    "Sales": [50000, 2000, 30000, 2500, 15000]
}

df = pd.DataFrame(data)

# Sidebar filter
st.sidebar.header("Filter Options")
category = st.sidebar.selectbox("Select Category", df["Category"].unique())

# Filter data
filtered_df = df[df["Category"] == category]

# Display filtered data
st.write(f"### Showing data for: {category}")
st.dataframe(filtered_df)

# Line chart
st.write("### Sales Trend")
st.line_chart(filtered_df["Sales"])