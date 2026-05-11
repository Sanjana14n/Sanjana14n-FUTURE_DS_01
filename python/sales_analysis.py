import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r'dataset/Sample - Superstore.csv', encoding='latin1')

# Show first 5 rows
print(df.head())

# Total Sales
total_sales = df['Sales'].sum()
print("Total Sales:", total_sales)

# Sales by Region
sales_by_region = df.groupby('Region')['Sales'].sum()

# Create bar chart
sales_by_region.plot(kind='bar')

# Chart title
plt.title('Sales by Region')

# X and Y labels
plt.xlabel('Region')
plt.ylabel('Sales')

# Save chart
plt.savefig('images/revenue_by_region.png')

# Show chart
plt.show()

# Profit by Category
profit_by_category = df.groupby('Category')['Profit'].sum()

# Create pie chart
profit_by_category.plot(kind='pie', autopct='%1.1f%%')

# Title
plt.title('Profit by Category')

# Save image
plt.savefig('images/profit_by_category.png')

# Show chart
plt.show()

# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Monthly Sales Trend
monthly_sales = df.groupby(df['Order Date'].dt.month)['Sales'].sum()

# Line chart
monthly_sales.plot(kind='line', marker='o')

# Title
plt.title('Monthly Sales Trend')

# Labels
plt.xlabel('Month')
plt.ylabel('Sales')

# Save image
plt.savefig('images/monthly_sales_trend.png')

# Show chart
plt.show()

# Top 10 Products by Sales
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

# Horizontal bar chart
top_products.plot(kind='barh')

# Title
plt.title('Top 10 Products by Sales')

# Labels
plt.xlabel('Sales')
plt.ylabel('Product Name')

# Save image
plt.savefig('images/top_products_sales.png')

# Show chart
plt.show()