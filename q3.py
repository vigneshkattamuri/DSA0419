import numpy as np
house_data = np.array([
    [3, 1500, 300000],
    [5, 2500, 500000],
    [4, 1800, 400000],
    [6, 3000, 600000],
    [2, 1200, 200000],
    [5, 2200, 450000]
])
houses_with_more_than_four_bedrooms = house_data[house_data[:, 0] > 4]
sale_prices = houses_with_more_than_four_bedrooms[:, 2]
if sale_prices.size > 0:  
    average_sale_price = np.mean(sale_prices)
    print(f"Average Sale Price of Houses with More Than 4 Bedrooms: ${average_sale_price:.2f}")
else:
    print("No houses found with more than 4 bedrooms.")
