import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [1000, 1500, 1200, 1700, 1300, 1600, 1800, 1900, 2200, 2100, 2500, 2300]
plt.figure(figsize=(10, 6))
plt.bar(months, sales, color='c')
plt.title('Monthly Sales Data', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.show()
