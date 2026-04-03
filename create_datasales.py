import csv

# Our messy, realistic daily sales data
data = [
    ['transaction_id', 'customer_id', 'product_id', 'quantity', 'price_paid', 'sale_date'],
    [1001, 1, 101, 2, 15.99, '2023-10-26'],
    [1002, 2, 102, 1, 29.50, '2023-10-26'],
    [1003, 1, 103, 5, -5.00, '2023-10-26'], # ERROR: Negative price!
    [1004, '', 101, 1, 15.99, '2023-10-26'], # ERROR: Missing customer_id!
    [1005, 3, 104, 0, 9.99, '2023/10/26'],   # ERROR: Zero quantity and weird date format!
    [1006, 4, 105, 3, 45.00, '2023-10-26']
]

with open('daily_sales.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("daily_sales.csv generated successfully!")