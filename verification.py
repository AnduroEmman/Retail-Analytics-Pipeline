import sqlite3

conn = sqlite3.connect('retail_warehouse.db')

cursor = conn.cursor()

query = "SELECT * FROM fact_sales;"

cursor.execute(query)

rows = cursor.fetchall()

print("Data in fact_sales:")
for row in rows:
    print(row)

conn.commit()
conn.close()

print("Verification completed successfully")