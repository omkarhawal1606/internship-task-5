import os
import pandas as pd
import matplotlib.pyplot as plt

print(os.getcwd())  # to check current directory

# Load the CSV file (make sure it's in the same folder)
df = pd.read_csv('sales_data.csv')

# Display first few rows
print(df.head())

# Basic info
print(df.info())
print(df.describe())

# Check missing values
print(df.isnull().sum())

# Grouping & Summarizing
sales_by_product = df.groupby('Product')['Sales'].sum().reset_index()
print(sales_by_product)

sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()
print(sales_by_region)

# Date column and monthly sales
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()
print(monthly_sales)

# Charts
plt.figure(figsize=(8,5))
plt.bar(sales_by_product['Product'], sales_by_product['Sales'])
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.show()

plt.figure(figsize=(8,5))
plt.bar(sales_by_region['Region'], sales_by_region['Sales'], color='orange')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.show()

plt.figure(figsize=(10,5))
plt.plot(monthly_sales['Month'].astype(str), monthly_sales['Sales'], marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
