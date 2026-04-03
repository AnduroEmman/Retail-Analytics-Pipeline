import sqlite3

conn = sqlite3.connect('retail_warehouse.db')

cursor = conn.cursor()

create_table_sql = """
CREATE TABLE IF NOT EXISTS dim_customer (
    customer_id INTEGER PRIMARY KEY,
    name text NOT NULL,
    email text NOT NULL,
    phone text NOT NULL,
    address text NOT NULL,
    city text NOT NULL,
    state text NOT NULL,
    zip_code text NOT NULL,
    date_of_birth date NOT NULL
);

CREATE TABLE IF NOT EXISTS dim_product (
    product_id INTEGER PRIMARY KEY,
    name text NOT NULL,
    description text,
    category text NOT NULL
);

CREATE TABLE IF NOT EXISTS fact_sales (

transaction_id INTEGER PRIMARY KEY,
customer_id INTEGER NOT NULL,
product_id INTEGER NOT NULL,
quantity INTEGER NOT NULL,
price_paid REAL NOT NULL,
sale_date date NOT NULL,
FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
FOREIGN KEY (product_id) REFERENCES dim_product(product_id)


);
"""

cursor.executescript(create_table_sql)

conn.commit()
conn.close()

print("database created successfully")