import pandas as pd
import sqlite3

print("--- Starting ETL Pipeline ---")

# --- PHASE 2: EXTRACT ---
print("Extracting data from CSV...")
df = pd.read_csv('daily_sales.csv')

# --- PHASE 3: TRANSFORM & QA ---
print("Cleaning and transforming data...")
df = df.dropna(subset=['customer_id'])
df = df[(df['price_paid'] > 0) & (df['quantity'] > 0)]
df['customer_id'] = df['customer_id'].astype(int)
df['transaction_id'] = df['transaction_id'].astype(int)
df['product_id'] = df['product_id'].astype(int)
df['sale_date'] = pd.to_datetime(df['sale_date']).dt.strftime('%Y-%m-%d')

# --- PHASE 4: LOAD ---
print("Connecting to Data Warehouse...")
conn = sqlite3.connect('retail_warehouse.db')

print("Loading data into fact_sales...")
# The magic function! 
df.to_sql(name='fact_sales', con=conn, if_exists='append', index=False)

conn.close()
print("--- ETL Pipeline Completed Successfully! ---")