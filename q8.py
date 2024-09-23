import pandas as pd
from datetime import datetime, timedelta
data = {
    'product_name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product D'],
    'quantity_sold': [10, 5, 7, 8, 2, 3],
    'date_sold': ['2024-08-05', '2024-08-15', '2024-08-20', '2024-08-22', '2024-08-25', '2024-08-30']
}
sales_data = pd.DataFrame(data)
sales_data['date_sold'] = pd.to_datetime(sales_data['date_sold'])
today = datetime.now()
one_month_ago = today - timedelta(days=30)

filtered_data = sales_data[sales_data['date_sold'] >= one_month_ago]
grouped_data = filtered_data.groupby('product_name')['quantity_sold'].sum()
sorted_data = grouped_data.sort_values(ascending=False)
top_5_products = sorted_data.head(5)
print("Top 5 products sold in the past month:")
print(top_5_products)
