import numpy as np
sales_data = np.array([
    [100, 150, 200],
    [120, 130, 140],  
    [80, 90, 100]     
])
average_prices_per_product = np.mean(sales_data, axis=1)
overall_average_price = np.mean(average_prices_per_product)
print("Average Prices for Each Product:")
for i, avg_price in enumerate(average_prices_per_product):
    print(f"Product {i + 1}: {avg_price:.2f}")

print(f"\nOverall Average Price of Products Sold: {overall_average_price:.2f}")
 
