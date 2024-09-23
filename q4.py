import numpy as np
sales_data = np.array([150000, 200000, 250000, 300000])
total_sales = np.sum(sales_data)
first_quarter_sales = sales_data[0]
fourth_quarter_sales = sales_data[3]
if first_quarter_sales > 0:  
    percentage_increase = ((fourth_quarter_sales - first_quarter_sales) / first_quarter_sales) * 100
else:
    percentage_increase = None 
print(f"Total Sales for the Year: ${total_sales:.2f}")
if percentage_increase is not None:
    print(f"Percentage Increase in Sales from Q1 to Q4: {percentage_increase:.2f}%")
else:
    print("Percentage Increase cannot be calculated (Q1 sales are zero).")
