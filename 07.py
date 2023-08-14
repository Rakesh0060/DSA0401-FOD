import pandas as pd

data = {
    'customer ID': [1921, 1922, 1921, 1921, 1922, 1922, 1921],
    'order date': ['2002-08-08', '2002-08-09', '2002-08-10', '2002-08-11', '2002-08-12', '2002-08-13', '2002-08-14'],
    'product name': ['A', 'B', 'A', 'A', 'B', 'B', 'C '],
    'order quantity': [6, 5, 4, 7, 8, 9, 2]
}

order_data = pd.DataFrame(data)
order_data['order date'] = pd.to_datetime(order_data['order date'])

total_orders_per_customer = order_data['customer ID'].value_counts()
average_order_quantity_per_product = order_data.groupby('product name')['order quantity'].mean()
earliest_order_date, latest_order_date = order_data['order date'].min(), order_data['order date'].max()

print("Total number of orders made by each customer:\n", total_orders_per_customer)
print("\nAverage order quantity for each product:\n", average_order_quantity_per_product)
print("\nEarliest order date:", earliest_order_date, "\nLatest order date:", latest_order_date)
