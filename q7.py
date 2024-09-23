import pandas as pd
data = {
    'customer_id': [1, 2, 1, 3, 2, 1],
    'order_date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-02', '2024-01-03', '2024-01-04'],
    'product_name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product D'],
    'order_quantity': [1, 2, 1, 1, 3, 2]
}
order_data = pd.DataFrame(data)
order_data['order_date'] = pd.to_datetime(order_data['order_date'])
total_orders_by_customer = order_data['customer_id'].value_counts()
print("Total number of orders made by each customer:")
print(total_orders_by_customer)
average_order_quantity = order_data.groupby('product_name')['order_quantity'].mean()
print("\nAverage order quantity for each product:")
print(average_order_quantity)
earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()
print("\nEarliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
